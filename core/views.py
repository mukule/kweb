from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Department, Staff
from django.contrib.auth.decorators import login_required

# Create your views here.



class departmentview(ListView):
    model = Department
    template_name = 'core/department_list.html'
    context_object_name = 'departments'


class departmentdetail(DetailView):
    model = Department
    template_name = 'core/department_detail.html'
    context_object_name ='departments'

    def get(self, request, *args, **kwargs):
        department = self.get_object()
        staff = department.staff.all()
        for staff_member in staff:
            print(staff_member.user.username)
        return super().get(request, *args, **kwargs)
    
class staffdetail(DetailView):
    model = Staff
    template_name = 'core/staffs.html'
    context_object_name = 'staffs'