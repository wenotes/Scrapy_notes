#coding:utf-8


import scrapy
from job.items import JobItem
import urllib.parse


class jobspider(scrapy.Spider):
	name = "searchjobs"
	allowed_domains = ["http://search.51job.com"]
	offset = 1
	url = "http://search.51job.com/list/030200,000000,0000,00,2,99,"+urllib.parse.quote("自动化测试")+",2,"
	start_urls = [url+str(offset)+".html?"]#这个列表里面的url只会执行一次，写成元组也行
	# "http://search.51job.com/list/030200,000000,0000,00,2,99,python,2,1.html?"
	def parse(self,response):
		for each in response.xpath('//*[@id="resultList"]/div[@class="el"]'):
			l = len(response.xpath('//*[@id="resultList"]/div'))#response.css()也行
			# print(l)
			if l<=3:
				break
			else:
				item = JobItem()
				#extract()方法返回的都是Unicode字符串列表
				item['job_name'] = each.xpath('./p/span/a/text()').extract()[0].strip()
				job_infor_url = each.xpath('./p/span/a/@href').extract()[0].strip()
				item['company_name'] = each.xpath('./span[@class="t2"]/a/text()').extract()[0].strip()
				company_infor_url = each.xpath('./span[@class="t2"]/a/@href').extract()[0].strip()
				item['work_place'] = each.xpath('./span[@class="t3"]/text()').extract()[0].strip()
				if len(each.xpath('./span[@class="t4"]/text()'))==0:
					item['salary'] = u"薪资面议"
				else:
					item['salary'] = each.xpath('./span[@class="t4"]/text()').extract()[0].strip()
				item['published'] =each.xpath('./span[@class="t5"]/text()').extract()[0].strip()

				# print(item['job_name']+item['job_infor_url']+item['company_name']+item['company_infor_url']+item['work_place']+item['salary']+item['published']+'\n')
				yield scrapy.Request(job_infor_url,callback=self.get_jobinfor,dont_filter=True,meta={'job_infor_url':job_infor_url})
				yield scrapy.Request(company_infor_url,callback=self.get_conpanyinfor,dont_filter=True,meta={'company_infor_url':company_infor_url})
				yield item
				
		self.offset+=1
		yield scrapy.Request(self.url+str(self.offset)+".html?",callback=self.parse,dont_filter=True)#dont_filter是因为你在allowed_domain那里加了http://
	
	def get_jobinfor(self,response):
		item = JobItem()
		item['job_infor_url'] = str(response.meta['job_infor_url']).strip()
		item['job_infor'] = response.xpath('//span[@class="label"]')[0].extract()[0].strip()

		# print(item['job_infor'])
		return item

	def get_conpanyinfor(self,response):
		item = JobItem()
		item['company_infor_url'] = str(response.meta['company_infor_url']).strip()
		item['company_infor'] = response.xpath('//div[@class="con_msg"]/div/p/text()').extract()[0].strip()
		item['company_website'] = response.xpath('//div[@class="tBorderTop_box"]/div/p/a/@href').extract()[0].strip()
		item['company_size'] = response.xpath('//p[@class="ltype"]').extract()[0].strip()
		# item['industry'] = response.xpath().extract()[0].strip()
		# print(item['company_infor']+item['company_website']+item['company_size']+item['industry'])
		return item