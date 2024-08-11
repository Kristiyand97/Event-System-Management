from django.urls import path
from .views import purchase_ticket

urlpatterns = [
    path('purchase/<int:event_id>/', purchase_ticket, name='purchase_ticket'),
]
