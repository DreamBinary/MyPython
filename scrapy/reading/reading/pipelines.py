# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests
from itemadapter import ItemAdapter


class ReadingPipeline:

    # def process_item(self, item, spider):
    #     print("---------------------------------------")
    #     print(item["png"])
    #     content = requests.get(item["png"]).content
    #     with open("D:/MyPython/MyProject_1/img/" + item["alt"] + ".jpg", "wb") as file:
    #         file.write(content)
    #     file.close()
    pass