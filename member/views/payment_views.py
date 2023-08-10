import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import uuid
from django.conf import settings
from member.models import Payment
import json

PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY

@api_view(['POST'])
def initiate_payment(request):
    data = json.loads(request.body)
    amount = data.get('amount')
    email = data.get('email')
    payment_method = data.get('payment_method')
    bank_name = data.get('bank_name')
    account_no = data.get('account_no')

    if not amount or not email or not payment_method:
        return Response({'error': 'Amount, Payment_method and email are required.'}, status=400)

    if payment_method == 'cash':
        reference = f"txn_{uuid.uuid4().hex}"
        payment = Payment.objects.create(
            amount = amount,
            email = email,
            payment_method = payment_method,
            payment_id = request.data.get('reference'),
        )
        payment.save()
        
    elif payment_method == 'online':
        if not bank_name or not account_no:
            return Response ({'message':'please provide bank name and account details '}, status=400)
        reference = f"txn_{uuid.uuid4().hex}"
        payment = Payment.objects.create(
            amount = amount,
            email = email,
            payment_method = payment_method,
            payment_id = request.data.get('reference'),
            bank_name = bank_name,
            account_no = account_no,
        )
        payment.save()
       

    # Make a request to the Paystack API to initialize the payment
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "reference": reference,
        "amount": amount,
        "email": email,
        "bank_name": bank_name,
        "account_no": account_no,
        "callback_url": "https://lobster-app-et3xm.ondigitalocean.app/api/payment/callback/",  
    }

    response = requests.post('https://api.paystack.co/transaction/initialize', json=data, headers=headers)

    # Process the response from Paystack API
    if response.status_code == 200:
        data = response.json()
        return Response(data)
    else:
        return Response({'error': 'Failed to initiate payment'}, status=500)

@api_view(['POST'])
def payment_callback(request):
    reference = request.data.get('reference')

    if not reference:
        return Response({'error': 'Reference is required.'}, status=400)

    # Make a request to the Paystack API to verify the payment
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.get(f'https://api.paystack.co/transaction/verify/{reference}', headers=headers)

    # Process the response from Paystack API
    if response.status_code == 200:
        data = response.json()
        if data['data']['status'] == 'success':
              # Payment is successful, process the order or save payment information
            # You can write your own logic here
                payment = Payment.objects.create(
                    email = request.data.get('email'),
                    payment_id = request.data.get('reference'),
                    amount = request.data.get('amount'),
                    )
                payment.save()


                return Response({'message': 'Payment successful'})
        else:
            return Response({'error': 'Payment not successful'}, status=400)
    else:
        return Response({'error': 'Verification failed'}, status=500)
