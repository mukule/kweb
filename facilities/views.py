
from django.views.generic import ListView, DetailView
from .models import Facility
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import BookingForm
from .models import Booking
from django.shortcuts import get_object_or_404
from django.contrib import messages



class FacilityListView(ListView):
    model = Facility
    template_name = 'facilities/facility_list.html'

class FacilityDetailView(DetailView):
    model = Facility
    template_name = 'facilities/facility_detail.html'
    context_object_name = 'facility'


def book_facility(request, facility_id):
    facility = get_object_or_404(Facility, pk=facility_id)
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
                    facility_name = booked.facility.name
                    messages.error(request, f'The {facility_name} is already booked for this time.')
                    return render(request, 'facilities/booking.html', {'form': form, 'facility': booked.facility})
            
            # Check if the start time is not in the past
            if booking.date < timezone.now().date():
                form.add_error('date', 'The booking date cannot be in the past.')
                return render(request, 'facilities/booking.html', {'form': form})
            if booking.date == timezone.now().date() and booking.start_time < timezone.now().time():
                form.add_error('start_time', 'The start time cannot be in the past.')
                return render(request, 'facilities/booking.html', {'form': form})

            booking.save()
            request.session['booking_id'] = booking.id
            return redirect('facilities:booking_success')
    else:
        form = BookingForm()
        now = timezone.now()
        bookings = Booking.objects.filter(facility_id=facility_id, date__gte=now.date()).order_by('date', 'start_time')


    if bookings.exists():
        context = {'form': form, 'facility': facility, 'bookings': bookings}
        return render(request, 'facilities/booking.html', context)
    else:
        context = {'form': form, 'facility': facility}
        return render(request, 'facilities/booking.html', context)
    
    
def booking_success(request):
    booking_id = request.session.get('booking_id')
    if booking_id:
        booking = Booking.objects.get(id=booking_id)
        context = {'booking': booking}
        return render(request, 'facilities/booking_success.html', context)
    else:
        return redirect('facilities:book_facility', facility_id=booking.facility_id)
