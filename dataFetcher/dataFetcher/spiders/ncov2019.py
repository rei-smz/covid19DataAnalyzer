import scrapy


def rm_m1_func(x):
    return '' if x == '-1' else x


class Ncov2019Spider(scrapy.Spider):
    name = 'ncov2019'
    allowed_domains = ['ncov2019.live']
    start_url = 'https://ncov2019.live/'

    def start_requests(self):
        yield scrapy.Request(url=self.start_url + 'data/world', callback=self.parse)

    def parse(self, response):
        data = response.xpath('//table[@id="sortable_table_world"]/tbody/tr')

        # 处理全球总数
        yield {'region': 'World',
               'confirmed': data[0].xpath('./td[2]/@data-order').get(),
               'deceased': data[0].xpath('./td[4]/@data-order').get(),
               'active': data[0].xpath('./td[7]/@data-order').get(),
               'recovered': data[0].xpath('./td[8]/@data-order').get(),
               'vaccinated': data[0].xpath('./td[10]/@data-order').get(),
               'population': data[0].xpath('./td[11]/@data-order').get()}

        # 处理剩下数据
        for item in data[1:]:
            obj = {'region': item.xpath('./td[1]/div/span[2]/text()').get().strip(),
                   'confirmed': rm_m1_func(item.xpath('./td[2]/@data-order').get()),
                   'deceased': rm_m1_func(item.xpath('./td[4]/@data-order').get()),
                   'active': rm_m1_func(item.xpath('./td[7]/@data-order').get()),
                   'recovered': rm_m1_func(item.xpath('./td[8]/@data-order').get()),
                   'vaccinated': rm_m1_func(item.xpath('./td[10]/@data-order').get()),
                   'population': rm_m1_func(item.xpath('./td[11]/@data-order').get())}
            yield obj
