from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from eparhiapp.apps import transliterate

# Create your models here.
class Tample(models.Model):
    title = models.CharField(max_length = 255, verbose_name='Назва')
    saint = models.CharField(max_length = 255, verbose_name='На честь святого')
    address = models.CharField(max_length = 255, verbose_name='Адреса')
    city = models.CharField(max_length = 255, verbose_name='Місто')
    body = HTMLField(verbose_name='Опис')
    abbot = models.CharField(max_length = 255, verbose_name='Настоятель')
    link = models.CharField(max_length=255, verbose_name='Посилання', unique=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    icon = FileBrowseField("Зображення", max_length=250, directory="uploads/", extensions=[".jpg", "jpeg", "png"],
                           null=True)

    # this is not needed for create link
    def save(self, *args, **kwargs):
        self.createlink()
        super(Tample, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        if (self.link == ""):
            self.link = transliterate(self.title)
        self.save()

    def createlink(self):
        if (self.link == ""):
            self.link = transliterate(self.title)

    def __str__(self):
        return self.title


class TamplePhone(models.Model):
    tample = models.ForeignKey(Tample, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length = 20, verbose_name='Телефон')
    phonename = models.CharField(max_length = 50, null=True, verbose_name='Примитки')

    def __str__(self):
        return self.phonenumber
