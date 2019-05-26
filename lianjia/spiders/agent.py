# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from lianjia.items import AgentInfo
from urllib.parse import urljoin
from lianjia.items import AgentInfo
import json
# from bs4 import BeautifulSoup
class AgentSpider(Spider):
    name = "agent"
    allowed_domains = ["lianjia.com"]
    start_urls = ['https://www.lianjia.com/city/']


    def parse(self, response):#主要得到各地区的url入口，和对应地区名字。加上jingjiren/，构成经纪人页面的url，发送请求Request
        info_items = response.xpath('//ul[@class="city_list_ul"]//ul//a')
        for info_item in info_items:
            url = info_item.xpath('./@href').extract_first()
            area = info_item.xpath('./text()').extract_first()
            yield Request(urljoin(url,"jingjiren/"),meta={"area":area},callback=self.get_agent_item)

    def get_agent_item(self,response):#各地区的经纪人列表页的翻页，page-div是加载而成，常用翻页不行。需要for in构建url，再进行Request
        area = response.meta['area']
        # 这里的页码是有JavaScript渲染的
        page_info = response.xpath('//div[contains(@class,"page-box")]/@page-data').extract_first()#页码信息，总页数，当前页；
        if page_info:
            page = json.loads(page_info)
            total_page = page['totalPage']
            for page_num in range(1,total_page+1):
                url = response.url + 'pg' + str(page_num)
                yield Request(url=url,meta={"area":area},callback=self.parse_agent_item)

    def parse_agent_item(self,response):#解析各地区的经纪人列表页的经纪人信息页面的url
        area = response.meta['area']
        for url in response.xpath('//div[@class="agent-name"]//a/@href').extract():
            yield Request(url,meta={"area":area},callback=self.parse_agent_info)

    def parse_agent_info(self,response):
        # print("agent-url", response.url)  # 经纪人的信息页面
        item = AgentInfo()
        item['agent_url'] = response.url
        item['agent_name'] = response.xpath('//span[@class="agent-name"]/text()').extract_first()
        item['agent_tag'] = response.xpath('//span[@class="pub-tag"]/text()').extract_first()
        item['agent_tel']  = response.xpath('//span[@class="agent-tel"]/text()').extract_first()
        item['seniority'] = response.xpath('//ul[@class="info-list"]/li[1]/span[@class="info-item-value"]//text()').extract_first()
        item['plate'] = response.xpath('//ul[@class="info-list"]/li[2]/span[@class="info-item-value"]//text()').extract_first()
        item['achievement'] = response.xpath('//ul[@class="info-list"]/li[3]/span[@class="info-item-value"]//text()').extract_first()
        item['plot'] = response.xpath('//ul[@class="info-list"]/li[4]/span[@class="info-item-value"]//text()').extract_first()
        item['capability'] = response.xpath('//ul[@class="info-list"]/li[5]/span[@class="info-item-value"]//text()').extract_first()
        item['area'] = response.meta['area']
        yield item
