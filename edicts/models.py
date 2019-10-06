from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from eparhiapp.apps import transliterate

class Edict(models.Model) :
    title = models.CharField(max_length = 255, verbose_name='Заголовок')
    annonce = HTMLField(verbose_name='Анонс указа')
    body = HTMLField(verbose_name='Повний текст указа')
    link = models.CharField(max_length = 255, verbose_name='Посилання', unique=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    icon = FileBrowseField("Зображення", max_length=250, directory="uploads/", extensions=[".jpg","jpeg","png"], null=True)

    class Meta:
        verbose_name = 'Указ'
        verbose_name_plural = 'Укази'

    # this is not needed for create link
    def save(self, *args, **kwargs):
        self.createlink()
        super(Edict, self).save(*args, **kwargs)

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