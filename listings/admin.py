from django.contrib import admin

from .models import Listing

class listingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor') # Displays additional data in listing admin
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_published',)
  search_fields = ('title', 'address', 'city', 'state', 'zipcode', 'description',)
  list_per_page = 25

# Register your models here.
admin.site.register(Listing, listingAdmin)