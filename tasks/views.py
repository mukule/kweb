from django.views.generic import ListView, DetailView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.models import Notification
from django.shortcuts import render



class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/dashboard_home.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get tasks assigned to the logged-in user
        user = self.request.user
        assigned_tasks = Task.objects.filter(assignments__assigned_to=user)

        # Get unread notifications for the current user
        notifications = Notification.objects.filter(user=user, read=False)

        context['assigned_tasks'] = assigned_tasks
        context['notifications'] = notifications
        return context
    
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        # Mark associated notification as read
        user = request.user
        task = self.get_object()
        notification = Notification.objects.filter(user=user, task=task).first()
        if notification:
            notification.read = True
            notification.save()

            # Dismiss associated notification
            notification.delete()

        return response

