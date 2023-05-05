from django.urls import path
from . views import update_task_status
from .views import TaskListView, TaskDetailView, accept_task, reject_task, task_report


app_name = 'tasks'
urlpatterns = [
    path('tasks', TaskListView.as_view(), name='dashboard_home'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/accept/', accept_task, name='accept_task'),
    path('task/<int:pk>/accept/task_report/', task_report, name='task_report'),
    path('task/<int:pk>/reject/', reject_task, name='reject_task'),
    path('<int:pk>/update_status/', update_task_status, name='task_status_update'),
    
   
  
]