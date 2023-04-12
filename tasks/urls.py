from django.urls import path,include
from . import views
from .views import TaskListView, TaskDetailView


app_name = 'tasks'
urlpatterns = [
    path('tasks', TaskListView.as_view(), name='dashboard_home'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
   
  
]