from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
from security.forms import SignupForm, LoginForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
        print form.errors
    else:
        form = SignupForm()
    data = {"form": form}
    return render(request, "signup.html", data)


@login_required
def special_page(request):
    data = {}
    return render(request, "special.html", data)



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("special")
        print form.errors
    else:
        form = LoginForm()
    data = {"form": form}
    return render(request, "login.html", data)

