import json

import scrapy
from cultrue.items import CultrueItem

class CultureSpider(scrapy.Spider):
    name = 'culture'
    allowed_domains = ['www.ihchina.cn']
    start_urls = ['https://www.ihchina.cn/Article/Index/getProject.html?type=2&category_id=16&limit=10&p=1']
    base_url = "https://www.ihchina.cn/Article/Index/getProject.html?type=2&category_id=16&limit=10&p="
    page = 1

    def parse(self, response):
        print("********************************************")
        data = json.loads(response.text)
        list = data["list"];
        if list is None:
            return
        for i in list:
            num_sec = i["num_sec"]
            num = i["num"]
            title = i["title"]
            type = i["type"]
            rx_time = i["rx_time"]
            cate = i["cate"]
            province = i["province"]
            protect_unit = i["protect_unit"]
            item = CultrueItem(num_sec=num_sec, num=num, title=title, type=type, rx_time=rx_time, cate=cate,
                               province=province, protect_unit=protect_unit)
            yield item
        self.page += 1
        yield scrapy.Request(url=self.base_url + str(self.page), callback=self.parse)
        print("********************************************")
        # result = response.xpath('//*[@id="table"]/tbody/tr/td')
        # print(result.extract())
