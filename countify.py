#!/usr/bin/env python3

import glob
import pprint
import re
from collections import Counter

file_list = []
file_list += glob.iglob(r'fetch_page\gh_pages\*')
file_list += glob.iglob(r'fetch_page\lever_pages\*')
#pprint.pprint(file_list)
word_count = Counter()
for file_name in file_list:
    with open(file_name,'r') as f_in:
        w_arr = map(str.lower, re.sub('[\t\?\!\xa0\n\*]',' ',f_in.read().strip()).split(' '))
        w_set = set(w_arr)
        for w in w_set:
            word_count[w] += 1
        #print(w_arr)
pprint.pprint(word_count)