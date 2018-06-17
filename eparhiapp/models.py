from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from eparhiapp.apps import transliterate

# Create your models here.

class Patriarch(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    annonce = HTMLField(verbose_name='Анонс (не обовьязково - зараз не використовується)', null = True, blank = True)
    body = HTMLField(verbose_name='Повний текст')
    link = models.CharField(max_length=255, verbose_name='Посилання', unique=True, blank=True, default="patriarch")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    class Meta:
        verbose_name = 'Патриарх'
        verbose_name_plural = 'Патриарх'

    # this is not needed for create link
    def save(self, *args, **kwargs):
        self.createlink()
        super(Patriarch, self).save(*args, **kwargs)

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

class Archbishop(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    annonce = HTMLField(verbose_name='Анонс (не обовьязково - зараз не використовується)', null = True, blank = True)
    body = HTMLField(verbose_name='Повний текст')
    link = models.CharField(max_length=255, verbose_name='Посилання', unique=True, blank=True, default = "archbishop")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    class Meta:
        verbose_name = 'Єпископ'
        verbose_name_plural = 'Єпископи'

    # this is not needed for create link
    def save(self, *args, **kwargs):
        self.createlink()
        super(Archbishop, self).save(*args, **kwargs)

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

class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    annonce = HTMLField(verbose_name='Анонс (не обовьязково - зараз не використовується)', null = True, blank = True)
    body = HTMLField(verbose_name='Повний текст')
    link = models.CharField(max_length=255, verbose_name='Посилання', unique=True, blank=True, default="about")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакти'

    # this is not needed for create link
    def save(self, *args, **kwargs):
        self.createlink()
        super(About, self).save(*args, **kwargs)

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