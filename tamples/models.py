from django.db import models
import datetime
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from eparhiapp.apps import transliterate

# Create your models here.
class Deanery(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Назва')
    abbot = models.CharField(max_length = 255, null= True, blank= True, verbose_name = 'Благочинний')
    description = HTMLField(null = True, blank = True, verbose_name = 'Детальний опис')
    link = models.CharField(max_length=255, verbose_name='Посилання', unique=True, blank=True)

    class Meta:
        verbose_name = 'Благочиня'
        verbose_name_plural = 'Благочиння'

    def save(self, *args, **kwargs):
        self.createlink()
        super(Deanery, self).save(*args, **kwargs)

    def createlink(self):
        if (self.link == ""):
            self.link = transliterate(self.title)

    def __str__(self):
        return self.title

class DeaneryContacts(models.Model):
    deanery = models.ForeignKey(Deanery, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20, verbose_name='Телефон або инший контакт')
    description = models.CharField(max_length=50, null=True, verbose_name='Примитки')



    def __str__(self):
        return self.phonenumber


class Tample(models.Model):
    title = models.CharField(max_length = 255, verbose_name='Назва')
    address = models.CharField(max_length = 255, verbose_name='Адреса')
    city = models.ForeignKey(Deanery, on_delete = models.CASCADE, verbose_name = 'Благочиння')
    body = HTMLField(verbose_name='Опис')
    abbot = models.CharField(max_length = 255, verbose_name='Настоятель')
    link = models.CharField(max_length=255, verbose_name='Посилання', unique=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateField(
        default=datetime.date.today, null = True)
    published_date = models.DateField(
        blank=True, null=True)
    icon = FileBrowseField("Зображення", max_length=250, directory="uploads/", extensions=[".jpg", "jpeg", "png"],
                           null=True)

    class Meta:
        verbose_name = 'Храм'
        verbose_name_plural = 'Храми'

    # this is not needed for create link
    def save(self, *args, **kwargs):
        self.createlink()
        super(Tample, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = datetime.now()
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
