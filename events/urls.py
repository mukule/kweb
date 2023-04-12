from django.urls import path
from . import views
from .views import events_list, events_detail


app_name = 'events'
urlpatterns = [
    path('events_list', events_list.as_view(), name='events_list'),
    path('<int:pk>/', events_detail.as_view(), name='event_detail'),
    path('create_event/', views.create_event, name='create_event'),
    
   
  
]