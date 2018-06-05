#!/usr/bin/env python3
import scrapy
import re

LEVER_CPNY_REGEX = re.compile(r"lever\.co\/(?P<company>.*)\/(?P<pos>[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})")
GH_CPNY_REGEX = re.compile(r"greenhouse.io\/(?P<company>.*)\/jobs\/(?P<pos>\d*)")

from html.parser import HTMLParser
import html.entities

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.result = [ ]

    def handle_data(self, d):
        self.result.append(d)

    def handle_charref(self, number):
        codepoint = int(number[1:], 16) if number[0] in (u'x', u'X') else int(number)
        self.result.append(unichr(codepoint))

    def handle_entityref(self, name):
        codepoint = html.entities.name2codepoint[name]
        self.result.append(unichr(codepoint))

    def get_text(self):
        return u''.join(self.result)

def html_to_text(html):
    s = HTMLTextExtractor()
    s.feed(html)
    return s.get_text()


class GHJobSpider(scrapy.Spider):
    name = "gh_job"

    def start_requests(self):
        f_in = open('result_gh_clean.txt','r')
        #urls = [
        #    'https://boards.greenhouse.io/khanacademy/jobs/15827',
        #]
        #for url in urls:
        #    yield scrapy.Request(url=url, callback=self.parse)
        for line in f_in:
            if line.strip() != "":
                yield scrapy.Request(url=line.strip(), callback=self.parse)

    def parse(self, response):
        url_split = GH_CPNY_REGEX.search(response.url)
        if url_split is None:
            self.log('----Error at {:}'.format(response.url))
            return
        cpny = url_split.group('company')
        pos = url_split.group('pos')
        
        #filename = 'gh_pages/gh_{:}_{:}_raw.htm'.format(cpny, pos)
        #with open(filename, 'wb') as f:
        #    f.write(response.body) #  change this to just body text
            
        filename = 'gh_pages/gh_{:}_{:}.txt'.format(cpny, pos)
        with open(filename, 'w') as f:
            txt_response = response.xpath('//div[@id="content"]').extract_first()
            txt_response = re.sub(r'&nbsp;', ' ', txt_response)
            txt_response = html_to_text(txt_response)
            txt_response = re.sub(r'[.,:;()/\"\\]', ' ', txt_response)
            f.write(txt_response) #  change this to just body text
        self.log('Saved file %s' % filename)