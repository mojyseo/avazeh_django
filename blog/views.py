from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post 

# Create your views here.

def blog(req):
    posts = Post.objects.order_by('-date')
    return render(req, 'blog/blog.html' , {'posts': posts}
)
def blog_en(req):
    posts = Post.objects.order_by('-date')
    return render(req, 'blog/blog-en.html' , {'posts': posts}
)

def post(req, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(req, 'blog/post.html' , {'post': post}
)
