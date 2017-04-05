# -*- coding: utf-8 -*-


import os
import sys
import django

# django project settings

from decouple import config

DJANGO_PROJECT_PATH='/home/pycon/Desktop/Live_your_sport'

DJANGO_SETTINGS_MODULE = 'live_sport.settings'
sys.path.insert(0, DJANGO_PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE


BOT_NAME = 'live_sport'

SPIDER_MODULES = ['scrapy_task.live_sport.live_sport.spiders']
NEWSPIDER_MODULE = 'scrapy_task.live_sport.live_sport.spiders'

#
# sys.path.insert(0,'/home/pycon/Desktop/Live_your_sport')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'live_sport.settings'

ITEM_PIPELINES = {
    'scrapy_task.live_sport.live_sport.pipelines.LiveSportPipeline': 300,
}

DOWNLOAD_DELAY = 0.5
# Obey robots.txt rules
ROBOTSTXT_OBEY = True
