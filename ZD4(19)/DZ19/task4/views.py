from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http import HttpResponse

def create_posts(request):
    Post.objects.create(title='Первый пост', content='Содержание первого поста', published_date=timezone.now(), author=User.objects.get(pk=1))
    Post.objects.create(title='Второй пост', content='Содержание второго поста', published_date=timezone.now(), author=User.objects.get(pk=1))
    Post.objects.create(title='Третий пост', content='Содержание третьего поста', published_date=timezone.now(), author=User.objects.get(pk=2))
    return HttpResponse("Посты созданы.")

def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.title = 'Новый заголовок'
    post.save()
    return HttpResponse(f"Заголовок поста изменён на: {post.title}")

def list_posts(request):
    all_posts = Post.objects.all()
    output = ', '.join([post.title for post in all_posts])
    return HttpResponse(f"Все посты: {output}")

def delete_post(request, post_id):
    post_to_delete = Post.objects.get(id=post_id)
    post_to_delete.delete()
    return HttpResponse(f"Пост с ID {post_id} удалён.")

def filter_posts(request):
    posts_in_2024 = Post.objects.filter(published_date__year=2024)
    return HttpResponse(f"Посты за 2024 год: {', '.join([post.title for post in posts_in_2024])}")

