from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Volunteer, Contact, Donation


def home(request):
    return render(request, 'ngo_app/home.html')


def about(request):
    return render(request, 'ngo_app/about.html')


@login_required(login_url='login')
def donate(request):
    

    return render(request, 'ngo_app/donate.html')


@login_required(login_url='login')
def volunteer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reason = request.POST.get('reason')

        Volunteer.objects.create(
            vname=name,
            vemail=email,
            vphno=phone,
            vaddress=reason
        )

        return render(request, 'ngo_app/volunteer.html', {
            'success': True,
            'name': name
        })

    return render(request, 'ngo_app/volunteer.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            cname=name,
            cemail=email,
            csubject=subject,
            cmessage=message,
        )
        return render(request, 'ngo_app/contact.html', {
            'success': True,
            'name': name
        })

    return render(request, 'ngo_app/contact.html')


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully! 🎉")
            return redirect('home')
        else:
            messages.error(request, "Please check the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'ngo_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}! 🌟")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'ngo_app/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('home')
