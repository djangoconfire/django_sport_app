# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_sport_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=6, blank=True),
        ),
    ]
