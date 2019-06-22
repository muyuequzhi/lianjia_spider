import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ljia.items import LjiaItem


class Myspider(scrapy.Spider):

    name = 'ljia'
    bash_url = ("https://sh.lianjia.com/zufang/{}")

    def start_requests(self):
        # 将每个地区的url传给下个函数
        district_dic = {'jingan/': '静安', 'xuhui/': '徐汇', 'huangpu/': '黄浦', 'changning/': '长宁', 'putuo/': '普陀',
                        'pudong/': '浦东', 'baoshan/': '宝山', 'zhabei/': '闸北', 'hongkou/': '虹口', 'yangpu/': '杨浦',
                        'minhang/': '闵行', 'jinshan/': '金山', 'jiading/': '嘉定', 'chongming/': '崇明',
                        'fengxian/': '奉贤', 'songjiang/': '松江', 'qingpu/': '青浦'}
        for key in district_dic.keys():
            district = district_dic[key]
            url = self.bash_url.format(key)
            print(url)
            # meta 将变量值传给下一个参数
            yield Request(url, self.parse, meta={'district': district})

    def parse(self, response):
        # 构造每个地区所有的url
        soup = BeautifulSoup(response.text, 'lxml')
        district = response.meta['district']
        l_url = 'pg{}/#contentList'
        # 得到总页数
        total_page = soup.find('div', class_='content__pg')['data-totalpage'] # data-totalpage是和class相同级别的属性
        # 拼接成完整url
        for num in range(1, eval(total_page)+1):
            url = response.url + l_url.format(num)
            print(url)
            yield Request(url, callback=self.get_detail, meta={'district': district})

    def get_detail(self, response):
        # 获取每个页面房源的链接
        district = response.meta['district']
        soup = BeautifulSoup(response.text, 'lxml')
        urls = soup.find_all('p', class_="content__list--item--title twoline")
        for url in urls:
            bashurl = url.a.get('href')
            url = 'http://sh.lianjia.com/{}'.format(bashurl)
            yield Request(url, callback=self.get_value, meta={'district':district})


    def get_value(self, response):
        # 获取所需信息
        item = LjiaItem()
        soup = BeautifulSoup(response.text, 'lxml')
        tra_list = []
        type1 = soup.find('p', class_='content__article__table').text.strip().split()  # 户型

        item['house'] = soup.find('p', class_='content__title').text.strip()  # 名称
        item['type'] = type1[1]
        item['area'] = type1[2]
        item['direction'] = type1[3]
        price = soup.find('p', class_='content__aside--title').text.strip()  # 价格
        item['price'] = re.search(r'\d+', price).group() # 找到数字部分
        traffic = soup.find('div', class_='content__article__info4').text.strip() # 交通
        traffic = re.findall(r'[0-9]{1,4}m', traffic)
        #找出离地铁最近的距离
        for i in traffic:
            tra = eval(i[:-1])
            tra_list.append(tra)
        tra_list.sort()
        if tra_list == []:
            tra_list.append(0)
        item['traffic'] = tra_list[0]
        item['district'] = response.meta['district']

        return item


    def get_district(content):
        #下载城市对应的后几位网址
        district = {}
        a = content.find_all('li', class_="filter__item--level2", limit=18)
        for i in a:
            href = i.a.get('href').replace('/zufang/', '')
            text = i.text.strip()
            district[ href ] = text
        #删除不限地区的那一项
        district.pop('')
        print(district)
