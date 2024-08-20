from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from events.models import Event
from events.admin import EventAdmin

User = get_user_model()

class MockRequest:
    def __init__(self, user):
        self.user = user

class EventAdminTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_superuser('admin', 'admin@example.com', 'password')

        # Create a test request
        self.factory = RequestFactory()
        self.request = self.factory.get('/admin/events/event/')
        self.request.user = self.user

        # Create some test events
        self.event1 = Event.objects.create(
            name='Event 1',
            description='Description 1',
            date='2024-08-20',
            time='10:00:00',
            venue='Venue 1',
            category='Conference',
            ticket_price=100.00,
            organizer=self.user,
            status='Pending',
            checked=False
        )
        self.event2 = Event.objects.create(
            name='Event 2',
            description='Description 2',
            date='2024-08-21',
            time='11:00:00',
            venue='Venue 2',
            category='Seminar',
            ticket_price=150.00,
            organizer=self.user,
            status='Pending',
            checked=False
        )

        self.event_admin = EventAdmin(Event, AdminSite())

    def test_mark_checked_action(self):
        queryset = Event.objects.filter(id__in=[self.event1.id, self.event2.id])
        self.event_admin.mark_checked(self.request, queryset)

        self.event1.refresh_from_db()
        self.event2.refresh_from_db()

        self.assertTrue(self.event1.checked)
        self.assertTrue(self.event2.checked)

    def test_list_display(self):
        # Ensure the list_display property is set correctly
        self.assertEqual(self.event_admin.list_display, ('name', 'date', 'venue', 'organizer', 'status', 'checked'))

    def test_list_filter(self):
        # Ensure the list_filter property is set correctly
        self.assertEqual(self.event_admin.list_filter, ('date', 'category', 'status'))

    def test_search_fields(self):
        # Ensure the search_fields property is set correctly
        self.assertEqual(self.event_admin.search_fields, ('name', 'description', 'venue'))
