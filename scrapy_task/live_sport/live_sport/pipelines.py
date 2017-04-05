# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3 as lite
from items import LiveSportItem

class LiveSportPipeline(object):

    def __init__(self):
        self.setup_database_con()
        self.createTables()

    def process_item(self, item, spider):

        if(isinstance(item, LiveSportItem)):
            self.storeInLiveSportTable(item)

        return item

    def storeInLiveSportTable(self, item):
        self.cur.execute("INSERT INTO live_sport_app_order(\
            product_name,\
            product_url, \
            price,\
            description\
            ) \
        VALUES( ?, ?,?,? )", \
        ( \
            item.get('product_name', 0),
            item.get('product_url', 0),
            item.get('price', ''),
            item.get('description', '')
        ))
        self.con.commit()


    def setup_database_con(self):
        self.con = lite.connect('scrap_data.db')
        self.cur = self.con.cursor()

    def createTables(self):
        self.dropLiveSportTable()
        self.createLiveSportTable()

    def dropLiveSportTable(self):
        self.cur.execute("DROP TABLE IF EXISTS language")

    def createLiveSportTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS live_sport_app_order(id INTEGER PRIMARY KEY NOT NULL, \
            product_name TEXT NOT NULL, \
            product_url TEXT,\
            description TEXT,\
            price INTEGER\
            )")

    def  close_spider(self,spider):
        self.con.close()
