from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import auth
from django.utils.crypto import get_random_string
from .models import token, exp

# Create your views here.

@csrf_exempt
def home(request):
        if request.method == 'POST':
            t_user = get_object_or_404(User, token__token = request.POST['token'] )
            #if request.POST['income'] and request.POST['amount']:
                #income.objects.create(user = t_user, title = request.POST['income'], amount = request.POST['amount'])
            #elif request.POST['expent'] and request.POST['amount']:
            exp.objects.create(user = t_user, title = request.POST['expent'], amount = request.POST['amount'])
            #else:
            return HttpResponse('erooooooooooooooorrrrrrrrrrr')
        else:
            return render(request, 'add.html')


@csrf_exempt
def signup(request):

#   send_mail(
#        'Subject here',
#        'Here is the message.',
#        'erfan.aliagdam1831@gmail.com',
#        ['yasiw49043@provamail.com'],
#        fail_silently=False,
#    )
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password-retype']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {'error' : 'username existance error'})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'])
                auth.login(request ,user)
                user_token = get_random_string(length = 48)
                token_create = token()
                token_create.user = request.user
                token_create.token = user_token
                token_create.save()
                return render(request, 'token.html', {'user_token' : user_token })
        else:
            return render(request, 'signup.html', {'error' : 'pass match error'})
    else:
        return render(request, 'signup.html')



@csrf_exempt
def login(request):
    if request.method == 'POST':
            user = auth.authenticate(username =  request.POST['username'],password = request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return HttpResponse('password failed')
    else:
        return render(request, "login.html")
