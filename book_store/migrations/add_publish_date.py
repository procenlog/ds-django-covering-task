# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField("Book", "publish_date", models.DateField(default=date.today())),
    ]