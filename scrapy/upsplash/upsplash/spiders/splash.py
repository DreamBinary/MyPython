import scrapy
from PIL.Image import Image
from upsplash.items import UpsplashItem
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None


class SplashSpider(scrapy.Spider):
    name = 'splash'
    allowed_domains = ['unsplash.com']
    start_urls = ['https://unsplash.com/']

    def parse(self, response):
        urls = response.xpath('//div[@data-test="editorial-route"]//a[@rel="nofollow"]/@href').extract()
        yield UpsplashItem(file_urls=urls)
