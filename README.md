DPS Scrapy Scraper
==================

This scraper, given a start URL, would crawl all the pages within the domain and store the HTML as JSON in a file for subsequent processing (as opposed to parsing in real-time, which is preferable you're confident that the parser will extract exactly the right data elements a priori).

Parsing postponement provides flexibility and resilience. The data can be collected and uses be discovered: no need to re-crawl in the event some interesting data element wasn't captured as the page requests were made.

To run the scraper:

    scrapy crawl dpsk12

The HTML would get captured in file containing JSON objects, one object per page per line, e.g.:

    {'url': 'http://....'}
    {'url': 'http://....'}

This file can subsequently be parsed on a cluster.
