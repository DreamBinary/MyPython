# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter


class Reading2Pipeline:
    # def open_spider(self, spider):
    #     self.file = open("read.json", "w", encoding="utf-8")
    #
    # def process_item(self, item, spider):
    #     self.file.write(str(item))
    #
    # def close_spider(self, spider):
    #     self.file.close()

    def open_spider(self, spider):
        self.file = open("read.csv", "wb")
        self.exporter = CsvItemExporter(self.file, encoding="utf-8-sig")
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
