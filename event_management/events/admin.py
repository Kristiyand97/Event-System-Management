from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'venue', 'organizer', 'status', 'checked')
    list_filter = ('date', 'category', 'status')
    search_fields = ('name', 'description', 'venue')
    actions = ['mark_checked']

    def mark_checked(self, request, queryset):
        queryset.update(checked=True)
    mark_checked.short_description = "Mark selected events as checked"

admin.site.register(Event, EventAdmin)
