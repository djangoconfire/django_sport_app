# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_sport_app', '0004_auto_20170405_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'Active', b'Active'), (b'Cancelled', b'Cancelled')]),
        ),
    ]
