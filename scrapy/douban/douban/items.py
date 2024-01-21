# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    people = scrapy.Field()
    time = scrapy.Field()
    place = scrapy.Field()
    type = scrapy.Field()
