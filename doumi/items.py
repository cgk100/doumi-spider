# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoumiItem(scrapy.Item):
    # define the fields for your item here like:
     title    = scrapy.Field()
     price    = scrapy.Field()
     cpy_name= scrapy.Field()
     cpy_type=scrapy.Field()
     cpy_time=scrapy.Field()
     posttime=scrapy.Field()
     cate_tag=scrapy.Field()
     url     =scrapy.Field()
     description =scrapy.Field()
     request_num=scrapy.Field()
     jiesuan    =scrapy.Field()
     address    =scrapy.Field()
     tag_type   =scrapy.Field()


