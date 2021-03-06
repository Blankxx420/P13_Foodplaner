from django.contrib import messages
from django.contrib.auth import login, authenticate

# uses custom form instead of UserCreationForm
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def register(request):
    """Displays the registration page"""
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Login automatically
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            messages.success(
                request, f"Compte créé pour l'adresse email : {email} !")
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect("menu/home.html")
    else:
        form = UserRegistrationForm()
    return render(
        request, "users/register.html", {"form": form}
    )  # form as a context to be used in template


@login_required  # only allows this page to logged_in users
def account(request):
    """Displays the account page when a user is logged in"""
    if request.method == "POST":
        update_user_form = UserUpdateForm(request.POST, instance=request.user)
        if update_user_form.is_valid():
            update_user_form.save()
            messages.success(request, f"Votre compte à été mis à jour !")
            return redirect('account')
    else:
        update_user_form = UserUpdateForm(instance=request.user)
        context = {
            "update_user_form": update_user_form
        }
        return render(request, "users/account.html", context)
