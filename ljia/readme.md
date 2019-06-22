将去上海，第一件事不是找漂亮小姐姐，而是先找房。。。

采用scrapy爬取了上海链家将近20000条数据，然后进行分析。

保存至csv文件：

python entrypoint.py csv

保存至mysql：

python entrypoint.py mysql

首先创建mysql表：

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
) ENGINE=InnoDB AUTO_INCREMENT=18695 DEFAULT CHARSET=utf8 ;

然后更改/ljia/mysqlpipelines/sql.py 中连接数据库的信息

img<imag>
