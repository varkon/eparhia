from django.shortcuts import render
from django.utils import timezone
from .models import Article

# Create your views here.


def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'articles/index.html', {'articles':articles})

def detail_article(request, path):
    post = Article.objects.get(link = path)
    return render(request, 'articles/view.html', {'post': post})