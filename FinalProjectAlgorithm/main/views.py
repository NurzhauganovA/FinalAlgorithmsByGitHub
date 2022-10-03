import datetime

from django.shortcuts import render

from post.models import Post


def HomePage(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'main/index.html', context)


def PopularPosts(request):

    context = {

    }

    return render(request, 'main/popular_posts.html', context)


def FreshPosts(request):
    return render(request, 'main/fresh_posts.html')


def MySubscription(request):
    return render(request, 'main/my_subscription.html')