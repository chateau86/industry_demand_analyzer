#!/usr/bin/env python3
import scrapy
import re

LEVER_CPNY_REGEX = re.compile(r"lever\.co\/(?P<company>.*)\/(?P<pos>[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})")
GH_CPNY_REGEX = re.compile(r"greenhouse.io\/(?P<company>.*)\/jobs\/(?P<pos>\d*)")

from html.parser import HTMLParser
import html.entities

import job.spiders.job_spider

class GHJobSpider(job.spiders.job_spider.JobSpider):
    name = "gh_job"
    def __init__(self):
        super()
        self.cpny_regex = GH_CPNY_REGEX
        self.out_fname = "gh_pages/gh_{:}_{:}.txt"
        self.in_fname = "result_gh_clean.txt"
        self.body_xpath = '//div[@id="content"]'
        
class LeverJobSpider(job.spiders.job_spider.JobSpider):
    name = "lever_job"
    def __init__(self):
        super()
        self.cpny_regex = LEVER_CPNY_REGEX
        self.out_fname = "lever_pages/lever_{:}_{:}.txt"
        self.in_fname = "result_lever_clean.txt"
        self.body_xpath = '//html/body/div[2]/div/div[2]'
        
        