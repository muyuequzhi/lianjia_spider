## 将去上海，第一件事不是找漂亮小姐姐，而是先找房。。。

+ 采用scrapy爬取了上海链家将近20000条数据，然后进行分析。

![img](https://github.com/muyuequzhi/lianjia_spider/tree/master/imgs/ljia1.png)

```
保存至csv文件：
python start.py csv
保存至mysql：
python start.py mysql
```

+ 保存至mysql时首先创建表：
```
CREATE TABLE `ljia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `house` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `direction` varchar(255) DEFAULT NULL,
  `traffic` int(5) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `district` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 ;
然后更改/ljia/mysqlpipelines/sql.py 中连接数据库的信息
```

+ 字段的实际意义
```
house、type、area、direction、price、traffic、district
名称、户型、大小、朝向、价格、离地铁最近的距离(m)、地区
```

+ 数据分析的代码及过程在: https://github.com/muyuequzhi/lianjia_spider/ljia.ipynb
![img](https://github.com/muyuequzhi/lianjia_spider/tree/master/imgs/ljia2.png)
