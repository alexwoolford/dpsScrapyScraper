import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from dpsk12_org.items import Dpsk12OrgItem

class DenverPublicSchoolsK12Spider(CrawlSpider):
    name = 'dpsk12'
    allowed_domains = ['dpsk12.org']
    start_urls = ['http://www.dpsk12.org/']

    rules = (
        Rule(LinkExtractor(allow=(), deny=('safari')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = Dpsk12OrgItem()
        item['url'] = response.url
        item['html'] = response.body_as_unicode()
        return item