from io import BytesIO
import qrcode
from django.conf import settings
from django.core.files import File
from django.db import models
from events.models import Event

class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    stripe_payment_intent_id = models.CharField(max_length=255)  # Store the PaymentIntent ID
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.event.name} - {self.quantity} tickets'

    def save(self, *args, **kwargs):

        # Save the ticket first to get the ID
        if not self.id:
            super().save(*args, **kwargs)

        if not self.qr_code:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr_data = f"Ticket for {self.event.name}\nUser: {self.user.username}\nDate: {self.event.date}\nVenue: {self.event.venue}"
            qr.add_data(qr_data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Save to a file-like object
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            filename = f'ticket_qr_{self.id}.png'
            self.qr_code.save(filename, File(buffer), save=False)

        super().save(*args, **kwargs)
