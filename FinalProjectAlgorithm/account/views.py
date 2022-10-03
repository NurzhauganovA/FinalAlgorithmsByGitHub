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
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        regex = "^[a-zA-Zа-яА-ЯёЁ]+$"
        pattern = re.compile(regex)

        if password1 == password2:
            if pattern.search(str(first_name)) is not None and pattern.search(str(last_name)) is not None:
                if CustomUser.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    return redirect('account_register')
                elif CustomUser.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('account_register')
                else:
                    user = CustomUser.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, age=age, gender=gender, phone_number=phone_number, password=password1)
                    user.save()
                    profile = ProfileSettings.objects.create(user=user, profile_avatar='', entry_draft='')
                    profile.save()
                    login_user = authenticate(username=username, password=password1)
                    login(request, login_user)

            else:
                messages.info(request, 'First name or Last name is invalid!')
                return redirect('account_register')
        else:
            messages.info(request, 'Password not matching')
            return redirect('account_register')
        return redirect('home')
    else:
        return render(request, 'account/register.html')


def AccountLogout(request):
    auth.logout(request)
    return redirect('/')