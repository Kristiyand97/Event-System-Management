from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from rest_framework import viewsets

from .forms import EventForm, EventSearchForm
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user  # Set the organizer to the logged-in user
            event.save()
            return redirect('user_event_list')  # Redirect to the user's event list after creation
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user != event.organizer:
        return redirect(reverse('event_list'))  # Redirect if the user is not the organizer
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect(reverse('event_detail', kwargs={'pk': event.pk}))
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        # This will return all events
        return Event.objects.all()


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'


class UserEventListView(ListView):
    model = Event
    template_name = 'events/user_event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)



class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Event.objects.all()

        # Get the form values
        name = self.request.GET.get('name')
        venue = self.request.GET.get('venue')
        category = self.request.GET.get('category')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        # Filter by name
        if name:
            queryset = queryset.filter(name__icontains=name)

        # Filter by venue
        if venue:
            queryset = queryset.filter(venue__icontains=venue)

        # Filter by category
        if category:
            queryset = queryset.filter(category=category)

        # Filter by date range
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)

        # Filter by price range
        if min_price:
            queryset = queryset.filter(ticket_price__gte=min_price)
        if max_price:
            queryset = queryset.filter(ticket_price__lte=max_price)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EventSearchForm(self.request.GET or None)
        return context


class UserEventListView(ListView):
    model = Event
    template_name = 'events/user_event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Event.objects.filter(organizer=self.request.user)

        # Get the form values
        name = self.request.GET.get('name')
        venue = self.request.GET.get('venue')
        category = self.request.GET.get('category')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')

        # Filter by name
        if name:
            queryset = queryset.filter(name__icontains=name)

        # Filter by venue
        if venue:
            queryset = queryset.filter(venue__icontains=venue)

        # Filter by category
        if category:
            queryset = queryset.filter(category=category)

        # Filter by date range
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EventSearchForm(self.request.GET or None)
        return context