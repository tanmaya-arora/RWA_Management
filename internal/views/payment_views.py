from django.http import JsonResponse, HttpResponse
from django.conf import settings
import hashlib
import base64
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import uuid


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
