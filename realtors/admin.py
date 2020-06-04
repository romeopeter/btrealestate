from django.contrib import admin
from .models import Realtor

class realtorAdmin(admin.ModelAdmin):
  list_display = ('name', 'photo', 'email', 'phone', 'hire_date')
  list_display_links = ('name',)
  search_fields = ('name',)
  list_per_page = 25

# Register your models here.
admin.site.register(Realtor, realtorAdmin)

