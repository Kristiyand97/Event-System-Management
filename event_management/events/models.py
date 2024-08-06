from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)  # Correct field name
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
