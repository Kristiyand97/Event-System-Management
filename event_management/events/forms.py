from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'venue', 'category', 'ticket_price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'venue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Venue'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'ticket_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ticket Price'}),
        }

class EventSearchForm(forms.Form):
    name = forms.CharField(required=False, label='Event Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by name'}))
    venue = forms.CharField(required=False, label='Venue', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by venue'}))
    category = forms.ChoiceField(choices=[('', 'All Categories')] + Event.CATEGORY_CHOICES, required=False, label='Category', widget=forms.Select(attrs={'class': 'form-control'}))
    date_from = forms.DateField(required=False, label='Date From', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    date_to = forms.DateField(required=False, label='Date To', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    min_price = forms.DecimalField(required=False, label='Min Price', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Min Price'}))
    max_price = forms.DecimalField(required=False, label='Max Price', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max Price'}))