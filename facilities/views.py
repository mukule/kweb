
from django.views.generic import ListView, DetailView
from .models import Facility

class FacilityListView(ListView):
    model = Facility
    template_name = 'facilities/facility_list.html'

class FacilityDetailView(DetailView):
    model = Facility
    template_name = 'facilities/facility_detail.html'
    context_object_name = 'facility'
