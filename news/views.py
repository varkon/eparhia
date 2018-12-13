from django.shortcuts import render
from django.utils import timezone
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def news_list(request):
    news_lists = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(news_lists, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, 'news/index.html', {'news':news})

def detail_news(request, path):
    post = News.objects.get(link = path)
    return render(request, 'news/view.html', {'post': post})