from django.shortcuts import render, redirect
from .forms import RegistrationUserForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from main_page.models import Presentation


def login_view(request):
    form = UserLoginForm(request.POST or None)
    greetings = Presentation.objects.filter(is_visible=True, greetings=True)
    next_get = request.GET.get('next')

    if form.is_valid():
        password = form.cleaned_data['password']
        username = form.cleaned_data['username']

        user = authenticate(username=username, password=password)
        login(request, user)

        next_post = request.POST.get('next')

        return redirect(next_get or next_post or '/')

    return render(request, 'login.html', context={'form': form, 'greetings': greetings})


def registration_view(request):
    form = RegistrationUserForm(request.POST or None)
    greetings = Presentation.objects.filter(is_visible=True, greetings=True)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()

        return render(request, 'registration_done.html', context={'user': new_user, 'greetings': greetings})
    return render(request, 'registration.html', context={'form': form, 'greetings': greetings})


def logout_view(request):
    logout(request)
    return redirect('/')


