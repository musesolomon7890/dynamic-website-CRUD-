from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone
from .forms import PhoneForm

def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'phone_list.html', {'phones': phones})

def phone_detail(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    return render(request, 'phone_detail.html', {'phone': phone})

def phone_create(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.save()
            return redirect('phone_detail', pk=phone.pk)
    else:
        form = PhoneForm()
    return render(request, 'phone_form.html', {'form': form})

def phone_update(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    if request.method == 'POST':
        form = PhoneForm(request.POST, instance=phone)
        if form.is_valid():
            phone = form.save()
            return redirect('phone_detail', pk=phone.pk)
    else:
        form = PhoneForm(instance=phone)
    return render(request, 'phone_form.html', {'form': form})

def phone_delete(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('phone_list')
    return render(request, 'phone_confirm_delete.html', {'phone': phone})
