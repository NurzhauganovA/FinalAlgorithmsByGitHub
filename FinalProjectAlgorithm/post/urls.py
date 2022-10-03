from django.urls import path
from . import views


urlpatterns = [
    path('create', views.CreatePost, name='create_post'),
    path('<int:pk>', views.PostDetailView.as_view(), name='detail_post'),
    path('category/<int:pk>', views.CategoryPostDetailView.as_view(), name='detail_category_post'),
]
