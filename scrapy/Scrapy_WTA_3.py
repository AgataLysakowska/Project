# -*- coding: utf-8 -*-
import scrapy

class WTA(scrapy.Item):
    ranking = scrapy.Field()
    name = scrapy.Field()
    country = scrapy.Field()
    points = scrapy.Field()

class LinkSpider(scrapy.Spider):
#class LinkListsSpider(scrapy.Spider):
    name = 'WTA_3'
    allowed_domains = ['tennis.com/']
    start_urls = ['https://www.tennis.com/rankings/WTA/']


    def parse(self, response):
        # if bool = True it scrape only 99 trs, if bool=False it scrape every trs it found
        bool = True
        trs = response.xpath('//tbody/tr')
        if bool:
            for tr in trs[:99]:
                r = WTA()
                #get ranking
                rankings = tr.xpath('td[1]/text()').getall()

                #get name
                names = tr.xpath('td[3]/a/text()').getall()

                #get country
                countries_n = tr.xpath('td[4]/span/text()').getall()
                countries=[]
                #removing "\n"
                for element in countries_n:
                    countries.append(element.strip())

                # get points
                points = tr.xpath('td[5]/text()').getall()

                r['ranking'] = rankings
                r['name'] = names
                r['country'] = countries
                r['points'] = points

                yield r

        else:
            for tr in trs:
                r = WTA()
                # get ranking
                rankings = tr.xpath('td[1]/text()').getall()

                # get name
                names = tr.xpath('td[3]/a/text()').getall()

                # get country
                countries_n = tr.xpath('td[4]/span/text()').getall()
                countries = []
                # removing "\n"
                for element in countries_n:
                    countries.append(element.strip())

                # get points
                points = tr.xpath('td[5]/text()').getall()

                r['ranking'] = rankings
                r['name'] = names
                r['country'] = countries
                r['points'] = points

                yield r

