DPS Scrapy Scraper
==================

This scraper, given a start URL, would crawl all the pages within the domain and store the HTML as JSON in a file for subsequent processing (as opposed to parsing in real-time, which is preferable if the use-case is known a priori).

Parsing postponement provides flexibility and resilience. The data can be collected and uses be discovered: no need to re-crawl in the event some interesting data element wasn't captured by the built-in parser.

    scrapy crawl 
