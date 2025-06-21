from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import PostForm
from .models import Post

def home(request):
    return HttpResponse("Привет, это мой блог!")

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})
