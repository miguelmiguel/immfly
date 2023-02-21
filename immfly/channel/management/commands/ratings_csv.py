import csv
from django.http import HttpResponse
from django.core.management.base import BaseCommand, CommandError

from common.utils import detailed_exception_message
from channel.models import Channel


class Command(BaseCommand):
    help = 'Generate CSV containing all Channel Ratings'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs=1, type=str)

    def handle(self, *args, **options):
        try:
            ratings = Channel.get_all_ratings_sorted()
            filepath = options['file_path'][0]
            f = open(filepath, 'w')

            writer = csv.writer(f)
            writer.writerow(['Channel title', 'Average rating'])
            for ch in ratings:
                writer.writerow([ratings[ch]['title'], ratings[ch]['rating']])
            f.close()
        except Exception as e:
            error_message = detailed_exception_message(e)
            raise CommandError(error_message)