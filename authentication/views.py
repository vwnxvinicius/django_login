from pickletools import read_unicodestring1
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('authentication:success')
        else:
            message = messages.add_message(request, messages.INFO, 'Your credentials are incorrect')
            return render(request, 'authenticate/login.html', {'message': message})
    else:
        return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    logged_out = messages.add_message(request, messages.INFO, 'You loged out succesfully')
    return redirect('/', {'logged_out': logged_out})

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse_lazy('authentication:success'))
        else:
            return render(request, 'authenticate/register.html', {'form': form})
    else:
        form = RegisterUserForm(request.POST)
        return render(request, 'authenticate/register.html', {'form': form})

def success(request):
    return render(request, 'authenticate/successfull.html')