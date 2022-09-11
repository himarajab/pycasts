from django.core.management import BaseCommand
from podcasts.tasks import hello_celery

class Command(BaseCommand):
    help = "A description of the command"
    
    def handle(self, *args, **options):
        hello_celery.delay()
        self.stdout.write("My sample command just ran.")


