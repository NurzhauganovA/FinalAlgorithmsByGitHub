from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from post.models import Post


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

    context = {

    }

    return render(request, 'post/popular_posts.html', context)


def FreshPosts(request):
    return render(request, 'post/fresh_posts.html')


def MySubscription(request):
    return render(request, 'post/my_subscription.html')