from __future__ import print_function

import json
import urllib2
import re
from xml.etree import ElementTree as etree
from podcast_map import *
import alexa as a
# --------------- Podcast Response -------------
def recent_podcast_stream(stream_url, guest=None):

    #'http://feeds.feedburner.com/DougLovesMovies'
    reddit_file = urllib2.urlopen(stream_url)
    reddit_data = reddit_file.read()
    reddit_file.close()
    # entire feed
    reddit_root = etree.fromstring(reddit_data)
    item = reddit_root.findall('channel/item')
    url = ""
    reddit_feed=[]

    if guest is not None:
    	return return_guest_object(item, guest)
    else:
    	return return_recent_object(item)

def return_guest_object(item, guest):

	url = ""
	desc = ""
	for entry in item:
	    # get description, url, and thumbnail
	    # print(entry.find('description').text)
	    #print(re.match(r'(?i)geoff tate', entry.find('description').text.strip()))
		t = entry.find('description').text.strip().lower()
		desc = ""
		url = ""
		title = ""
		try:
			if re.search(r'(?i)' + guest.lower(), t):
				print("Found Guest: " + guest)
				url = entry.find('enclosure').attrib['url'].replace('http:', 'https:')
				print(entry.find('description').text.strip())
				desc = cleanhtml(entry.find('description').text.strip())
				title = entry.find('title').text.strip()
				break
			else: 
				continue     
		except AttributeError:
			continue

	return {"url": url, "description": desc,"title" : title}

def return_recent_object(item):
	for entry in item:
	    # get description, url, and thumbnail
	    # print(entry.find('description').text)
		try:
		    url = entry.find('enclosure').attrib['url'].replace('http:', 'https:')
		    desc = cleanhtml(entry.find('description').text.strip())
		    title = entry.find('title').text.strip()
		    break
		except AttributeError:
			continue
		# 	break
		# except AttributeError:
		# 	continue

	return {"url": url, "description": desc, "title" : title}


def build_response(url, card):
    return {
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
                    "audioItem": {
                        "stream": {
                            "token": "12345",
                            "url": url,
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True,
            "card" : card["card"]
        }
       
    }

def intent_recent_podcast(intent_request, session):
	text = intent_request['slots']['podcast']['value'].lower()
	try:
		guest = intent_request['slots']['guest']['value']
	except KeyError:
		guest = None
		
	if re.search(r'(?i)doug loves movie',text):
		feed = podcast_map("dlm")
		pod = recent_podcast_stream(feed,guest)
		pod["image"] = podcast_img("dlm")
		pod["podcast"] = "dlm"

	elif re.search(r'(?i)(jericho|jerico)',text):
		feed = podcast_map("jericho")
		pod = recent_podcast_stream(feed,guest)
		pod["image"] = podcast_img("jericho")
		pod["podcast"] = "jericho"

	elif re.search(r'(?i)(stone cold)',text):
		feed = podcast_map("stonecold")
		pod = recent_podcast_stream(feed,guest)
		pod["image"] = podcast_img("stonecold")
		pod["podcast"] = "stonecold"

	elif re.search(r'(?i)(snap)',text):
		feed = podcast_map("snap")
		pod = recent_podcast_stream(feed,guest)
		pod["image"] = podcast_img("snap")
		pod["podcast"] = "snap"
	else:
		pod = {"url" : "","description":"","title":"","image": "","podcast" : False}
		card = {"card":{}}

	card = a.build_card(pod["title"],pod["description"],"Standard",pod["image"])
	response = build_response(pod["url"],card)
	response["sessionAttributes"] = pod
	return response

# ----------- HELPERS ----------------
def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

