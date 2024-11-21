from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from decouple import config
from datetime import datetime

from django.shortcuts import render, redirect
from django.shortcuts import redirect, get_object_or_404
from .models import Event
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse


def home(request):
    return render(request, 'index.html')



@login_required
def add_event(request):
    if request.method == "POST":
        # Extract form data
        event_name = request.POST.get('event_name')
        event_date = request.POST.get('event_date')
        event_location = request.POST.get('event_location')
        event_capacity = request.POST.get('event_capacity')
        price = request.POST.get('price')

        # Validate inputs
        if not all([event_name, event_date, event_location, event_capacity, price]):
            messages.error(request, "All fields are required.")
            return render(request, 'add_event.html')

        try:
            event_capacity = int(event_capacity)
            price = int(price)
        except ValueError:
            messages.error(request, "Capacity must be a number, and price must be a valid amount.")
            return render(request, 'add_event.html')

        #event yenye inaenda kwa database database
        event = Event(
            name=event_name,
            date=event_date,
            location=event_location,
            capacity=event_capacity,
            price=price
        )
        event.save()

        # Success message
        context = {
            "success": "Event added successfully!",
        }
        return render(request, 'add_event.html', context)

    # Render the form for GET requests
    return render(request, 'add_event.html')



@login_required
def events(request):
    all_events = Event.objects.all()
    context = {"all_events": all_events}
    return render(request, 'events.html', context)



@login_required
def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    messages.success(request, 'Event deleted successfully')
    return redirect('all-events')


@login_required
def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    context = {"event": event}
    if request.method == "POST":
        # Get updated values from the form
        updated_name = request.POST.get('e-name')
        updated_date = request.POST.get('e-date')
        updated_location = request.POST.get('e-location')
        updated_capacity = request.POST.get('e-capacity')
        updated_price = request.POST.get('e-price')
        event.name = updated_name
        event.date = updated_date
        event.location = updated_location
        event.capacity = updated_capacity
        event.price = updated_price
        event.save()
        messages.success(request, 'Event updated successfully')
        return redirect('all-events')

    return render(request, 'update_event.html', context)


def register_event(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event registered successfully')
            return redirect('all-events')

    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def events_today(request):
    # Get today's date
    today = timezone.now().date()
    events_happening = Event.objects.filter(start_time__date=today)
    return render(request, 'events_today.html', {'events_today': events_happening})