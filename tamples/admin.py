from django.contrib import admin

# Register your models here.
from .models import Tample, TamplePhone

class PhoneInline(admin.TabularInline):
    model = TamplePhone
    extra = 1

class TampleAdmin(admin.ModelAdmin):
    inlines = [PhoneInline]

admin.site.register(Tample, TampleAdmin)
