import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem


class FilmSpider(CrawlSpider):
    name = 'film'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow=r'\?start=\d+&filter='), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print("==========================")
        response.body.decode(encoding='utf-8')
        title_x = response.xpath('//div/a/span[@class="title"][1]/text()')
        title = [i.extract() for i in title_x]
        info_x = response.xpath('//div[@class="bd"]/p/text()')
        info = [i.extract().strip() for i in info_x]
        info = [i for i in info if i != '']
        people = info[::2]
        info2 = [i.split("/") for i in info[1::2]]
        time = [i[0] for i in info2]
        place = [i[1].split(" ")[0] for i in info2]
        type = [i[2].split(" ")[0] for i in info2]
        for i, j, k, l, m in zip(title, people, time, place, type):
            yield DoubanItem(title=i, people=j, time=k, place=l, type=m)

    #  第一页 特殊 提取不到链接
    # def parse_start_url(self, response, **kwargs):
    #     self.parse_item(response) 顺序问题
    #     print("++++++++++++++++++++++++++++++++++++++++")

    def parse_start_url(self, response, **kwargs):
        print("==========================")
        response.body.decode(encoding='utf-8')
        title_x = response.xpath('//div/a/span[@class="title"][1]/text()')
        title = [i.extract() for i in title_x]
        info_x = response.xpath('//div[@class="bd"]/p/text()')
        info = [i.extract().strip() for i in info_x]
        info = [i for i in info if i != '']
        people = info[::2]
        info2 = [i.split("/") for i in info[1::2]]
        time = [i[0] for i in info2]
        place = [i[1].split(" ")[0] for i in info2]
        type = [i[2].split(" ")[0] for i in info2]
        for i, j, k, l, m in zip(title, people, time, place, type):
            yield DoubanItem(title=i, people=j, time=k, place=l, type=m)
