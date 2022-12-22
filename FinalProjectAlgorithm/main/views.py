from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from post.models import Post

import datetime
from datetime import date, timedelta


def MainPage(request):
    return redirect('account_login')


class HomePage(ListView):
    model = Post
    template_name = 'post/index.html'

    def get_context_data(self, *args, **kwargs):

        context = super(HomePage, self).get_context_data(**kwargs)

        posts = Post.objects.all()

        context['posts'] = posts

        return context


def PopularPosts(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'post/popular_posts.html', context)


def FreshPosts(request):

    current_date = datetime.datetime.today()
    ago_date = current_date - timedelta(days=7)

    posts = Post.objects.all().filter(date_created__gte=ago_date)

    context = {
        'posts': posts
    }

    return render(request, 'post/fresh_posts.html', context)


def MySubscription(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'post/my_subscription.html', context)