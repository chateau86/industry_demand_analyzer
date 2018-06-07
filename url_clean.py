#!/usr/bin/env python3

import sys
import re
import urllib.parse

YAHOO_URL_REGEX = re.compile(r"\/RU=(?P<url>\S*)\/RK")
LEVER_CPNY_REGEX = re.compile(r"lever\.co\/(?P<company>.*)\/(?P<pos>[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})")
GH_CPNY_REGEX = re.compile(r"greenhouse.io\/(?P<company>.*)\/jobs\/(?P<pos>\d*)")
SR_CPNY_REGEX = re.compile(r"smartrecruiters\.com\/(?P<company>.*)\/(?P<pos>[^?\n]*)")

def clean_lever_url(url_decode):  # return (cpny, pos_id) tuple or None if malformed
    if url_decoded is None:
        return None
    url_split = LEVER_CPNY_REGEX.search(url_decoded)
    if url_split is None:
        return None
    cpny = url_split.group('company')
    pos = url_split.group('pos')
    #print((cpny, pos))
    return "https://jobs.lever.co/{:}/{:}/".format(cpny, pos)
    
def clean_gh_url(url_decoded):
    if url_decoded is None:
        return None
    url_split = GH_CPNY_REGEX.search(url_decoded)
    if url_split is None:
        return None
    cpny = url_split.group('company')
    pos = url_split.group('pos')
    #print((cpny, pos))
    return "https://boards.greenhouse.io/{:}/jobs/{:}".format(cpny, pos)

def clean_sr_url(url_decoded):
    if url_decoded is None:
        return None
    url_split = SR_CPNY_REGEX.search(url_decoded)
    if url_split is None:
        return None
    cpny = url_split.group('company')
    pos = url_split.group('pos')
    #print((cpny, pos))
    return "https://www.smartrecruiters.com/{:}/{:}".format(cpny, pos)
        
def decode_yahoo_url(url_encoded):
    url_encoded = YAHOO_URL_REGEX.search(line)
    if url_encoded is None:
        return None
    url_encoded = url_encoded.group('url')
    url_decoded = urllib.parse.unquote(url_encoded)
    return url_decoded
  
if __name__ == '__main__':
    f_name = sys.argv[1]
    f_in = open(f_name,'r')  
    for line in f_in:
        #URL regex = r"\/RU=(?P<url>\S*)\/RK"
        #then decode

        #url_decoded = decode_yahoo_url(line)
        url_decoded = line.strip()
        if 'lever' in f_name:
            decoded_tuple = clean_lever_url(url_decoded)
        elif 'gh' in f_name:
            decoded_tuple = clean_gh_url(url_decoded)
        elif 'sr' in f_name:
            decoded_tuple = clean_sr_url(url_decoded)
            
        if decoded_tuple is not None:
            #print(url_decoded)
            print(decoded_tuple)