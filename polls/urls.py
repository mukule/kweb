from django.urls import path
from . import views
from .views import *


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:pk>/', PollDetailView.as_view(), name='poll_detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
   
    
]