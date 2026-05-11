from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

from django.shortcuts import render, redirect
from .models import Event, Registration

def event_list(request):
    if request.method == "POST":
        name = request.POST.get("student_name")
        event_id = request.POST.get("event_id")

        event = Event.objects.get(id=event_id)

        Registration.objects.create(
            student_name=name,
            event=event
        )

        return redirect('event_list')

    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def registered_list(request):
    registrations = Registration.objects.all()
    return render(request, 'events/registered.html', {'registrations': registrations})
