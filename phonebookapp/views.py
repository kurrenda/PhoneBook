from django.shortcuts import render, redirect

from .models import Email,Telefon,Osoba
from .forms import OsobaForm, TelefonForm


def list_users(request):
    user_list = Osoba.objects.prefetch_related('telefon_set','email_set').all()
    return render(request, 'index.html',{'users': user_list})

def create_user(request):
    form = OsobaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'index-form.html', {'form': form})



def create_phone(request, id):
    user = Osoba.objects.get(id=id)
    form = TelefonForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'index-phone.html', {'form': form})



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
        user.delete()
        return redirect('list_users')

    return render(request,'index-delete.html', {'user': user})
