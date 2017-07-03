from django.apps import AppConfig

class BookStoreConfig(AppConfig):
    name = 'book_store'

    def ready(self):
        AppConfig.ready(self)
        from book_store import signals