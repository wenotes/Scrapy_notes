# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()#职位名                       
    company_name = scrapy.Field()#公司名称
    work_place = scrapy.Field()#工作地点
    salary = scrapy.Field()#薪资
    published = scrapy.Field()#发布时间
    job_infor_url = scrapy.Field()#职位的url
    company_infor_url = scrapy.Field()#公司简介的url

    job_infor = scrapy.Field()#职位信息
    company_infor = scrapy.Field()#公司简介
    company_website = scrapy.Field()#公司官网
    company_size = scrapy.Field()#公司规模
    industry = scrapy.Field()#所属行业


