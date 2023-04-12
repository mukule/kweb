from django.contrib import admin
from .models import CompanyDocument, StaffDocument, Category, Tag

# Register your models here.

admin.site.register(CompanyDocument)
admin.site.register(StaffDocument)
admin.site.register(Category)
admin.site.register(Tag)

