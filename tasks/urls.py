from django.urls import path,include
from . views import update_task_status
from .views import TaskListView, TaskDetailView


app_name = 'tasks'
urlpatterns = [
    path('tasks', TaskListView.as_view(), name='dashboard_home'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update_status/', update_task_status, name='task_status_update'),
   
  
]