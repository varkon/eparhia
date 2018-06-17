from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.deanery_list, name='deanery_list'),
    path('<int:id>/', views.tamples_list, name='tamples_list'),
    path('<slug:path>/', views.detail_tample, name='detail')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)