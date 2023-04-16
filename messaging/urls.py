from django.urls import path
from . import views
from .views import *


app_name = 'messaging'
urlpatterns = [
    path('send_message', views.send_message, name='send_message'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('message/<int:message_id>/', MessageDetailView.as_view(), name='message_detail'),
    
]