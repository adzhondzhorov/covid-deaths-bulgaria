import re
import scrapy
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess

BASE_URL = "https://www.mh.government.bg/"
PAGES_TO_SCRAPE = 40


class MhGovernmentBgSpider(scrapy.Spider):
    name = "MhGovernmentBgSpider"
    start_urls = [BASE_URL + "/bg/novini/aktualno/?page={}".format(i) for i in range(1, PAGES_TO_SCRAPE)]
    custom_settings = {
        "FEED_FORMAT": "csv",
        "FEED_URI": "data/deaths.csv"
    }
    
    def parse(self, response):
        selector = Selector(response)
        links = selector.xpath("//h2/a/@href").extract()
        for link in links:
            title = link.split("/")[-2]
            first_word = title.split("-")[0]
            if re.match("^([0-9]|[1-9][0-9])+$", first_word) is not None:
                yield scrapy.Request(BASE_URL + link, callback=self.parse_page)
        
    def parse_page(self, response):
        selector = Selector(response)
        date = selector.xpath("//time/@datetime").extract()[0][:10]
        text = selector.xpath("//div[@class=\"single_news\"]").extract()[0]
        for idx, stat in enumerate(re.findall("((мъж|жена) на [0-9]* г.,? [а-я, ]+)([,.;]|( и ))", text)):
            yield {"text": stat[0], "date": date, "idx": idx}
            
            
process = CrawlerProcess()

process.crawl(MhGovernmentBgSpider)
process.start()