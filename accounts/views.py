from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User

# Create your views here.

def index(request):

    user = User.objects.all()

    context={
        'user': user,
    }
    return render(request, 'accounts/index.html', context)

def signup(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context=context)

def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:index")