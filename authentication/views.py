from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'authenticate/home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse_lazy('authentication:login'))
        else:
            return render(request, 'authenticate/register.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        return render(request, 'authenticate/register.html', {'form': form})
