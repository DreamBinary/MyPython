# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import hashlib
import mimetypes
import os
from io import BytesIO
from scrapy.utils.python import to_bytes
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline


class UpsplashPipeline:
    def process_item(self, item, spider):
        return item


class MyImagePipeline(ImagesPipeline):
    def convert_image(self, image, size=None):
        buf = BytesIO()
        if image.format == 'PNG':
            image.save(buf, 'PNG')
        else:
            image.save(buf, 'JPEG')
        if size:
            image = image.copy()
            image.thumbnail(size, self._Image.ANTIALIAS)
        return image, buf


class MyFilePipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        media_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        media_ext = os.path.splitext(request.url)[1]
        # Handles empty and wild extensions by trying to guess the
        # mime type then extension or default to empty string otherwise
        if media_ext not in mimetypes.types_map:
            media_ext = ''
            media_type = mimetypes.guess_type(request.url)[0]
            if media_type:
                media_ext = mimetypes.guess_extension(media_type)
        return f'full/{media_guid}{media_ext}'
