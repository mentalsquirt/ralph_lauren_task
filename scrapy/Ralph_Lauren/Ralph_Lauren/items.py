# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class RalphLaurenItem(scrapy.Item):
  image_type = scrapy.Field() # either 'person' or 'cloth'
  image_urls = scrapy.Field()
  images = scrapy.Field()
