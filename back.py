# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class CtPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("clima.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        # table_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='clima'"
        #schema do BD
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS clima (
                            city TEXT NOT NULL,
                            weather_now_C TEXT,
                            felling TEXT,
                            wind TEXT,
                            humidity TEXT,
                            pressure INTEGER,
                            url TEXT,
                            register_at TEXT)
        """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute(
            """insert INTO clima values (?, ?, ?, ?, ?, ?, ?, ?)""",
            (item['city'][0], item['weather_now_C'][0], item['felling'][0],
             item['wind'][0], item['humidity'][0], item['pressure'][0],
             item['url'], item['register_at']))

        #write database
        self.conn.commit()

        #close connection to DB
        self.conn.close()
