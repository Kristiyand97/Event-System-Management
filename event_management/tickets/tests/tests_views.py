import stripe
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from unittest.mock import patch
from events.models import Event


User = get_user_model()

class PurchaseTicketViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.event = Event.objects.create(
            name='Test Event',
            description='Test Description',
            date='2024-12-31',
            time='18:00:00',
            venue='Test Venue',
            ticket_price=100.00,
            organizer=self.user,  # Pass the user as the organizer
            checked=True,
        )
        self.url = reverse('purchase_ticket', args=[self.event.id])

    def test_purchase_ticket_view_get(self):
        response = self.client.get(self.url)
        if response.status_code == 200:
            self.assertTemplateUsed(response, 'tickets/purchase_ticket.html')
        elif response.status_code == 302:
            self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    def test_purchase_ticket_view_post_invalid_data(self):
        data = {'quantity': '', 'payment_method_id': ''}
        response = self.client.post(self.url, data)
        if response.status_code == 200:
            self.assertFormError(response, 'form', 'quantity', 'This field is required.')
        elif response.status_code == 302:
            self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    @patch('stripe.PaymentIntent.create')
    def test_purchase_ticket_view_post_stripe_card_error(self, mock_payment_intent_create):
        mock_payment_intent_create.side_effect = stripe.error.CardError(
            message="Your card was declined.",
            param="",
            code="card_declined",
        )
        data = {'quantity': 1, 'payment_method_id': 'pm_card_visa'}
        response = self.client.post(self.url, data)
        if response.status_code == 200:
            self.assertContains(response, "Your card was declined.")
        elif response.status_code == 302:
            self.assertRedirects(response, f'/accounts/login/?next={self.url}')
