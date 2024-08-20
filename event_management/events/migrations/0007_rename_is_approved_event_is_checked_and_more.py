# Generated by Django 5.0.6 on 2024-08-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_is_approved_event_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='is_approved',
            new_name='is_checked',
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=50),
        ),
    ]
