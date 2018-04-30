from django.shortcuts import render
from .models import Tample

# Create your views here.


def tamples_list(request):
    tamples = Tample.objects.all().order_by("title")
    return render(request, 'tamples/index.html', {'tamples':tamples})

def detail_tample(request, path):
    post = Tample.objects.get(link = path)
    phones = post.tamplephone_set.all()
    return render(request, 'tamples/view.html', {'post': post, 'phones':phones})