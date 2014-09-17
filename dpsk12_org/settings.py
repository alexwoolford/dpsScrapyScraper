# -*- coding: utf-8 -*-

BOT_NAME = 'dpsk12_org'

SPIDER_MODULES = ['dpsk12_org.spiders']
NEWSPIDER_MODULE = 'dpsk12_org.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36'
DOWNLOAD_DELAY = 2.5
ITEM_PIPELINES = {
    'dpsk12_org.pipelines.Dpsk12OrgPipeline': 300,
}