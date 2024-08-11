from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import TicketPurchaseForm
from .models import Ticket
from events.models import Event

@login_required
def purchase_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.event = event
            ticket.user = request.user
            ticket.save()
            messages.success(request, 'Ticket purchased successfully!')
            return redirect(reverse('event_detail', kwargs={'pk': event.id}))
    else:
        form = TicketPurchaseForm()

    return render(request, 'tickets/purchase_ticket.html', {'form': form, 'event': event})
