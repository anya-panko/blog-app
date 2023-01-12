from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms import ModelForm
from .models import Post

posts = [
    {
        'author': 'Администратор',
        'title': 'Это первый пост',
        'content': 'Подробное содержание первого поста.',
        'date_posted': '12 мая, 2022'
    },
    {
        'author': 'Пользователь',
        'title': 'Это второй пост',
        'content': 'Подробное содержание второго поста',
        'date_posted': '13 мая, 2022'

    }
]


def home(request):
    user_id = request.GET.get("user_id")
    posts = Post.objects.all()

    if user_id is not None:
        posts = posts.filter(author_id=user_id)

    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "content")


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.data['title']
            messages.success(request, f'Создан пост {title}!')
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/new.html', {'form': form})

