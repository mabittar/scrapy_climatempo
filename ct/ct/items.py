# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime


class CtItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field()
    weather_now_C = scrapy.Field()
    felling = scrapy.Field()
    wind = scrapy.Field()
    humidity = scrapy.Field()
    pressure = scrapy.Field()
    url = scrapy.Field()
    register_at = scrapy.Field()
