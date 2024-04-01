from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from userauths.models import User
from . import forms
from django.core.exceptions import ValidationError

def user_register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST or None)
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if form.is_valid():
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect("userauths:signup-page")
            if password1 != password2:
                messages.error(request, "Passwords don't match")
                return redirect("userauths:signup-page")
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            new_user = authenticate(username=form.cleaned_data["email"], password=form.cleaned_data["password1"])
            login(request, new_user)
            return redirect("base:home-page")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            return redirect("userauths:signup-page")
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
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.filter(email=email).first()  # Check if the email exists
            if user is not None:
                if user.check_password(password):  # Check if the password is correct
                    user = authenticate(email=user.email, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect("base:home-page")
                else:
                    messages.error(request, "Incorrect password")
                    return redirect("userauths:login-page")
            else:
                messages.error(request, "Account not found, you should signup first")
                return redirect("userauths:login-page")
        else:
            messages.error(request, "Please enter a correct email address")
            return redirect("userauths:login-page")
    else:
        form = forms.UserLoginForm()
        context = {
            'form': form
        }
        return render(request, 'userauths/login.html', context)
def user_logout(request):
    logout(request)
    return redirect("userauths:login-page")