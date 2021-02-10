from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display        = ('id', 'name', 'phone', 'email', 'is_mvp')
    list_display_links  = ('id', 'name')
    list_per_page       = 25
    list_filter         = ('is_mvp',)
    search_fields       = ('id', 'name', 'phone', 'email')
    

# Register your models here.
admin.site.register(Realtor, RealtorAdmin)