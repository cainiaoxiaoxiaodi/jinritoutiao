# -*- coding: utf-8 -*-
from pprint import pprint

import scrapy
import json
import time

import execjs


class TtSpider(scrapy.Spider):
    name = 'tt'
    allowed_domains = ['www.toutiao.com']
    start_urls = [
        'https://www.toutiao.com/api/pc/feed/?category=news_tech&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1E51BCB7A4DADB&cp=5BBA5DFA2D4B3E1&_signature=YK0XGgAAOxuFG9OrNtu0wWCtFw']

    def parse(self, response):
        item = {}
        # print(response.text)
        data = response.text
        new_data = json.loads(data)
        # print(new_data)
        # item['data'] = new_data['data']
        data_list = new_data['data']
        for i in data_list:
            url = 'https://www.toutiao.com/' + i['source_url']  # 新闻详情页url
            if len(url) < 30:
                yield scrapy.Request(url, callback=self.details, dont_filter=True)

    def details(self, response):
        print(response.text)

