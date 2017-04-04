import sys, os, django
from decimal import Decimal

sys.path.append("/home/pycon/Desktop/Live_your_sport/live_sport")  # Set it to the root of your project
os.environ["DJANGO_SETTINGS_MODULE"] = "live_sport.settings"
django.setup()

import csv

# Full path and name to your csv file
csv_filepathname = "/home/pycon/Desktop/Live_your_sport/live_sport/order.csv"

from live_sport_app.models import Order
from django.conf import settings
from utils import *

with open(csv_filepathname,'rU') as csv_file:
    next(csv_file)
    dataReader = csv.reader(csv_file,delimiter=',', quotechar='"')

    for row in dataReader:
        order=Order()
        order.order_id=row[2]
        order.product_name=row[6]
        order.order_status=row[1]
        order.product_url=row[7]
        if row[23]:
            order.price=(Decimal(row[23]) * 66 )
        print order
        print 'for debugging'
        # order.price=row[23]
        order.save()