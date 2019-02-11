from django.contrib import admin
from .models import Post, Comment

@admin.register(Post) # декоратор для класса ModelAdmin, заменяет admin.site.register()
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', # атрибуты для отображения постов
                    'publish', 'status')
    list_filter = ('status', 'created', 'publish', # атрибуты для фильтра (боковая панель)
                    'author')
    search_fields = ('title', 'body') # атрибуты поиска
    # prepopulated_fields = {'slug': ('title',)} # откуда slug берет данные для заполнения
    raw_id_fields = ('author',) # поиск пользователя по id
    date_hierarchy = 'publish'
    ordering = ('status', 'publish') # параметры сортировки панели фильтров

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 
                    'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')