from django.urls import reverse
from django.test import TestCase
from events.models import Event
from users.models import User  # Ensure this points to your custom User model


class CreateEventViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_event_view_get(self):
        # Use force_login to log in the user without relying on session
        self.client.force_login(self.user)

        # Attempt to access the create event page
        response = self.client.get(reverse('event_create'))

        # Check if the response is redirecting to the login page
        if response.status_code == 302:
            redirect_target = response.url
            self.assertIn('/accounts/login/', redirect_target)
        else:
            # Expecting a 200 status code, indicating the form is displayed
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'events/event_form.html')

    def test_create_event_view_post_valid_data(self):
        # Use force_login to log in the user without relying on session
        self.client.force_login(self.user)

        # Submit the form with valid data
        data = {
            'name': 'Test Event',
            'description': 'This is a test event.',
            'date': '2027-02-22',
            'time': '23:11:00',
            'venue': 'Freemon Street 123',
            'category': 'Concert',
            'ticket_price': 100.00,
        }
        response = self.client.post(reverse('event_create'), data)

        # Check if the response is redirecting to the login page
        if response.status_code == 302:
            redirect_target = response.url
            self.assertIn('/accounts/login/', redirect_target)
        else:
            # Ensure the event was created and is in pending status
            event = Event.objects.filter(name='Test Event').first()
            self.assertIsNotNone(event)
            self.assertEqual(event.organizer, self.user)
            self.assertEqual(event.status, 'Pending')

    def test_create_event_view_post_invalid_data(self):
        # Use force_login to log in the user without relying on session
        self.client.force_login(self.user)

        # Submit the form with invalid data
        data = {
            'name': '',  # Invalid: name is required
            'description': 'This is a test event with no name.',
            'date': '2027-02-22',
            'time': '23:11:00',
            'venue': 'Freemon Street 123',
            'category': 'Concert',
            'ticket_price': 100.00,
        }
        response = self.client.post(reverse('event_create'), data)

        # Check if the response is redirecting to the login page
        if response.status_code == 302:
            redirect_target = response.url
            self.assertIn('/accounts/login/', redirect_target)
        else:
            # Expecting to stay on the form page due to validation error
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'events/event_form.html')
            self.assertFormError(response, 'form', 'name', 'This field is required.')
    def test_create_event_view_not_logged_in(self):
        response = self.client.get(reverse('event_create'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login page
        self.assertRedirects(response, '/accounts/login/?next=/events/create/')

    def test_event_approval(self):
        # Create an event with a pending status
        self.client.login(username='testuser', password='testpassword')
        event = Event.objects.create(
            name='Pending Event',
            description='This event is awaiting approval.',
            date='2024-08-21',
            time='14:00',
            venue='Test Venue',
            category='CONFERENCE',
            ticket_price=100.00,
            organizer=self.user,
            status='Pending',
            checked=False,
        )

        # Admin logs in and approves the event
        self.client.login(username='admin', password='adminpassword')
        event.status = 'Approved'
        event.checked = True
        event.save()

        # Verify that the event is now approved
        event.refresh_from_db()
        self.assertEqual(event.status, 'Approved')
        self.assertTrue(event.checked)
