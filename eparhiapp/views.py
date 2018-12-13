from django.shortcuts import render
from django.utils import timezone
from news.models import News
from articles.models import Article
from eparhiapp.models import Patriarch, Archbishop, About

# Create your views here.


def index(request) :
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    return render(request, 'index.html', {'news': news, 'articles':articles})

def about(request):
    about_model = About.objects.all().order_by('-id').first()
    if not about_model :
        return render(request,'about.html', {'about_model': None})
    return render(request,'about.html', {'about_model':about_model})

def patriarch(request):
    about_model = Patriarch.objects.all().order_by('-id').first()
    if not about_model :
        return render(request,'patriarch.html', {'about_model': None})
    return render(request,'patriarch.html', {'about_model':about_model})

def archbishop(request):
    about_model = Archbishop.objects.all().order_by('-id').first()
    if not about_model :
        return render(request,'archbishop.html', {'about_model':None})
    return render(request,'archbishop.html', {'about_model':about_model})

# def articles(request) :
#     return render(request,'articles.html', {'about_model':None})

