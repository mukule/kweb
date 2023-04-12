from django.contrib import admin
from .models import News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    fields = [
        'image',
        'title',
        'author',
        'content',
        
       
    ]




admin.site.register(News, NewsAdmin)
