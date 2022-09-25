from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .models import Task

def signup(request):

    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password_repeat']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username Taken')
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=pass1)
                user.save()

                messages.success(request, 'Profile Created!')
                return redirect('login')
        else:
            messages.warning(request, 'Password does not match')
            return redirect('signup')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.warning(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'Logged Out')
        return redirect('login')

@login_required(login_url='login')
def profile(request):
    data=Task.objects.all()
    context={'tasks':data}
    return render(request, 'profile.html', context)

