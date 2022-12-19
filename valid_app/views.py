from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


def index(request):
    if request.method == "POST":
        registration = Registration(request.POST)
        if registration.is_valid():
            name = registration.cleaned_data['name']
            email = registration.cleaned_data['email']
            password = registration.cleaned_data['password']
        return HttpResponse(
            f'{name}, поздравляю с регистрацией <br> Указанные вами данные: <br> Имя - {name}, <br> email - {email}, <br> пароль - {password}')
    registration = Registration()
    return render(request, 'valid_app/index.html', context={'form': registration})


def sign(request):
    if request.method == 'POST':
        sign = SignForm(request.POST)
        if sign.is_valid():
            name = sign.cleaned_data['email']
            password = sign.cleaned_data['password']
            if name == 'User1' and password == '12345678':
                return HttpResponse('Поздравляю с успешным входом')
        else:
            return redirect(index)
    else:
        sign = SignForm()
        return render(request, 'valid_app/sign.html', {'form': sign})
