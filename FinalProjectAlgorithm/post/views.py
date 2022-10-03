from django.shortcuts import render
from django.views.generic import DetailView

from post.models import Post, CategoryPost


def CreatePost(request):
    pass


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context


class CategoryPostDetailView(DetailView):
    model = CategoryPost
    template_name = 'post/category_post_detail.html'
    context_object_name = 'category_post'

    def get_context_data(self, **kwargs):
        context = super(CategoryPostDetailView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(category=self.object.id)
        return context