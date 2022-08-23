from django.contrib import admin
from main.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'comment')

admin.site.register(Contact, ContactAdmin)
