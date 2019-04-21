from django.contrib import admin
from django.urls import path,include
from myapi import views
#import cars.urls

urlpatterns = [
    path('admin/', admin.site.urls,name='index'),
    path('user/',views.createcars.as_view()),
]
