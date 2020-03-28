from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import auth
from django.utils.crypto import get_random_string
from .models import token, exp, income
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum


###############################################signup##############################################
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password-retype']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'index.html', {'error' : 'username existance error'})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'])
                auth.login(request ,user)
                user_token = get_random_string(length = 48)
                token_create = token()
                token_create.user = request.user
                token_create.token = user_token
                token_create.save()
                return render(request, 'index.html', {'token' : user_token })
        else:
            return render(request, 'index.html', {'error' : 'pass match error'})
    else:
        return render(request, 'index.html')
###############################################login##############################################
@csrf_exempt
def login(request):
    if request.method == 'POST':
            user = auth.authenticate(username =  request.POST['username'],password = request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, "index.html", {'error':'password failure!'})
    else:
        return render(request, "index.html")
#######################################home(ADD:exp, inco)########################################
@csrf_exempt
@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        if request.POST.get('expent') and request.POST.get('amount1') and request.POST.get('date1'):
            expent = exp()
            expent.title = request.POST.get('expent')
            expent.amount = request.POST.get('amount1')
            expent.date = request.POST.get('date1')
            expent.user = request.user
            expent.save()
            return redirect('home')
        elif request.POST.get('income') and request.POST.get('amount2') and request.POST.get('date2'):
            inco = income()
            inco.title = request.POST.get('income')
            inco.amount = request.POST.get('amount2')
            inco.date = request.POST.get('date2')
            inco.user = request.user
            inco.save()
            return redirect('home')
    else:
        USER = request.user
        INCOME = income.objects.filter(user = USER).aggregate(Count('amount'), Sum('amount'))
        EXPENT = exp.objects.filter(user = USER).aggregate(Count('amount'), Sum('amount'))
        exp_per = 0
        inco_per = 0
        if EXPENT['amount__count'] is not 0 and EXPENT['amount__sum'] is not None and INCOME['amount__count'] is not 0 and INCOME['amount__sum'] is not None:
            exp_per = ((EXPENT['amount__sum'])*100)/INCOME['amount__sum']
            inco_per = (100 - exp_per)

        #stat = {'expent':EXPENT, 'income':INCOME}
        return render(request, 'add.html', {'username' : request.user ,'expent': exp_per, 'income': inco_per})
###############################################logout##############################################
@csrf_exempt
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
