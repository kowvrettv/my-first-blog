from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

# Общее количество постов
@register.simple_tag
def total_posts():
    posts = Post.objects.filter(status='published')
    return posts.count()

# Самые комментриуемые посты
@register.simple_tag
def get_most_commented_posts(count=5):
    posts = Post.objects.filter(status='published')
    return posts.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

# Последние опубликованные посты
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.filter(status='published').order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

# Редактор для текста
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
