from django.shortcuts import render
from django.utils import timezone
from news.models import News
from edicts.models import Edict
from articles.models import Article
from eparhiapp.models import Patriarch, Archbishop, Primat, About, Benefactor
from .apps import getPatriarhiaNew
# Create your views here.


def index(request) :
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:12]
    edicts = Edict.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:11]
    articles = {} #Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
    patriarhia = getPatriarhiaNew()
    return render(request, 'index.html', {'news': news, 'articles':articles, 'patriarhia':patriarhia, 'edicts': edicts})

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
    caption = "Архієрей"
    if not about_model :
        return render(request,'archbishop.html', {'about_model':None, 'caption':caption})
    return render(request,'archbishop.html', {'about_model':about_model, 'caption':caption})

def primat(request):
    about_model = Primat.objects.all().order_by('-id').first()
    caption = "Предстоятель"
    if not about_model:
        return render(request, 'archbishop.html', {'about_model': None, 'caption':caption})
    return render(request, 'archbishop.html', {'about_model': about_model, 'caption':caption})

def benefactors(request):
    benefactors_model = Benefactor.objects.all().order_by('-id').first()
    caption = "Благодійникам"
    if not benefactors_model :
        return render(request,'benefactors.html', {'about_model': None, 'caption':caption})
    return render(request,'benefactors.html', {'about_model':benefactors_model, 'caption':caption})

# def articles(request) :
#     return render(request,'articles.html', {'about_model':None})

