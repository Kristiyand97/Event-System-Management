from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Event(models.Model):
    CATEGORY_CHOICES = [
        ('CONFERENCE', 'Conference'),
        ('SEMINAR', 'Seminar'),
        ('MEETING', 'Meeting'),
        ('WORKSHOP', 'Workshop'),
        ('CONCERT', 'Concert'),
        ('FESTIVAL', 'Festival'),
        ('WEBINAR', 'Webinar'),
        ('NETWORKING', 'Networking Event'),
        ('EXHIBITION', 'Exhibition'),
        ('PARTY', 'Party'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='CONFERENCE')
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    is_approved = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.name
