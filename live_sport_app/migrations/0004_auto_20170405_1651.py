# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_sport_app', '0003_auto_20170402_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'Active', b'Active'), (b'Cancelled', b'Cancelled')]),
        ),
    ]
