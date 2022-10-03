from django.db import models
from account.models import CustomUser


class CategoryPost(models.Model):
    category_image = models.ImageField('Category image', blank=True, null=True, upload_to='category_images/')
    title = models.CharField('Category title', max_length=255)
    description = models.TextField('Category description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category_post'


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_image = models.ImageField('Post image', blank=True, null=True, upload_to='post_images/')
    title = models.CharField('Post title', max_length=255)
    description = models.TextField('Post description')
    category = models.ForeignKey(CategoryPost, verbose_name='Post category', on_delete=models.CASCADE)
    date_created = models.DateTimeField('Post date created', auto_now_add=True)
    like_post = models.ManyToManyField(CustomUser, verbose_name='Do you like this post?', blank=True, null=True, related_name='like_post')
    view_post = models.ManyToManyField(CustomUser, verbose_name='You viewed this post', blank=True, null=True, related_name='view_post')

    def __str__(self):
        return f'Title: {self.title} <==> Category: {self.category}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'


class Comment(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title of comments')
    post_name = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Name of Post', blank=True, null=True, related_name='comments_post')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Author of comments', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Text of comments')
    status = models.BooleanField(verbose_name='Comment visibility', default=True)

    def __str__(self):
        return f'Title: {self.title} <==> Post: {self.post_name} <==> Author: {self.author}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comment'


class MySubscription(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='My subscription user', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField('Subscribe time', auto_now=True)

    def __str__(self):
        return str({self.user})

    class Meta:
        verbose_name = 'My subscription'
        verbose_name_plural = 'My subscriptions'
        db_table = 'my_subscription'


class BlockedUser(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='Blocked user', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField('Block time', auto_now_add=True)

    def __str__(self):
        return {self.user}

    class Meta:
        verbose_name = 'Blocked user'
        verbose_name_plural = 'Blocked users'
        db_table = 'blocked_user'
