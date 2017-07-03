from optparse import make_option
from django.core.management.base import BaseCommand, CommandError

from book_store.models import Book

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-o', '--order',
            action='store',
            dest='order',
            choices=['asc', 'desc'],
            default=None,
            help='Possibility to order by publish date field defining ordering (asc/desc)'),
        )

    def handle(self, *args, **options):
        if options['order']:
            if options['order'] == 'asc': book_list = Book.objects.order_by('publish_date')
            elif options['order'] == 'desc': book_list = Book.objects.order_by('-publish_date')
        else: book_list = Book.objects.all()

        for book in book_list:
            self.stdout.write(self.style.SUCCESS(" - %s" % book.title))