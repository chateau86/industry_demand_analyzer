#!/usr/bin/env python3

import glob
import pprint

pprint.pprint(list(glob.iglob(r'fetch_page\gh_pages\*')))
pprint.pprint(list(glob.iglob(r'fetch_page\lever_pages\*')))
