from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration


# Home Page - Display All Events
def index(request):
    events = Event.objects.all()
    return render(request, "index.html", {"events": events})


# Event Details
def details(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, "details.html", {"event": event})


# Register for Event
def register(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        Registration.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            event=event
        )
        return redirect("registrations")

    return render(request, "details.html", {"event": event})


# View Registrations
def registrations(request):
    data = Registration.objects.select_related("event").all()
    return render(request, "registrations.html", {"registrations": data})


# Cancel Registration
def cancel(request, id):
    registration = get_object_or_404(Registration, id=id)
    registration.delete()
    return redirect("registrations")