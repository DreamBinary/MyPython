# -*- coding: UTF-8 -*-

import scrapy
from scrapy.pipelines.images import ImagesPipeline

from pexels.items import PexelsItem


class PexelSpider(scrapy.Spider):
    name = 'pexel'
    allowed_domains = ['www.pexels.com']
    start_urls = ['https://www.pexels.com']

    def parse(self, response):
        print("------------------------------------------")
        print(response.text)
        # print(dir(response))
        # print(response.status)
        # print(response.text.get().encode(response.encoding).decode('gbk'))
        image_urls = response.xpath('//article[@class="MediaCard_card__PAVEg"]/a/img/@src').extract()
        print(image_urls)
        yield PexelsItem(name=response.text)

