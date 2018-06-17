from django.shortcuts import render
from .models import Deanery,Tample

# Create your views here.

def deanery_list(request):
    deanery = Deanery.objects.all()
    if deanery.count() == 0 :
        return tamples_list(request,1)
   # contacts = deanery.deanerycontacts_set.all()
    return render(request, 'tamples/index.html',{'deanery':deanery})

def tamples_list(request, id):
    tamples = Tample.objects.filter(city_id = id).order_by("created_date")
    return render(request, 'tamples/index_tample.html', {'tamples':tamples})

def detail_tample(request, path):
    post = Tample.objects.get(link = path)
    phones = post.tamplephone_set.all()
    return render(request, 'tamples/view.html', {'post': post, 'phones':phones})