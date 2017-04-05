
import os
import subprocess
from celery import task

@task()
def crawl():
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'scrapy_task.live_sport.live_sport.settings'
    return subprocess.call(['scrapy', 'crawl', 'squash'])
