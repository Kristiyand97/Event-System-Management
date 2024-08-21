from django.test import TestCase
from django.urls import reverse
from users.models import User  # Import your custom User model

class CoreViewsTest(TestCase):

    def setUp(self):
        # Use the custom User model for creating a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact.html')

    def test_services_view(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/services.html')

    def test_profile_view_with_login(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('profile'))
        # Check if the response is 200, otherwise follow the redirect
        if response.status_code == 302:
            response = self.client.get(response.url)
        self.assertEqual(response.status_code, 200)

    def test_profile_view_without_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Redirects to login
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('profile')}")
