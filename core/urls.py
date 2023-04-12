from django.urls import path
from . import views
from .views import departmentview, departmentdetail, staffdetail


app_name = 'core'
urlpatterns = [
    path('department', departmentview.as_view(), name='departmentview'),
    path('<int:pk>', departmentdetail.as_view(), name='departmentdetail'),
    path('<int:pk>/', staffdetail.as_view(), name='staffdetail'),
   
  
]