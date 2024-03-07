from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from . import forms

def user_register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data["password1"])
            new_user.save()
            new_user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            
            login(request, new_user)
            return redirect("base:home-page")
    else:
        form = forms.UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, 'userauths/register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("base:home-page")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("userauths:login")
    else:
        form = forms.UserLoginForm()
        context = {
            'form': form
        }
        return render(request, 'userauths/login.html', context)
def user_logout(request):
    logout(request)
    return redirect("userauths:login-page")