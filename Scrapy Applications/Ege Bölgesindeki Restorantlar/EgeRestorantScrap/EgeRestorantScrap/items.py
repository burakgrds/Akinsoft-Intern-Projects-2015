# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EgerestorantscrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    isim = scrapy.Field()
    adres = scrapy.Field()
    sehir = scrapy.Field()
    tel = scrapy.Field()
    ilce = scrapy.Field()

    pass
