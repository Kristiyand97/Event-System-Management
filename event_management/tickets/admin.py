from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'quantity', 'purchase_date', 'qr_code')
    search_fields = ('user__username', 'event__name')
    list_filter = ('event', 'purchase_date')
