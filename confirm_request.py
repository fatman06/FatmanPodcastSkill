from __future__ import print_function

import json
import urllib2
import re
from xml.etree import ElementTree as etree
from podcast import *
import alexa as alexa

def get_confirm_answer(confirm):
	print("Confirming Answer")
	if re.search(r'(?i)yes|yeah|oh kay|ok|sure|ya',confirm):
		answer = "YES"
	else:
		answer = "NO"
	return answer

def confirmation_play_recent_podcast(session_attr):
	try:
		print("Send Most Recent Podcast")
		token = {
			"url" : session_attr["stream"],
			"name" : session_attr["name"],
			"index": [0],
			"type" : 3
		}
		response = build_response(session_attr["stream"],None,0,token)
		print(session)
	except:
		print("Handle Exception confirmation_play_recent_podcast")
		response = alexa.basic_response("Something unexpected went wrong, please try again")
	return response

def handle_confirm_request(intent,session):
	slots = intent['slots']
	confirm = slots["confirm"]["value"]
	confirm_answer = get_confirm_answer(confirm)
	if 'attributes' in session:
		if 'prevIntent' in session["attributes"]:
			prevIntent = session["attributes"]["prevIntent"]
			if prevIntent == "ListRecentPodcast":
				if confirm_answer == "YES":
					response = confirmation_play_recent_podcast(session["attributes"])
					return response 
				else:
					return alexa.basic_response("Ok")
			else:
				print("Handle Exception handle_confirm_request::PrevIntent YES")
				return alexa.basic_response("I am unable to Handle Yes or No answers from this point in the skill. You can say Ask Pod Buddy to play and the name of a podcast to get started")

		else:
			print("Handle Exception handle_confirm_request::PrevIntent NO")
			return alexa.basic_response("I am unable to Handle Yes or No answers from this point in the skill. You can say Ask Pod Buddy to play and the name of a podcast to get started")
	else:
		print("Handled Exception handle_confirm_request NO Attributes")
		return alexa.basic_response("I am unable to Handle Yes or No answers from this point in the skill. You can say Ask Pod Buddy to play and the name of a podcast to get started")
