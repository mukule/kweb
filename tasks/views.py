from django.views.generic import ListView, DetailView, UpdateView
from .models import Task, Assignment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from notifications.models import Notification
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskUpdateForm, AssignmentAcceptForm, AssignmentRejectForm
from django.contrib.auth.decorators import login_required
from datetime import date
import os
from django.urls import reverse_lazy
from django.conf import settings
from django.templatetags.static import static
from django.http import HttpResponse
import requests
from django.views.generic import View
from django.contrib import messages






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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Check if the current user has an assignment for the task
        assignment = self.object.assignments.filter(assigned_to=self.request.user).first()

        if not assignment:
            # If the user doesn't have an assignment, add the accept/reject forms to the context
            context['accept_form'] = AssignmentAcceptForm()
            context['reject_form'] = AssignmentRejectForm()
        else:
            # If the user has an assignment, remove the accept/reject forms from the context
            context.pop('accept_form', None)
            context.pop('reject_form', None)

        # Calculate number of days before due date
        today = date.today()
        due_date = self.object.due_date
        days_before_due = (due_date - today).days

        # Check whether task is due today or has passed
        if due_date == today:
            context['due_message'] = "This task is due today!"
        elif due_date < today:
            context['due_message'] = "This task is past due!"
        else:
            context['due_message'] = f"This task is due in {days_before_due} days."

        # Check if the task has a document attached
        pdf_url = self.object.document.url if self.object.document else None
        if pdf_url and os.path.exists(pdf_url):
            # Add the PDF URL to the context
            context['pdf_url'] = pdf_url

        # Update the notification as read
        user = self.request.user
        task_id = self.kwargs['pk']
        try:
            notification = Notification.objects.get(user=user, task_id=task_id, read=False)
            notification.read = True
            notification.save()
        except Notification.DoesNotExist:
            pass

        return context



def accept_task(request, pk):
    task = Task.objects.get(pk=pk)
    assignment = task.assignments.filter(assigned_to=request.user).first()

    if assignment and assignment.accepted:
        # If the user has already accepted the assignment, redirect to task detail page
        messages.info(request, "You have already accepted this task!")
        return redirect('tasks:task_detail', pk=pk)
    elif assignment and assignment.rejection_reason:
        # If the user has already rejected the assignment, redirect to task detail page
        messages.info(request, "You have already rejected this task!")
        return redirect('tasks:task_detail', pk=pk)

    form = AssignmentAcceptForm(request.POST or None)
    if form.is_valid():
        additional_details = form.cleaned_data.get('additional_details')
        assignment.accepted = True
        assignment.additional_details = additional_details
        assignment.save()
        messages.success(request, "Task accepted successfully!")
        return redirect('tasks:task_report', pk=pk)

    context = {'form': form, 'task': task}
    return render(request, 'tasks/accept_task.html', context)

def reject_task(request, pk):
    task = Task.objects.get(pk=pk)
    assignment = task.assignments.filter(assigned_to=request.user).first()

    if assignment and assignment.rejection_reason:
        # If the user has already rejected the assignment, redirect to task detail page
        messages.info(request, "You have already rejected this task!")
        return redirect('tasks:task_detail', pk=pk)
    elif assignment and assignment.accepted:
        # If the user has already accepted the assignment, redirect to task detail page
        messages.info(request, "You have already accepted this task!")
        return redirect('tasks:task_detail', pk=pk)

    form = AssignmentRejectForm(request.POST or None)
    if form.is_valid():
        rejection_reason = form.cleaned_data.get('rejection_reason')
        assignment.rejected = True
        assignment.rejection_reason = rejection_reason
        assignment.save()
        messages.success(request, "Task rejected successfully!")
        return redirect('tasks:task_detail', pk=pk)

    context = {'form': form, 'task':task}
    return render(request, 'tasks/reject_task.html', context)

def task_report(request, pk):
    assignment = Assignment.objects.filter(task__pk=pk, assigned_to=request.user).first()
    if not assignment:
        messages.error(request, "You have not been assigned this task!")
        return redirect('tasks:task_detail', pk=pk)
    elif not assignment.accepted and not assignment.rejection_reason:
        messages.info(request, "You have not accepted or rejected this task yet!")
        return redirect('tasks:task_detail', pk=pk)
    elif assignment.rejection_reason:
        messages.error(request, "You rejected the assignment!")
        return redirect('tasks:task_detail', pk=pk)

    task = assignment.task
    today = date.today()

    if task.due_date < today:
        messages.error(request, "The due date for this task has passed!")
        return redirect('tasks:task_detail', pk=pk)

    milestones = task.milestones.all()

    return render(request, 'tasks/task_report.html', {'pk': pk, 'task': task, 'milestones': milestones})



@login_required
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)

    # Check if the user is assigned to the task
    try:
        assignment = Assignment.objects.get(task=task, assigned_to=request.user)
    except Assignment.DoesNotExist:
        return redirect('tasks:task_detail', pk=pk)

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            # Update the task status
            task = form.save()

            # Mark the task as completed if status is "Complete"
            if task.status == 'C':
                assignment.completed = True
                assignment.save()

            # Redirect to the task detail page
            return redirect('tasks:task_detail', pk=pk)
    else:
        form = TaskUpdateForm(instance=task)

    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'tasks/task_detail.html', context)
