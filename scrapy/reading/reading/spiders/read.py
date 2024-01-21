import scrapy
from reading.items import ReadingItem
from scrapy.pipelines.images import ImagesPipeline


class ReadSpider(scrapy.Spider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1107_1.html']

    def parse(self, response):
        img = response.xpath('//div[@class="book-info"]//img')

        # alt = img.xpath("./@alt").extract()
        jpgs = img.xpath("./@data-original").extract()
        print("--------------------------------------------")
        print(jpgs)
        yield ReadingItem(image_urls=jpgs)
        # print(alt, png)
        # for i, j in zip(alt, png):
        #     # print(i, j)
        #     item = ReadingItem(alt=i, png=j)
        #     yield item
        # yield item
