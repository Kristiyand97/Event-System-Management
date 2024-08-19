from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site


class Command(BaseCommand):
    help = 'Update the Site domain and name.'

    def handle(self, *args, **kwargs):
        site = Site.objects.get_current()
        site.domain = '127.0.0.1:8000'
        site.name = 'EventHorizon'
        site.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated site domain and name.'))
