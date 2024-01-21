import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(item["jpg"])

    def item_completed(self, results, item, info):
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        imgName = request.url.split('/')[-1]
        return imgName
