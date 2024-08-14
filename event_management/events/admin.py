from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'venue', 'organizer')
    list_filter = ('date', 'category')
    search_fields = ('name', 'description', 'venue')

admin.site.register(Event, EventAdmin)
