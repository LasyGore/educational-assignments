from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.objects.all().order_by('-created_at')  # Получаем все посты
    per_page = request.GET.get('per_page', 5)

    paginator = Paginator(post_list, per_page)  # Показываем 5 постов на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    print("Rendering template")
    return render(request, 'tsk5/post_list.html', {'page_obj': page_obj,'per_page': per_page})