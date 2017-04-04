# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_sport_app', '0002_auto_20170402_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True),
        ),
    ]
