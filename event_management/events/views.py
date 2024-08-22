from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils.functional import cached_property
from django.views.generic import ListView, DetailView
from rest_framework import viewsets

from users.decorators import email_verified_required
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
            event.organizer = request.user
            event.save()
            return redirect('user_event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user != event.organizer:
        return redirect(reverse('event_list'))
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
    paginate_by = 9

    def get_queryset(self):
        # Fetch only approved events
        queryset = Event.objects.filter(status='Approved').order_by('-date')


        name = self.request.GET.get('name')
        venue = self.request.GET.get('venue')
        category = self.request.GET.get('category')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if venue:
            queryset = queryset.filter(venue__icontains=venue)
        if category:
            queryset = queryset.filter(category=category)
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)
        if min_price:
            queryset = queryset.filter(ticket_price__gte=min_price)
        if max_price:
            queryset = queryset.filter(ticket_price__lte=max_price)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the search form to the context
        context['form'] = EventSearchForm(self.request.GET or None)
        # Only show filters if there is more than one page
        context['show_filters'] = self.get_queryset().count() > self.paginate_by
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'


class UserEventListView(ListView):
    model = Event
    template_name = 'events/user_event_list.html'
    context_object_name = 'events'
    paginate_by = 9

    def get_queryset(self):
        # Fetch only the events created by the current user
        queryset = Event.objects.filter(organizer=self.request.user, checked=True).order_by('-date')


        name = self.request.GET.get('name')
        venue = self.request.GET.get('venue')
        category = self.request.GET.get('category')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')


        if name:
            queryset = queryset.filter(name__icontains=name)


        if venue:
            queryset = queryset.filter(venue__icontains=venue)


        if category:
            queryset = queryset.filter(category=category)


        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)


        if min_price:
            queryset = queryset.filter(ticket_price__gte=min_price)
        if max_price:
            queryset = queryset.filter(ticket_price__lte=max_price)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the search form to the context
        context['form'] = EventSearchForm(self.request.GET or None)
        # Only show filters if there is more than one page
        context['show_filters'] = self.get_queryset().count() > self.paginate_by
        return context
