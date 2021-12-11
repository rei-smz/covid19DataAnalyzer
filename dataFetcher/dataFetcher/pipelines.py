# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import time

from itemadapter import ItemAdapter
import scrapy.exporters


class DatafetcherPipeline:
    def open_spider(self, spider):
        self.file = open(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '_data.csv', 'wb')
        self.exporter = scrapy.exporters.CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
