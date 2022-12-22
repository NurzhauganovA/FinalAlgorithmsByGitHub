import re

from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import CustomUser, ProfileSettings
from post.models import MySubscription


def ProfileView(request):

    users = CustomUser.objects.all()
    profile = ProfileSettings.objects.get(user=request.user)
    date_joined = str(profile.user.date_joined.strftime('%b')) + ' ' + str(profile.user.date_joined.day) + ', ' + str(profile.user.date_joined.year)

    subscription = MySubscription.objects.all()
    subscribers = ''

    if request.user in subscription:
        subscribers = request.user
    if subscribers in users:
        print(profile.user)

    context = {
        'profile': profile,
        'date_joined': date_joined,
        'subscribers': subscribers
    }

    print(profile)

    return render(request, 'account/profile_page.html', context)


def AccountLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('account_login')
    else:
        return render(request, 'account/login.html')


def AccountRegister(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        regex = "^[a-zA-Zа-яА-ЯёЁ]+$"
        pattern = re.compile(regex)

        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('account_register')
            else:
                user = CustomUser.objects.create_user(username=username, password=password1)
                user.save()
                profile = ProfileSettings.objects.create(user=user, profile_avatar='', entry_draft='')
                profile.save()
                login_user = authenticate(username=username, password=password1)
                login(request, login_user)
        else:
            messages.info(request, 'Password not matching')
            return redirect('account_register')
        return redirect('home')
    else:
        return render(request, 'account/register.html')


def AccountLogout(request):
    auth.logout(request)
    return redirect('/')