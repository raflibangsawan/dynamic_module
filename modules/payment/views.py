from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Payment

@login_required
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment/payment_list.html', {'payments': payments})

@login_required
def payment_create(request):
    if request.method == 'POST':
        currency = request.POST.get('currency')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        
        Payment.objects.create(
            currency=currency,
            amount=amount,
            description=description
        )
        messages.success(request, 'Payment created successfully.')
        return redirect('payment:payment_list')
    
    return render(request, 'payment/payment_form.html')

@login_required
def payment_delete(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        payment.delete()
        messages.success(request, 'Payment deleted successfully.')
        return redirect('payment:payment_list')
    return render(request, 'payment/payment_confirm_delete.html', {'payment': payment}) 