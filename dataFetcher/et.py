import csv

from lxml import etree

file_list = ['./12/12.5/Coronavirus Dashboard.html',
             './12/12.6/Coronavirus Dashboard.html',
             './12/12.7/Coronavirus Dashboard.html',
             './12/12.8/Coronavirus Dashboard.html',
             './12/12.9/Coronavirus Dashboard.html',
             './12/12.10/Coronavirus Dashboard.html']


def rm_m1_func(x):
    return '' if x == '-1' else x


for f in file_list:
    csv_file = open(f[5:9] + '_data.csv', 'w')
    writer = csv.DictWriter(csv_file, fieldnames=['region', 'confirmed', 'deceased', 'vaccinated', 'population'])
    writer.writeheader()
    file = etree.parse(f, etree.HTMLParser())
    data = file.xpath('//table[@id="sortable_table_world"]/tbody/tr')
    writer.writerow({'region': 'World',
                     'confirmed': data[0].xpath('./td[2]/@data-order')[0],
                     'deceased': data[0].xpath('./td[4]/@data-order')[0],
                     'vaccinated': data[0].xpath('./td[10]/@data-order')[0],
                     'population': data[0].xpath('./td[11]/@data-order')[0]})

    for item in data[1:]:
        writer.writerow({'region': item.xpath('./td[1]/div/span[2]/text()')[0].strip(),
                         'confirmed': rm_m1_func(item.xpath('./td[2]/@data-order')[0]),
                         'deceased': rm_m1_func(item.xpath('./td[4]/@data-order')[0]),
                         'vaccinated': rm_m1_func(item.xpath('./td[10]/@data-order')[0]),
                         'population': rm_m1_func(item.xpath('./td[11]/@data-order')[0])})
