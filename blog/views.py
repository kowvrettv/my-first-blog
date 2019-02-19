from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Comment
from .forms import CommentForm

def homepage(request):
    return render(request, 'base.html', {})

class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    # Список активных комментариев для поста
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # Комментарий был опубликован
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создание объекта комментария без сохранения в базу
            new_comment = comment_form.save(commit=False)
            # Назначить текущее сообщение для комментария
            new_comment.post = post
            # Сохранение комментария в базу
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    return render(request, 'blog/post/detail.html', {'post': post,
                                                    'comments': comments,
                                                    'new_comment': new_comment,
                                                    'comment_form': comment_form})

def search(request):
    if request.method == 'GET':
        search_prompt = request.GET.get('search')
        # Поиск по словам/фразам в заголовке или тексте поста
        search_result = Post.objects.filter(body__icontains=search_prompt) or Post.objects.filter(title__icontains=search_prompt) 
        return render(request, 'blog/search.html', {'search_result': search_result})
    else:
        return render(request, 'blog/search.html', {})