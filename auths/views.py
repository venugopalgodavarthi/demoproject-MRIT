from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from auths.forms import register
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.conf import settings

from pro1.settings import EMAIL_HOST_USER 
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def registerview(request):
    form=register()
    if request.method=='POST':
        form=register(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            email= form.cleaned_data['email']
            subject='welcome to My Student World'
            message=f'hi {user} thank you for registartion.'
            email_form = settings.EMAIL_HOST_USER
            rec = [email,]
            send_mail(subject,message,email_form,rec)
            users=form.save()
            login(request,users)
            messages.success(request,'thanks for your registaration')
        else:
            messages.error(request,'your not register') 
    return render(request,'register.html',{'form':form})

def loginview(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            print(user,pas)
            users= authenticate(username=user,password=pas)
            if users is not None:
                login(request,users)
                messages.info(request,f'your login success mr.{user}')
                return redirect('/app1/home')
            else:
                messages.error(request,'incorrect username or password')
        else:
            messages.error(request,'invalid username or password')
    return render(request,'login.html',{'form':form})

def logoutview(request):
    logout(request)
    return redirect('welcome')

            
                
            
            
    