# -*- coding: utf-8 -*-

import scrapy

class Dpsk12OrgItem(scrapy.Item):
    url = scrapy.Field()
    html = scrapy.Field()
