from django.shortcuts import render
from django.utils import timezone
from news.models import News

# Create your views here.


def index(request) :
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:10]
    return render(request, 'index.html', {'news': news})

def about(request):
    return render(request,'about.html')
