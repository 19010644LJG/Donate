from django.shortcuts import render
from account.models import Account

# Create your views here.
def index(request):
    context = {}

    if request.user.is_authenticated:
        account = Account.objects.get(user=request.user)
        context.setdefault('username', account.user.username)

    return render(request, 'main/index.html', context)

