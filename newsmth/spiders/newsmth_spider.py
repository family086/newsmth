# -*- coding: utf-8 -*-
import logging
import os
import sys
import time

import scrapy

class NewsmthSpider(scrapy.Spider):
    name = 'newsmth'
    allowed_domains = ['newsmth.net']
    start_urls = ['http://www.newsmth.net/nForum/rss/topten']

    def parse(self, response):
        crawl_path = "./crawl"
        filename = response.url.split("/")[-1]
        #1.crawl_path
        if not os.path.exists(crawl_path):
            command = "mkdir -p %s" % (crawl_path)
            os.system(command)
        title = response.selector.xpath('//item/title/text()').extract()
        for i in xrange(len(title)):
            logging.info("title: %s" % (title[i].encode("gb18030")))
        #2.filename
        time_stamp = time.strftime("%Y%m%d", time.localtime())
        filename = crawl_path + "/" + filename + "." + time_stamp
        with open(filename, "wb") as f:
            f.write(response.body)
        pass
