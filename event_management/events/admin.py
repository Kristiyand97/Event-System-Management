from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'venue', 'organizer')

admin.site.register(Event, EventAdmin)
