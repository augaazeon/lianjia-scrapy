# -*- coding: utf-8 -*-



import random
class RandomUserAgentMiddleware():
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Opera/8.0 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'
        ]

    def process_request(self,request,spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)

