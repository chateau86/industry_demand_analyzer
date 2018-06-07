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
bigram_count = Counter()
for file_name in file_list:
    with open(file_name,'r') as f_in:
        w_arr = map(str.lower, re.sub('[\t\?\!\xa0\n\*]',' ',f_in.read().strip()).split(' '))
        w_arr = list(filter(None, w_arr))
        w_set = set(w_arr)
        for w in w_set:
            word_count[w] += 1
            
        for ind in range(len(w_arr)-1):
            bigram_count[(w_arr[ind],w_arr[ind+1])] += 1
        #print(w_arr)
f_out = open('count.txt','w')
for w, c in word_count.most_common(len(word_count)):
    f_out.write('{:} {:}\n'.format(w,c))
f_out = open('count_bigram.txt','w')
for w, c in bigram_count.most_common(len(bigram_count)):
    f_out.write('{:} {:}\n'.format(w,c))