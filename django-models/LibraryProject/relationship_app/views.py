from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


def _has_role(user, role_name):
    """Safe check for a user's profile role."""
    try:
        profile = getattr(user, "userprofile", None)
        return bool(profile) and profile.role == role_name
    except Exception:
        return False

def is_admin(user):
    return _has_role(user, "Admin")

def is_librarian(user):
    return _has_role(user, "Librarian")

def is_member(user):
    return _has_role(user, "Member")

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")