import requests
from django.shortcuts import render, redirect
from account.models import Account
from donate.models import Donate
from django.contrib.auth.models import User

def donate(request):
        if not request.user.is_authenticated:
                return redirect('login')

        card = Donate.objects.all()
        context = {
                'card': card,
        }

        return render(request, 'donate/donate.html', context)

def donate_pay(request):
        if not request.user.is_authenticated:
                return redirect('login')

        if request.method == "POST":
                donation = request.POST.get('donation')
                select = request.POST.get('select')

                donate = Donate(user=request.user, donation=donation, select=select)
                donate.save()

        return render(request, 'donate/donate_pay.html')


def donate_confirm(request):
        if not request.user.is_authenticated:
                return redirect('login')

        card = Donate.objects.all()
        context = {
                'card': card,
        }

        return render(request, 'donate/donate_confirm.html', context)


def donate_admin(request):
        name = request.session.get('name')
        account = Account.objects.get(name=name)
        card = Donate.objects.all()
        context = {
                'card': card,
        }

        if account.user.is_superuser:
                return render(request, 'donate/donate_admin.html',context)

def donate_accept(request,id):
        donate = Donate.objects.get(id=id)
        donate.accept = '승인'
        donate.save()
        return redirect('donate_admin')