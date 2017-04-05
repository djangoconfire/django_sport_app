# -*- coding: utf-8 -*-
import scrapy
from live_sport.items import LiveSportItem
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from utils import *

class SquashSpider(scrapy.Spider):
    name = "squash"
    allowed_domains = ["liveyoursport.com"]
    start_urls = []

    for num in range(1,100):
        start_urls.append("https://www.liveyoursport.com/squash/?page=" + str(num))

    def parse(self, response):
        selector_list=response.xpath("//*[@class='category-page']/ul/li")
        for selector in selector_list:
            item = LiveSportItem()
            item['product_name'] =  selector.xpath("div[3]/strong/a/text()")[0].extract()
            url = selector.xpath("div[3]/strong/a/@href")[0].extract()
            item['product_url'] = url
            price = selector.xpath("div[3]/em/span/text()")[0].extract()
            item['price'] = price
            request = Request(url, callback=self.live_sport_item)
            request.meta['item'] = item
            yield request

    def live_sport_item(self, response):
        pass
