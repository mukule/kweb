from django.urls import path
from . import views


app_name = 'applications'
urlpatterns = [
    path('events_list', views.applications, name='applications_list'),
    
    
   
  
]