from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from events.models import Event


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class AdminEventApprovalListView(ListView):
    model = Event
    template_name = 'events/admin_event_approval_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(is_approved=False)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class AdminEventApprovalUpdateView(UpdateView):
    model = Event
    fields = ['is_approved', 'status']
    template_name = 'events/admin_event_approval_update.html'
    success_url = reverse_lazy('admin_event_approval_list')

    def form_valid(self, form):
        event = form.save(commit=False)
        if event.is_approved:
            event.status = 'Approved'
        else:
            event.status = 'Rejected'
        event.save()
        return redirect(self.success_url)
