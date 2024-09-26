from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.objects.all().order_by('-created_at')  # �������� ��� �����
    paginator = Paginator(post_list, 5)  # ���������� 5 ������ �� ��������

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    print("Rendering template")
    return render(request, 'app/post_list.html', {'page_obj': page_obj})