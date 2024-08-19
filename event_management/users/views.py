import logging

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import viewsets
from tickets.models import Ticket
from events.forms import EventForm
from events.models import Event
from tickets.models import Ticket
from .forms import CustomUserCreationForm, UserProfileForm
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


logger = logging.getLogger(__name__)



@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
        event_form = EventForm()  # Pass this to the template

    # Fetch user's events and purchased tickets
    my_events = Event.objects.filter(organizer=request.user)
    purchased_tickets = Ticket.objects.filter(user=request.user)

    return render(request, 'users/profile.html', {
        'form': form,
        'event_form': event_form,  # Pass the event form
        'username': request.user.username,
        'email': request.user.email,
        'phone_number': request.user.phone_number,
        'my_events': my_events,
        'purchased_tickets': purchased_tickets
    })


class CustomPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset_form.html'
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'account/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'domain_override': get_current_site(self.request).domain,
            'extra_email_context': {
                'protocol': self.request.scheme,
            },
        }
        form.save(**opts)
        return super().form_valid(form)


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'
