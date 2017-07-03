from datetime import datetime
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    info = models.TextField()
    ISBN = models.CharField(max_length=20) #primary key?
    price = models.DecimalField(decimal_places=2, max_digits=5)
    image = models.ImageField(upload_to='book_store/uploads')

    app_label = "book_store"
    model_name = "book"

    def __str__(self):
        return self.title


class RequestsManager(models.Manager):

    def last_10(self):
        return RequestRecord.requests.order_by('-id')[:10]


class RequestRecord(models.Model):
    path = models.URLField()
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.time.strftime('[%d/%b/%Y %H:%M:%S] - ') + self.path

    requests = RequestsManager()
