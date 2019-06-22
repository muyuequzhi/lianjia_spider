from .sql import Sql
from ljia.items import LjiaItem


class LjiaPipeline(object):

    def process_item(self, item, spider):

        house = item['house']
        type = item['type']
        area = item['area']
        direction = item['direction']
        traffic = item['traffic']
        price = item['price']
        district = item['district']
        Sql.insert_ljia(house, type, area, direction, traffic, price, district)
        print('正在存放数据')