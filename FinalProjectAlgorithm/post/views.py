from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView

from .models import Post, CategoryPost
from account.models import SubscribeToAuthorOfPost, ProfileSettings, CustomUser

from django.http import HttpResponseRedirect

from django.urls import reverse, reverse_lazy

from .forms import CommentForm
from django.views.generic.edit import FormMixin


def CreatePost(request):
    pass


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_post', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post_name = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.like_post.filter(id=self.request.user.id).exists():
            liked = True

        subscribed = False
        if stuff.subscribe_author.filter(id=self.request.user.id).exists():
            subscribed = True

        post = get_object_or_404(Post, id=self.object.id)
        context['profiles'] = CustomUser.objects.filter(username=post.author.username)
        context['all_posts'] = Post.objects.exclude(id=post.id)
        context['total_likes'] = total_likes
        context['liked'] = liked
        context['subscribed'] = subscribed

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
    post_like = get_object_or_404(Post, id=request.POST.get('detail_post_like'))
    liked_post = False
    if post_like.like_post.filter(id=request.user.id).exists():
        post_like.like_post.remove(request.user)
        liked_post = False
    else:
        post_like.like_post.add(request.user)
        liked_post = True
    return HttpResponseRedirect(reverse('detail_post', args=[str(pk)]))


def SubscribeAuthor(request, pk):
    subscribe_author = get_object_or_404(Post, id=request.POST.get('post_author_id'))
    subscribed_author = False
    if subscribe_author.subscribe_author.filter(id=request.user.id).exists():
        subscribe_author.subscribe_author.remove(request.user)
        subscribed_author = False
    else:
        subscribe_author.subscribe_author.add(request.user)
        subscribed_author = True
    return HttpResponseRedirect(reverse('detail_post', args=[str(pk)]))
