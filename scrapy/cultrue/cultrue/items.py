# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CultrueItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 项目序号
    num_sec = scrapy.Field()
    # 编号
    num = scrapy.Field()
    # 名称
    title = scrapy.Field()
    # 类别
    type = scrapy.Field()
    # 公布时间
    rx_time = scrapy.Field()
    # 类型
    cate = scrapy.Field()
    # 申报地区或单位
    province = scrapy.Field()
    # 保护单位
    protect_unit = scrapy.Field()
