from django.urls import path
from .views import FacilityListView, FacilityDetailView
from .views import book_facility, booking_success

app_name = 'facilities'

urlpatterns = [
    path('', FacilityListView.as_view(), name='facility_list'),
    path('<int:pk>/', FacilityDetailView.as_view(), name='facility_detail'),
    # path('book_facility/', book_facility, name='book_facility'),
    path('<int:facility_id>/book_facility/', book_facility, name='book_facility'),
    path('booking_success/', booking_success, name='booking_success'),
    
]
