from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponseRedirect

def register(request):
    if request.user.is_authenticated:
        homeurl = reverse('home')
        return HttpResponseRedirect(homeurl)
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
        else:        
            form = RegistrationForm()
        return render(request,'accounts/register.html',{'form':form})

def auth_login(request):
    if request.user.is_authenticated:
        homeurl = reverse('home')
        return HttpResponseRedirect(homeurl)
    else:
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    homeurl = reverse('home')
                    return HttpResponseRedirect(homeurl)
        else:
            form = LoginForm()
        return render(request,'accounts/login.html',{'form':form})
    
def auth_logout(request):
    logout(request)
    loginurl = reverse('login')
    return HttpResponseRedirect(loginurl)