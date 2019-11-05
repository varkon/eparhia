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
    list_display = ['title', 'get_deanery']
    inlines = [PhoneInline]
    def get_deanery(self, obj):
        return obj.Deanery.title

    get_deanery.admin_order_field = 'title'  # Allows column order sorting
    get_deanery.short_description = 'Благочиння'  # Renames column head

class DeaneryAdmin(admin.ModelAdmin):
    inlines = [ContactsInLine]

admin.site.register(Tample, TampleAdmin)
admin.site.register(Deanery, DeaneryAdmin)

