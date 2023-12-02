from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordResetView


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.first_name = user.first_name.capitalize()
            user.last_name = user.last_name.capitalize()
            user.save()


            authenticated_user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            print(form.cleaned_data["username"], form.cleaned_data['password1'])
            if authenticated_user:
                login(request, authenticated_user)
                return redirect(reverse('course:course-list'))
            else:
                print("not authenticated")
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
        }
    return render(request, 'user/register.html', context=context)  