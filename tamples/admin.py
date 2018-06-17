from django.contrib import admin

# Register your models here.
from .models import Deanery, DeaneryContacts, Tample, TamplePhone

class PhoneInline(admin.TabularInline):
    model = TamplePhone
    extra = 1

class ContactsInLine(admin.TabularInline):
    model = DeaneryContacts
    extra = 1

class TampleAdmin(admin.ModelAdmin):
    inlines = [PhoneInline]

class DeaneryAdmin(admin.ModelAdmin):
    inlines = [ContactsInLine]

admin.site.register(Tample, TampleAdmin)
admin.site.register(Deanery, DeaneryAdmin)

