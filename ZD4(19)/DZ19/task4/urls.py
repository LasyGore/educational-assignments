from django.urls import path
from .views import create_posts, update_post, list_posts, delete_post, filter_posts

urlpatterns = [
    path('create/', create_posts, name='create_posts'),
    path('update/<int:post_id>/', update_post, name='update_post'),
    path('list/', list_posts, name='list_posts'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('filter/', filter_posts, name='filter_posts'),
]