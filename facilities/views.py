
from django.views.generic import ListView, DetailView
from .models import Facility
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import BookingForm
from .models import Booking


class FacilityListView(ListView):
    model = Facility
    template_name = 'facilities/facility_list.html'

class FacilityDetailView(DetailView):
    model = Facility
    template_name = 'facilities/facility_detail.html'
    context_object_name = 'facility'


def book_facility(request, facility_id):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.facility_id = facility_id

            # Check if the facility is available for the specified time and date
            bookings = Booking.objects.filter(facility_id=booking.facility_id, date=booking.date)
            for booked in bookings:
                if (booked.start_time <= booking.start_time <= booked.end_time or
                    booked.start_time <= booking.end_time <= booked.end_time or
                    booking.start_time <= booked.start_time and booking.end_time >= booked.end_time):
                    facility_name = booked.facility.name
                    form.add_error('start_time', f'The {facility_name} is already booked for this time.')
                    return render(request, 'facilities/booking.html', {'form': form})
            
            # Check if the start time is not in the past
            if booking.start_time < timezone.now().time():
                form.add_error('start_time', 'The start time cannot be in the past.')
                return render(request, 'facilities/booking.html', {'form': form})

            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'facilities/booking.html', {'form': form})
