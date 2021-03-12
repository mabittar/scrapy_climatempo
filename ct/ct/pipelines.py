# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class CtPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)

        db = self.conn['clima']
        self.collection = db['clima_tb']

    def create_connection(self):
        self.conn = sqlite3.connect("clima.db")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        self.store_db(item)
        return item
