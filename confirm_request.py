from __future__ import print_function

import json
import urllib2
import re
from xml.etree import ElementTree as etree
from podcast import *
import alexa as a

def get_confirm_answer(confirm):
	print("Confirming Answer")
	if re.search(r'(?i)yes|yeah|oh kay|ok|sure|ya',confirm):
		answer = "YES"
	else:
		anser = "NO"
	return answer

def confirmation_play_recent_podcast(session_attr):
	try:
		print("Send Most Recent Podcast")
		response = build_response(session_attr["stream"],None)
		print(session)
	except:
		print("Handle Exception confirmation_play_recent_podcast")
	return response

def handle_confirm_request(intent,session):
	slots = intent['slots']
	confirm = slots["confirm"]["value"]
	confirm_answer = get_confirm_answer(confirm)
	if 'prevIntent' in session["attributes"]:
		prevIntent = session["attributes"]["prevIntent"]
		if prevIntent == "ListRecentPodcast":
			if confirm_answer == "YES":
				response = confirmation_play_recent_podcast(session["attributes"])
				return response 
			else:
				response = a.on_session_ended(intent,session)
		else:
			print("Handle Exception handle_confirm_request::PrevIntent YES")
	else:
		print("Handle Exception handle_confirm_request::PrevIntent NO")
