from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Email,Telefon,Osoba
from .forms import OsobaForm, TelefonForm, EmailForm
from django.contrib import messages
from django.db.models import Value as V
from django.db.models.functions import Concat

def list_users(request):
    user_list = Osoba.objects.prefetch_related('telefon','email')
    return render(request, 'index.html',{'users': user_list})

def create_user(request):

    form = OsobaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'index-form.html', {'form': form})



def create_phone(request, id):

    user = Osoba.objects.get(id=id)
    form = TelefonForm(request.POST or None)
    phone = Telefon(osoba=user)
    form.instance = phone
    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'index-phone.html', {'form': form})


def create_email(request, id):

    user = Osoba.objects.get(id=id)
    form = EmailForm(request.POST or None)
    phone = Email(osoba=user)
    form.instance = phone
    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'index-email.html', {'form': form})



def update_user(request, id):
    user = Osoba.objects.get(id=id)
    form = OsobaForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'index-form.html', {'form':form, 'user': user})


def delete_user(request, id):
    user = Osoba.objects.get(id=id)

    if request.method == 'POST':
        if not user.email.exists() and not user.telefon.exists():
            user.delete()
            return redirect('list_users')
        else:
            messages.error(request, 'Nie możesz zmienić tego pola')
            return redirect('error')

    return render(request,'index-delete.html', {'user': user})


def query(request):

    query= request.GET.get('q')

    user = Osoba.objects.annotate(full_name=Concat('imie', V(' '), 'nazwisko')).filter(
                                Q(full_name__icontains=query) |
                                Q(imie__icontains=query)|
                                Q(nazwisko__icontains=query)|
                                Q(email__email__icontains=query)|
                                Q(telefon__telefon__icontains=query)).distinct()

    return render(request, 'index.html', {'users':user})

def error(request):

    return render(request, 'index-error.html')