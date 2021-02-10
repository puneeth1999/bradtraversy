from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','is_published', 'city', 'price', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('id', 'title', 'city', 'price', 'is_published')
    list_per_page = 25

# Register your models here.
admin.site.register(Listing, ListingAdmin)