# tickets/models.py

from django.conf import settings
from django.db import models
from events.models import Event  # Assuming you have an Event model

class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    stripe_payment_intent_id = models.CharField(max_length=255)  # Store the PaymentIntent ID

    def __str__(self):
        return f'{self.user.username} - {self.event.name} - {self.quantity} tickets'
