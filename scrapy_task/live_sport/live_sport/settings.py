# -*- coding: utf-8 -*-

import sys, os, django
# django project settings

from decouple import config

sys.path.append("/home/pycon/Desktop/Live_your_sport/live_sport")  # Set it to the root of your project
os.environ["DJANGO_SETTINGS_MODULE"] = "live_sport.settings"
django.setup()


BOT_NAME = 'live_sport'

SPIDER_MODULES = ['live_sport.spiders']
NEWSPIDER_MODULE = 'live_sport.spiders'


ITEM_PIPELINES = {
    'live_sport.pipelines.LiveSportPipeline': 300,
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
