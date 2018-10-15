import scrapy
from airbnbscrape.items import AirbnbscrapeItem

class Airbnbscrape(scrapy.Spider):
    name = 'airbnbscrape'
    allowed_domains = ['airbnb.com']
    start_urls = ['www.airbnb.com/rooms/10411427?adults=1&children=0&infants=0&toddlers=0',
    'www.airbnb.com/rooms/18240098?adults=1&children=0&infants=0&toddlers=0',
    'www.airbnb.com/rooms/14942835?adults=1&children=0&infants=0&toddlers=0',
    'www.airbnb.com/rooms/plus/15289972?adults=1&children=0&infants=0&toddlers=0',
    'www.airbnb.com/rooms/16592678?adults=1&children=0&infants=0&toddlers=0',
    'www.airbnb.com/rooms/15486188?adults=1&children=0&infants=0&toddlers=0',
    'www.airbnb.com/rooms/25364757?adults=1&children=0&infants=0&toddlers=0',
    'www.airbnb.com/rooms/10252775?adults=1&children=0&infants=0&toddlers=0',
    'www.airbnb.com/rooms/14058443?adults=1&children=0&infants=0&toddlers=0',
    'www.airbnb.com/rooms/6957805?adults=1&children=0&infants=0&toddlers=0']

    def parse(self, response):
        pages = start_urls
        while len(pages)!=0:
            item = AirbnbscrapeItem()
            item['page_url'] =  pages[0].strip("[,]'")
            request = scrapy.Request(item['page_url'], callback = self.parseHouseData)
            request.meta['AirbnbscrapeItem'] = item
            del(pages[0])
            yield request

    def parseHouseData(self, response):
        item = response.meta['AirbnbscrapeItem']
        item = self.getHouseInfo(item, response)
        return item

    def getHouseInfo(self, item, response):
        item['page_name'] = response.xpath('_______').extract()
        return item
