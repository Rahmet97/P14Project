from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, hashers, authenticate, login, logout
from django.contrib import messages
from django.views import View

User = get_user_model()


class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('/accounts/register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('/accounts/register')
            else:
                user = User.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=hashers.make_password(password1)
                )
                user.save()
                return redirect('/accounts/login')
        else:
            messages.error(request, 'Passwords are not same!')
            return redirect('/accounts/register')


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or password invalid!')
            return redirect('/accounts/login')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')
