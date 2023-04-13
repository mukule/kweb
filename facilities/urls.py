from django.urls import path
from .views import FacilityListView, FacilityDetailView

app_name = 'facilities'

urlpatterns = [
    path('', FacilityListView.as_view(), name='facility_list'),
    path('<int:pk>/', FacilityDetailView.as_view(), name='facility_detail'),
    # path('<int:pk>/book/', BookingCreateView.as_view(), name='booking_create'),
]
