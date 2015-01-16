# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaumblogItem(scrapy.Item):

    crawlUrl = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    desc = scrapy.Field()
    img = scrapy.Field()

    pass
