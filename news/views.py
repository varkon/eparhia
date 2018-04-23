from django.shortcuts import render
from django.utils import timezone
from .models import News

# Create your views here.


def news_list(request):
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'news/index.html', {'news':news})

def detail_news(request, path):
    post = News.objects.get(link = path)
    return render(request, 'news/view.html', {'post': post})