from django.contrib import admin
from .models import Item

#@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Измените на нужные вам поля


admin.site.register(Item, ItemAdmin)