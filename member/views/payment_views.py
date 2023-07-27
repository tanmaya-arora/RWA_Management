from django.shortcuts import render, redirect
from django.forms import PaymentForm

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