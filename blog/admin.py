from django.contrib import admin
from .models import Post, Category

admin.site.site_header = "Панель управления блогом"
admin.site.site_title = "Блог администратора"
admin.site.index_title = "Добро пожаловать в админку"
admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'text')
    date_hierarchy = ('created_at')
    ordering = ('created_at',)
