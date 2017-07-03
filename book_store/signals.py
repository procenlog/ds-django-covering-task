import logging
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from .models import Book

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('book_store/book_manipulation.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s', '[%d/%b/%Y %H:%M:%S]')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

@receiver(post_save, sender=Book, dispatch_uid="save_signal_handler")
def save_signal_handler(sender, **kwargs):
    if kwargs['created']:
        logger.info("Created: " + str(kwargs['instance']))
    else:
        logger.info("Edited: " + str(kwargs['instance']))

@receiver(post_delete, sender=Book, dispatch_uid="delete_signal_handler")
def delete_signal_handler(sender, **kwargs):
    logger.info("Deleted: " + str(kwargs['instance']))