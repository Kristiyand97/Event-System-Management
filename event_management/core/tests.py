from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from events.models import Event

class CoreViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create some test events
        Event.objects.create(name='Event 1', description='Description 1', date='2024-08-20', time='10:00:00', venue='Venue 1', category='Conference', ticket_price=100.00, organizer=self.user)
        Event.objects.create(name='Event 2', description='Description 2', date='2024-08-21', time='11:00:00', venue='Venue 2', category='Seminar', ticket_price=150.00, organizer=self.user)
        Event.objects.create(name='Event 3', description='Description 3', date='2024-08-22', time='12:00:00', venue='Venue 3', category='Workshop', ticket_price=200.00, organizer=self.user)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')
        self.assertEqual(len(response.context['events']), 3)  # We expect 3 events

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')

    def test_services_view(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/services.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact.html')

    def test_profile_view_without_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login page
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('profile')}")

    def test_profile_view_with_login(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/profile.html')
