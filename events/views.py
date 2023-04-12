from django.views.generic import ListView, DetailView
from .models import Event
from datetime import date
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.utils import timezone




# pip install -e git+https://github.com/rodrigoamaral/django-fullcalendar.git#egg=django-fullcalendar

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('events:event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})


class events_list(ListView):
    model = Event
    template_name = 'events/events_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        main_event = Event.objects.filter(is_main_event=True).first()

        # Filter the events queryset to exclude the main event, and order the remaining events by event date.
        events_queryset = Event.objects.filter(~Q(pk=main_event.pk)).order_by('event_date')

        # Split the events into today's events, upcoming events, and past events.
        today = date.today()
        today_events = []
        upcoming_events = []
        past_events = []
        for event in events_queryset:
            event_date = event.event_date.date()
            if event_date == today:
                today_events.append(event)
            elif event_date > today:
                upcoming_events.append(event)
            else:
                past_events.append(event)

        # Combine the main event and the ordered events into a list and return it.
        events_list = [main_event] if main_event else []
        events_list.extend(today_events)
        events_list.extend(upcoming_events)
        events_list.extend(past_events)

        return events_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_event'] = context['events'][0] if context['events'] else None
        context['today_events'] = [event for event in context['events'] if event.event_date.date() == date.today()]
        context['upcoming_events'] = [event for event in context['events'] if event.event_date.date() > date.today()]
        context['past_events'] = [event for event in context['events'] if event.event_date.date() < date.today()]
        return context
    
class events_detail(DetailView):
    model = Event
    template_name = 'events/event_detail.html'