# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirbnbscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    page_url = scrapy.Field()
    pass
