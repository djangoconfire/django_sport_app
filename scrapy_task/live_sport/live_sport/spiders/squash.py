# -*- coding: utf-8 -*-
import scrapy
from live_sport.items import LiveSportItem

class SquashSpider(scrapy.Spider):
    name = "squash"
    allowed_domains = ["livesport.com"]
    start_urls = ['http://www.livesport.com/squash/']



    def parse(self,response):
       pass
