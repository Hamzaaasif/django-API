from django.contrib import admin
from .models import cars
 
class carsadmin(admin.ModelAdmin):
  list_display=('model','brand','year','price')
  search_fields=['model']

admin.site.register(cars,carsadmin)

