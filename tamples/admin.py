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
    list_display = ['title', 'get_deanery']
    def get_deanery(self, obj):
        return obj.city.title
    get_deanery.admin_order_field = 'title'  # Allows column order sorting
    get_deanery.short_description = 'Благочиння'  # Renames column head

class DeaneryAdmin(admin.ModelAdmin):
    inlines = [ContactsInLine]

admin.site.register(Tample, TampleAdmin)
admin.site.register(Deanery, DeaneryAdmin)

