from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('patriarch/', views.patriarch, name='patriarch'),
    path('archibishop/', views.archbishop, name='archbishop'),
    path('articles/', views.articles, name='articles')
]
