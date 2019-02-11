from django.urls import path
from . import views
from .feeds import LatestPostFeed

app_name = 'blog'

urlpatterns = [
    # отображение постов
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', 
            views.post_detail, 
            name='post_detail'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('search/', views.search, name='search'),
]