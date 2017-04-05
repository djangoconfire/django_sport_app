# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field
from scrapy_djangoitem import DjangoItem
# from .live_sport_app import models

#
# class ScrapedItem(DjangoItem):
#     django_model = models.Order


class LiveSportItem(Item):
    product_name = Field()
    product_url=Field()
    price =Field()
    description =Field()
