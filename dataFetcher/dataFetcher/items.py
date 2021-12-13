# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DatafetcherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    region = scrapy.Field()
    confirmed = scrapy.Field()
    deceased = scrapy.Field()
    active = scrapy.Field()
    recovered = scrapy.Field()
    vaccinated = scrapy.Field()
    population = scrapy.Field()
