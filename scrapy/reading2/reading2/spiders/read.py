import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from reading2.items import Reading2Item


# scrapy genspider -t crawl read https://www.dushu.com/book/1107.html
class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1107_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1107_\d+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title = response.xpath('//div[@class="book-info"]//h3/a/text()')
        author = response.xpath('//div[@class="book-info"]/p/text()')
        for i, j in zip(title, author):
            # print(i.extract())
            yield Reading2Item(title=i.extract(), author=j.extract())

