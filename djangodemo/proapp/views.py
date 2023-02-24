from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['cpassword']

        if password == conf_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save()
                print('User Created')
        else:
            messages.info(request, 'Passwords does not match')
            return redirect('registration')
        return redirect('login')
    return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
