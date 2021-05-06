# -*- coding: utf-8 -*-
import scrapy

class WTA(scrapy.Item):
    birthdate = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    plays = scrapy.Field()
    name = scrapy.Field()


class LinksSpider(scrapy.Spider):
    name = 'WTA_2'
    allowed_domains = ['tennis.com/']
    try:
        with open("WTA1.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        p = WTA()

        #scrap name
        try:
            #first name
            f_names = response.xpath('//span[@class="first-name"]/text()').get()
            #last name
            l_names = response.xpath('//span[@class="last-name"]/text()').get()
        except:
            f_names = []
            l_names = []
        #full name
        names = f_names + ' ' + l_names

        # scrap birthdate
        try:
            birthdates= response.xpath('//span[@class="player-birthdate"]/text()').getall()
        except:
            birthdates = []

        # scrap heights
        try:
            heights = response.xpath('//span[@class="player-height"]/text()[re:test(., "[0-9][0-9][0-9]")]').extract()
        except:
            heights = []

        # scrap weights
        try:
            weights = response.xpath('//span[@class="player-weight"]/text()[re:test(., "\([0-9][0-9]\s")]').extract()
        except:
            weights = []

        # scrap plays
        try:
            plays = response.xpath('//span[@class="player-plays"]/text()').getall()
        except:
            plays = []

        p['birthdate']= birthdates
        p['height'] = heights
        p['weight'] = weights
        p['plays'] = plays
        p['name'] = names

        yield p