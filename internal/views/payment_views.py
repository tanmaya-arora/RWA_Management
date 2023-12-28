from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from django.conf import settings
from internal.models import Payment
from internal.serializers import PaymentSerializer, UserSerializer
from django.contrib.auth.models import User
import hashlib
import base64
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
import uuid


@api_view(['GET'])
def get_all_payments(request):
    payment = Payment.objects.all()
    serializer = PaymentSerializer(payment, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_active_user_payments(request,pk):
    try:
        payment = Payment.objects.filter(user=pk)
        serializer = PaymentSerializer(payment, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
         return Response(data={'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def add_cash_or_bank_payment(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    try:
        user_email = User.objects.get(email=data_dict['email'])
        response = {}

        if 'bankname' in data_dict and 'bank_ac_no' in data_dict:
            payment = Payment.objects.create(
                user=user_email,
                reference_id=data_dict['reference_id'],
                amount=float(data_dict['amount']),
                bank_acname=data_dict['bankname'],
                bank_acnumber=data_dict['bank_ac_no'],
                payment_method="Bank Transfer"
            )
            serializer = PaymentSerializer(payment, many=False)
            response['info'] = f"Payment of Rs.{data_dict['amount']} done successfully via Bank Transfer"
            response['data'] = serializer.data
        else:
            payment = Payment.objects.create(
                user=user_email,
                reference_id=data_dict['reference_id'],
                amount=float(data_dict['amount']),
                payment_method="Cash"
            )
            serializer = PaymentSerializer(payment, many=False)
            response['info'] = f"Cash Payment of Rs.{data_dict['amount']} done successfully"
            response['data'] = serializer.data
        return Response(data=response, status=status.HTTP_200_OK)
    except Exception as e:
         return Response(data={'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def generate_paytm_token(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    requested_amount = data_dict.get('amount')
    unique_orderid = uuid.uuid4().hex
    email = data_dict.get('email')

    if requested_amount:
            paytm_params = {
                "MID": settings.PAYTM_MERCHANT_ID,
                "ORDER_ID": unique_orderid,  
                "CUST_ID": email,
                "CHANNEL_ID": "WEB",
                "INDUSTRY_TYPE_ID": "Retail",
                "WEBSITE": settings.PAYTM_WEBSITE,
                "CALLBACK_URL": settings.PAYTM_CALLBACK_URL,
                "TXN_AMOUNT": requested_amount,
            }

            paytm_params["CHECKSUMHASH"] = generate_checksum(paytm_params, settings.PAYTM_MERCHANT_KEY)

            return JsonResponse(paytm_params)
    else:
            return HttpResponse("Invalid amount provided.")
    
def generate_checksum(params, key):
    paytm_params = {}
    for key, value in params.items():
        paytm_params[key] = str(value)

    data = "|".join([str(value) for value in paytm_params.values()])
    checksum = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return base64.b64encode(checksum.encode()).decode('utf-8')

@csrf_exempt
def verify_checksum(data, checksum, merchant_key):
    data_values = [str(value) for value in data.values()]
    data_string = "|".join(data_values)
    print(data_string)

    generated_checksum = hashlib.sha256(merchant_key.encode('utf-8')).hexdigest()
    generated_checksum = base64.b64encode(generated_checksum.encode()).decode('utf-8')

    return generated_checksum == checksum

@csrf_exempt
def paytm_callback(request):
    if request.method == 'POST':
        data = request.POST.dict()
        received_checksum = data.get('CHECKSUMHASH', '')

        is_checksum_valid = verify_checksum(data, received_checksum, settings.PAYTM_MERCHANT_KEY)

        if is_checksum_valid:
            if data.get('STATUS') == 'TXN_SUCCESS':
                return HttpResponse("Payment successful. Thank you!")

            elif data.get('STATUS') == 'TXN_FAILURE':
                return HttpResponse("Payment failed. Please try again later.")
        else:
            return HttpResponse("Checksum verification failed.")

    return HttpResponse("Invalid request method.")
