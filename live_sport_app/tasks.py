import requests

from django.conf import settings
from celery import task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .models import Order

logger = get_task_logger(__name__)
process = CrawlerProcess(get_project_settings())


# Scraper tasks - scrape orders credentials
@periodic_task(run_every=(crontab(minute='*/10')),
               name="scrape_orders")
def scrape_orders():
    process.crawl('squash')
    process.start()
