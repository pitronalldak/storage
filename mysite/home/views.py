from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
# Create your views here.

def index(request):
    latest_posts_list = Post.objects.order_by('-published_date')[:5]
    context = {'latest_posts_list': latest_posts_list}
    return render(request, 'home/home.html', context)

        