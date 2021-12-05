from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Account

def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        account = Account.objects.get(user=user)

        if user is None:
            return redirect('login')

        else:
            request.session['name'] = account.name

        auth.login(request, user)
        return redirect('index')
    else:
        return render(request, 'account/login.html')

def logout(request):
    if request.session.get('name'):
        del request.session['name']
        auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        id = request.POST.get('id')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        birth = request.POST.get('birth')
        gender = request.POST.get('gender')
        phoneNumber = request.POST.get('phone_number')

        # Password 일치 여부
        if password != password_confirm:
            return redirect('register')

        user = User.objects.create_user(username=id, password=password)
        user.save()

        account = Account(user=user,name=name,birth=birth,gender=gender,phoneNumber=phoneNumber)
        account.save()

        return render(request, 'main/index.html')
    else:
        return render(request, 'account/register.html')