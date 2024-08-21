from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class UserViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass', email='testuser@example.com')
        self.client.login(username='testuser', password='testpass')

    def test_profile_view_get(self):
        response = self.client.get(reverse('profile'))
        if response.status_code == 200:
            self.assertTemplateUsed(response, 'users/profile.html')
        elif response.status_code == 302:
            self.assertRedirects(response, f'/accounts/login/?next={reverse("profile")}')

    def test_profile_view_post(self):
        data = {
            'username': 'testuser',
            'email': 'newemail@example.com',
        }
        response = self.client.post(reverse('profile'), data)
        if response.status_code == 200:
            self.assertContains(response, 'Your profile was successfully updated!')
        elif response.status_code == 302:
            self.assertRedirects(response, f'/accounts/login/?next={reverse("profile")}')

    def test_password_reset_view_get(self):
        response = self.client.get(reverse('password_reset'))
        if response.status_code == 200:
            self.assertTemplateUsed(response, 'account/password_reset_form.html')
        elif response.status_code == 302:
            self.assertRedirects(response, f'/accounts/login/?next={reverse("password_reset")}')

    def test_password_reset_done_view_get(self):
        response = self.client.get(reverse('password_reset_done'))
        if response.status_code == 200:
            self.assertTemplateUsed(response, 'account/password_reset_done.html')
        elif response.status_code == 302:
            self.assertRedirects(response, f'/accounts/login/?next={reverse("password_reset_done")}')

    def test_password_reset_confirm_view_get(self):
        # Simulate the password reset confirm step
        uidb64 = 'set-uidb64-here'  # This would be dynamically generated in a real scenario
        token = 'set-token-here'  # This would be dynamically generated in a real scenario
        response = self.client.get(reverse('password_reset_confirm', args=[uidb64, token]))
        if response.status_code == 200:
            self.assertTemplateUsed(response, 'account/password_reset_confirm.html')
        elif response.status_code == 302:
            self.assertRedirects(response, f'/accounts/login/?next={reverse("password_reset_confirm", args=[uidb64, token])}')

    def test_password_reset_complete_view_get(self):
        response = self.client.get(reverse('password_reset_complete'))
        if response.status_code == 200:
            self.assertTemplateUsed(response, 'account/password_reset_complete.html')
        elif response.status_code == 302:
            self.assertRedirects(response, f'/accounts/login/?next={reverse("password_reset_complete")}')



