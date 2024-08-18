from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .admin_views import AdminEventApprovalListView, AdminEventApprovalUpdateView
from .views import EventViewSet, create_event, event_edit, EventDetailView, UserEventListView, EventListView

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),  # Ensure this is correct
    path('create/', create_event, name='event_create'),
    path('edit/<int:pk>/', event_edit, name='event_edit'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('my-events/', UserEventListView.as_view(), name='user_event_list'),
    path('admin/events/', AdminEventApprovalListView.as_view(), name='admin_event_approval_list'),
    path('admin/events/<int:pk>/approve/', AdminEventApprovalUpdateView.as_view(), name='admin_event_approval_update'),
    # URL for user event list
]