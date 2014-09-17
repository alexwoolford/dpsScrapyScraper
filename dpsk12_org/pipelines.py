# -*- coding: utf-8 -*-

import json

class Dpsk12OrgPipeline(object):
    def __init__(self):
        self.file = open('dpsk12_org.json', 'wb')
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
