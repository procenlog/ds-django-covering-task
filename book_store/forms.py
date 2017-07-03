from django import forms
from django.forms.widgets import Textarea
from django.forms.extras.widgets import SelectDateWidget
from .models import Book


class BookForm(forms.ModelForm):
    publish_date = forms.DateField(widget=SelectDateWidget(years = tuple([i for i in range(1970, 2021)])))

    class Meta():
        model = Book
        fields = ['title', 'author', 'info', 'ISBN', 'publish_date', 'price', 'image']