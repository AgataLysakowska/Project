# -*- coding: utf-8 -*-
import scrapy

class WTA(scrapy.Item):
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'WTA_1'
    allowed_domains = ['tennis.com/']
    start_urls = ['https://www.tennis.com/rankings/WTA/']


#scrap links to the players pages
    def parse(self, response):
        #if bool = True it scrape only 99 links, if bool=False it scrape every link found in trs
        bool = True
        trs = response.xpath('//tbody/tr')
        if bool:
            for tr in trs[:99]:
                r = WTA()

                #links
                xpath = 'td[3]/a//@href'
                href = tr.xpath(xpath).get()
                try:
                    link = 'https://www.tennis.com' + href + 'stats/'
                except:
                    pass
                #print(link)

                r['link'] = link

                yield r

        else:

            for tr in trs:
                r = WTA()

                # links
                xpath = 'td[3]/a//@href'
                href = tr.xpath(xpath).get()
                try:
                    link = 'https://www.tennis.com' + href + 'stats/'
                except:
                    pass
                #print(link)

                r['link'] = link

                yield r


