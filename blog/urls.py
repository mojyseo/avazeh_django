from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.blog, name='blog'),
    path('<int:post_id>/', blog_views.post , name='post'),
]