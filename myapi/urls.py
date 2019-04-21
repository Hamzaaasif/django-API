from django.urls import path
from .import views

app_name = 'cars'
urlpatterns = [
    path('destroy',views.destroycars.as_view(),name='car-add'),
    path('create',views.createcars.as_view()),
]