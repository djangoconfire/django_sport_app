# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(max_length=200, null=True)),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('order_status', models.CharField(blank=True, max_length=2, null=True, choices=[(b'A', b'Active'), (b'CN', b'Cancelled')])),
                ('product_url', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('order_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to='user_profile.UserProfile', null=True)),
            ],
            options={
                'ordering': ['order_created'],
            },
        ),
    ]
