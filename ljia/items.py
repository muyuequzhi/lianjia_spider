# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    direction = scrapy.Field()
    traffic = scrapy.Field()
    price = scrapy.Field()
    district = scrapy.Field()


#    pass
