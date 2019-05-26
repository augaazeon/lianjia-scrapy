# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


# class LianjiaItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class AgentInfo(Item):
    area = Field()#地区
    agent_name = Field()#
    agent_url = Field()#经纪人信息的url
    agent_tag = Field()#经纪人标签
    agent_tel = Field()#电话
    seniority = Field()#服务年限
    capability = Field()#能力
    achievement = Field()#成绩
    plate = Field()#板块
    plot = Field()#小区
