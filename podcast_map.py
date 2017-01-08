from __future__ import print_function

import sys
import re
import json
from collections import OrderedDict

def podcast_map():
	date_file = open('./podcast.json')

	podcast_map = json.load(date_file, object_pairs_hook=OrderedDict)
	return podcast_map

def find_podcast_regex(text):
	response = None
	podcast = podcast_map()
	for k in podcast.keys():
		try:
			if re.search(re.compile(k),text):
				return  podcast[k]
				break
		except:
			n = 1
	return response	

