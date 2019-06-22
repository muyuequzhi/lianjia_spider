import pymysql
from ljia import settings

MYSQL_HOSTS = '192.168.6.6'
MYSQL_USER = 'test'
MYSQL_PASSWORD = 'a'
MYSQL_PORT = '3306'
MYSQL_DB = 'ljia'

connection = pymysql.connect(host='192.168.6.6', port=3306, user='test',
                              password='a', db='test')
cur = connection.cursor()

class Sql:
    @classmethod
    def insert_ljia(cls, house, type, area, direction, traffic, price, district):
        sql = 'INSERT INTO ljia (`house`, `type`, `area`, `direction`, `traffic`, `price`, `district`) VALUES (%(house)s, %(type)s, %(area)s, %(direction)s, %(traffic)s, %(price)s, %(district)s)'
        value = {
            'house': house,
            'type': type,
            'area': area,
            'direction': direction,
            'traffic': traffic,
            'price': price,
            'district': district
        }
        cur.execute(sql, value)
        connection.commit()

