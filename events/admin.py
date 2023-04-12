from django.contrib import admin
from .models import Event

def approve_events(modeladmin, request, queryset):
    queryset.update(is_approved=True)

approve_events.short_description = "Approve selected events"

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'location', 'is_approved')
    actions = [approve_events]

admin.site.register(Event, EventAdmin)
