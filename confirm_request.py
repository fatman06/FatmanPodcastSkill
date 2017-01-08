from __future__ import print_function

import json
import urllib2
import re
from xml.etree import ElementTree as etree
from podcast import *

def get_confirm_answer(confirm):
	if re.search(r'(?i)yes|yeah|oh kay|ok|sure|ya',confirm):
		answer = "YES"
	else:
		anser = "NO"
	return answer

def confirmation_play_recent_podcast(session_attr):
	print(session)

def handle_confirm_request(intent,session):
	slots = intent_request['slots']
	confirm = slots["confirm"]
	if 'prevIntent' in session["attributes"]:
		prevIntent = session["attributes"]["prevIntent"]
		if prevIntent == "ListRecentPodcast":
			response = confirmation_play_recent_podcast(session["attributes"])
			return response
		else:
			print("Handle Exception")
	else:
		print("Handle Exception")
