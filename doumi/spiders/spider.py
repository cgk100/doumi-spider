# -*- coding: utf-8 -*-
import scrapy,time
import re
from scrapy import log
from doumi.items import DoumiItem


class Doumi(scrapy.Spider):
    name = 'doumi'
    allowed_domains = ['doumi.com']
    start_urls = ['http://www.doumi.com/ty/']

    def parse(self, response):
        sel=scrapy.Selector(response)
        sites=sel.xpath('//h3/a/@href').extract()

        ##get next url 
        next_url=sel.xpath('//a[contains(@class,"next")]/@href')[0].extract()

        for val in sites:
            abs_url=response.urljoin(val)
            yield scrapy.Request(abs_url,callback=self.parese_article)

        if next_url:
            next_url='http://www.doumi.com'+next_url
            print '+++++++++++++++++++++++++++++'
            print next_url
            yield scrapy.Request(next_url,callback=self.parse) 



    def parese_article(self,response):
        detail=response.xpath('//div[contains(@class,"clearfix")]')
        item=DoumiItem()
        dr=re.compile(r'<[^>]+>',re.S)

        item['title']    =detail.xpath('//h2/text()').extract_first(default='not-found').strip()
        item['price']   =detail.xpath('//b/text()').extract_first(default='not-found').strip()
        item['cpy_name'] =detail.xpath('//div[contains(@class,"cpy-name")]/a/text()').extract_first(default='not-find').strip()
        item['cpy_type'] =detail.xpath('//div[contains(@class,"cpy-intro-txt")]/span[2]/text()').extract_first(default='not-found').strip()
        item['jiesuan'] =detail.xpath('//div[contains(@class,"salary-tips")]/span/text()').extract_first(default='not-foudn').strip()
        item['cate_tag'] =detail.xpath('//div[contains(@class,"salary-tips")]/span[2]/text()').extract_first(default='not-found').strip()
        request_num =detail.xpath('//div[contains(@class,"salary-tips")]/span/text()').extract()[2].strip()
        item['address'] =detail.xpath('//*[@id="work-addr-fold"]/div/text()').extract_first(default='not-find').strip()
        item['request_num']=request_num.replace(u"人","")
        item['description']=dr.sub('',detail.xpath('//div[contains(@class,"jz-d-info")]').extract_first(default='not-find')).strip()
        item['url']=response.url

        remen=detail.xpath('//div[contains(@class,"jz-d-title")]/div/h2/i[contains(@class,"word-re-ico")]').extract_first(default='')
        if remen<>'':
            item['tag_type']="remen"

        huobao=detail.xpath('//div[contains(@class,"jz-d-title")]/div/h2/i[contains(@class,"word-huo-ico")]').extract_first(default='')
        if huobao<>'':
            item['tag_type']="huobao"

        zhipin=detail.xpath('//div[contains(@class,"jz-d-title")]/div/h2/i[contains(@class,"word-zhi-ico")]').extract_first(default='')
        if zhipin<>'':
            item['tag_type']="zhipin"

        youxian=detail.xpath('//div[contains(@class,"jz-d-title")]/div/h2/i[contains(@class,"word-you-ico")]').extract_first(default='')
        if youxian<>'':
            item['tag_type']="youxian"

        tag=detail.xpath('//div[contains(@class,"jz-d-title")]/div/h2/i').extract_first(default='no')
        if tag=='no':
            item['tag_type']='no'

        yield item
