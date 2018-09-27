# -*- coding: utf-8 -*-
import scrapy


class TtSpider(scrapy.Spider):
    name = 'tt'
    allowed_domains = ['www.toutiao.com']
    start_urls = ['http://www.toutiao.com/']

    def parse(self, response):
        pass
