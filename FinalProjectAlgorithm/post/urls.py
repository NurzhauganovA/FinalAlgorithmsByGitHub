from django.urls import path
from . import views


urlpatterns = [
    path('create', views.CreatePost, name='create_post'),
    path('<int:pk>', views.PostDetailView.as_view(), name='detail_post'),
    path('category/<int:pk>', views.CategoryPostDetailView.as_view(), name='detail_category_post'),
    path('like_post/<int:pk>', views.LikePost, name='like_post'),
    path('subscribe_to_author_of_post/<int:pk>', views.SubscribeAuthor, name='subscribe_post_author')
]
