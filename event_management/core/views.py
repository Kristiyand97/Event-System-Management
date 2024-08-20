from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from events.models import Event


def home(request):
    # Fetch the 3 most recently created events
    recent_events = Event.objects.order_by('-id')[:3]

    context = {
        'title': 'Upcoming Events',
        'events': recent_events  # Pass the actual events to the template
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    return render(request, 'core/contact.html')

@login_required
def profile(request):
    return render(request, 'core/profile.html')