# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql

class JobPipeline(object):
    def __init__(self):#这也是就爬虫开始的时候执行一次
        self.file = open('job.json',"w",encoding='utf-8')
        self.file.write("[")

    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii=False)+",\n"#如果这里面的数据有中文的话，就要用ensure_ascii=False。
        self.file.write(text)
        return item
    def close_file(self,spider):#这个是爬虫结束才关闭
        self.file.write(']')
        self.file.close()
# class JobMysqldbPipeline(object):
#     def __init__(self):
#         self.conn = pymysql.Connect(host="localhost",port="3306",user="wp",passwd="123456",db="jobsdb",charset="utf-8")

#     def process_item(self,item,spider):
#         pass
        