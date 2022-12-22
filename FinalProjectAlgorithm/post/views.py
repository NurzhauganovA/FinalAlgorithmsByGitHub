from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView

from .models import Post, CategoryPost
from account.models import SubscribeToAuthorOfPost, ProfileSettings, CustomUser

from django.http import HttpResponseRedirect

from django.urls import reverse, reverse_lazy


def CreatePost(request):
    pass


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        post = get_object_or_404(Post, id=self.object.id)
        context['profiles'] = CustomUser.objects.filter(username=post.author.username)
        context['all_posts'] = Post.objects.exclude(id=post.id)

        return context


class CategoryPostDetailView(DetailView):
    model = CategoryPost
    template_name = 'post/category_post_detail.html'
    context_object_name = 'category_post'

    def get_context_data(self, **kwargs):
        context = super(CategoryPostDetailView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(category=self.object.id)
        return context


def LikePost(request, pk):
    post_like = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked_post = False
    if post_like.like_post.filter(id=request.user.id).exists():
        post_like.like_post.remove(request.user)
        liked_post = False
    else:
        post_like.like_post.add(request.user)
        liked_post = True
    return HttpResponseRedirect(reverse('detail_post', args=[str(pk)]))


def SubscribeAuthor(request, pk):
    subscribe_author = get_object_or_404(SubscribeToAuthorOfPost, id=request.POST.get('post_author_id'))
    subscribed_author = False
    return HttpResponseRedirect(reverse('home', args=[str(pk)]))
