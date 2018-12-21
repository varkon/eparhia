from django.contrib import admin
from .models import Patriarch, Archbishop, Primat, About
# Register your models here.

admin.site.register(Patriarch)
admin.site.register(Archbishop)
admin.site.register(Primat)
admin.site.register(About)