import os
import re
import sys
from scrapy import cmdline

sql_write = "'ljia.mysqlpipelines.pipelines.LjiaPipeline': 300"
csv_write = "'ljia.pipelines.LjiaPipeline': 300"

def replace(file_path, old_str, new_str):
    f = open(file_path,'r+')
    all_lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in all_lines:
      line = line.replace(old_str, new_str)
      f.write(line)
    f.close()

if str(sys.argv[1]) == 'csv':
    replace('settings.py', sql_write, csv_write)
    print('正在保存为csv文件')
    cmdline.execute('scrapy crawl ljia -o zufang.csv -t csv'.split())
elif str(sys.argv[1]) == 'mysql':
    replace('settings.py', csv_write, sql_write)
    print('正在保存至mysql')
    cmdline.execute('scrapy crawl ljia'.split())
else:
    print('is not support')

