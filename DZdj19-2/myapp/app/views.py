from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Item


def item_list(request):
    item_list = Item.objects.all()
    items_per_page = int(request.GET.get('items_per_page', 5))

#    paginator = Paginator(item_list, items_per_page)
    paginator = Paginator(item_list, items_per_page)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/item_list.html', {'page_obj': page_obj, 'items_per_page': items_per_page})