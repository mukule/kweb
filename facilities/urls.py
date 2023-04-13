from django.urls import path
from .views import FacilityListView, FacilityDetailView
from .views import book_facility

app_name = 'facilities'

urlpatterns = [
    path('', FacilityListView.as_view(), name='facility_list'),
    path('<int:pk>/', FacilityDetailView.as_view(), name='facility_detail'),
    # path('book_facility/', book_facility, name='book_facility'),
    path('<int:pk>/', book_facility, name='book_facility'),
    
]
