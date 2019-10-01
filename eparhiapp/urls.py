from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('patriarch/', views.patriarch, name='patriarch'),
    path('archbishop/', views.archbishop, name='archbishop'),
    path('primat/', views.primat, name='primat'),
    path('benefactors/',views.benefactors, name='benefactors')
]
