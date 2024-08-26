from django.urls import path
from .views import purchase_ticket, payment_history

urlpatterns = [
    path('purchase/<int:event_id>/', purchase_ticket, name='purchase_ticket'),
    path('payment/history/', payment_history, name='payment_history'),
]