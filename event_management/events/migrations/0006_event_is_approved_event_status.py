# Generated by Django 5.0.6 on 2024-08-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_category_alter_event_organizer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
