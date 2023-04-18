from django.contrib import admin
from .models import Poll, Choice
 
 
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
 
 
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date', 'end_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
 
 
admin.site.register(Poll, PollAdmin)
