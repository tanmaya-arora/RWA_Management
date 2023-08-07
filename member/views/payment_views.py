from django.shortcuts import render, redirect
from django.forms import PaymentForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
import uuid
import requests

PAYSTACK_SECRET_KEY = "sk_test_6ebc624f934b56fa2985396ff79c3057b140eab6"

def payment_views(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            # Add any additional logic here, such as processing the payment or sending payment confirmation emails
            return redirect('payment_success')  # Redirect to a success page after payment
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form})

def payment_success_view(request):
    return render(request, 'payment_success.html')

@api_view(['POST'])
def initiate_payment(request):
    amount = request.data.get('amount')
    email = request.data.get('email')

    if not amount or not email:
        return Response({'error': 'Amount and email are required.'}, status=400)

    # Create a unique reference for the transaction (you can use your own logic to generate this)
    reference = f"txn_{uuid.uuid4().hex}"

    # Make a request to the Paystack API to initialize the payment
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "reference": reference,
        "amount": amount,
        "email": email,
        "callback_url": "http://localhost:8000/api/payment/callback/",  
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
            return Response({'message': 'Payment successful'})
        else:
            return Response({'error': 'Payment not successful'}, status=400)
    else:
        return Response({'error': 'Verification failed'}, status=500)