# tickets/forms.py

from django import forms
from .models import Ticket

class TicketPurchaseForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['quantity']
        labels = {
            'quantity': 'Number of Tickets',
        }
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
        }
