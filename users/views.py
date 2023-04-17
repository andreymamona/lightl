from django.shortcuts import render, redirect
import logging
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import logout, login, authenticate

from users.forms import RegisterForm, LoginForm

from faker import Faker
fake = Faker()


logger = logging.getLogger(__name__)


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['are_you_older_18'] is True:
                if form.cleaned_data['password'] == form.cleaned_data['repeat_password']:
                    # Process validated data
                    user = User.objects.create_user(email=form.cleaned_data['email'],
                                                    password=form.cleaned_data['password'],
                                                    )
                    return HttpResponse(f"Thanks for registration :) <br> <p><a href='/'>Main page</a></p>")
                else:
                    return HttpResponse(f"Sorry, you entered different passwords <br> <p><a href='/'>Main page</a></p>"
                                        f"<br> <p><a href='/register'>Registration</a></p>")
            else:
                return HttpResponse(f"Sorry, you must be older than 18 <br> <p><a href='/'>Main page</a></p>")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request,
                                email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'],
                                )
            if user is None:
                return HttpResponse('BadRequest', status=400)
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})
