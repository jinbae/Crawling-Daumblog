# -*- coding: utf-8 -*-

import scrapy

from daumblog.items import DaumblogItem


class DaumblogSpider(scrapy.Spider):        
	name="daum"
	allowed_domains = ["blog.daum.net"]
	start_urls = ["http://blog.daum.net/_blog/_top/sub/blogByCategorySubNew.do?category=%d&list_type=recent&page_no=%d" % (c, p)
                      for c in range(101,115) + range(201,206) + range(302,309) + range(401,406) + range(501,507) + range(601,607)
                      for p in xrange(1,251)]

	def parse(self, response):                
		for sel in response.xpath('//div[@id="articleFromCategory"]/ul[@class="list_blog_type2"]/li'):
                        if response.xpath('//div[@id="articleFromCategory"]/ul[@class="list_blog_type2"]/li[@class="no_list fst"]/text()').extract() != []:
                                break
                        item = DaumblogItem()
                        item['crawlUrl'] = response.url
                        item['title'] = sel.xpath('div[@class="box_info"]/strong/a/text()').extract()[0]
                        item['category'] = response.xpath('//div[@class="sub_title"]/h3/strong/text()').extract()[0]+">"+response.xpath('//div[@class="sub_title"]/h3/strong/text()').extract()[1]
                        item['link'] = sel.xpath('div[@class="box_info"]/strong/a/@href').extract()[0]
                        item['date'] = sel.xpath('div[@class="box_info"]/span[@class="date"]/text()').extract()[0].replace('.', '-')
                        if sel.xpath('p/a/text()').extract() != []:
                                 item['desc'] = sel.xpath('p/a/text()').extract()[0]
                        else :
                                 item['desc'] = 'None'
                        if sel.xpath('a/img/@src').extract() != []:
                                 item['img'] = sel.xpath('a/img/@src').extract()[0]
                        else :
                                 item['img'] = 'None'
                                        
                        yield item
                           
		
                        

                               
                        
