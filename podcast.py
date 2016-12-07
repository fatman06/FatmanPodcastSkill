from __future__ import print_function

import json
import urllib2
import re
from xml.etree import ElementTree as etree
from podcast_map import *
import traceback
import alexa as a
# --------------- Podcast Response -------------
def recent_podcast_stream(stream_url, guest=None):

    #'http://feeds.feedburner.com/DougLovesMovies'
	try:
		req = urllib2.Request(stream_url, headers={'User-Agent' : "Magic Browser"}) 
		reddit_file = urllib2.urlopen(req)
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
	except urllib2.HTTPError:
		print("Stream Is Bad: " + stream_url)
		#traceback.print_exc()
		return {"url": "", "description": "","title" : ""}
	except urllib2.URLError:
		print("Stream is Bad: " + stream_url)
		return None
	except etree.ParseError:
		None

def return_guest_object(item, guest):

	url = ""
	desc = ""
	title = ""
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
				desc = cleanhtml(cleanCDATA(entry.find('description').text.strip()))
				title = entry.find('title').text.strip()
				if re.search(r'(?i)mp3',url):
					break
				elif re.search(r'(?i)(mp4|m4v)',url):
					#print("this has a video in it")
					continue
				else:
					#print("Stream Does Not Have Mp3")
					continue
			else: 
				continue     
		except AttributeError:
			continue

	return {"url": url, "description": desc,"title" : title}

def return_recent_object(item):
	url = ""
	desc = ""
	title = ""
	for entry in item:
	    # get description, url, and thumbnail
	    # print(entry.find('description').text)

		desc = ""
		url = ""
		title = ""

		try:
		    url = entry.find('enclosure').attrib['url'].replace('http:', 'https:')
		    desc = cleanhtml(cleanCDATA(entry.find('description').text.strip()))
		    title = entry.find('title').text.strip()
		    if re.search(r'(?i)mp3',url):
		    	break
		    elif re.search(r'(?i)(mp4|m4v|m4a)',url):
		    	continue
		    else:
		    	continue
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

def no_podcast_response(podcast):
	return a.basic_response("Was Unabled to Locate A Podcast by the name: " + podcast)

def no_podcast_guest(podcast,guest):
	return a.basic_response("Was Unabled To Locate an episode of " + podcast + " featuring " + guest)

def intent_recent_podcast(intent_request, session):
	text = intent_request['slots']['podcast']['value'].lower()
	try:
		guest = intent_request['slots']['guest']['value']
	except KeyError:
		guest = None

	podcast = find_podcast_regex(text)
	if podcast is not None:
		feed = podcast["stream"]
		pod = recent_podcast_stream(feed,guest)
		pod["image"] = podcast["image"]
		pod["podcast"] = podcast["name"]

		if guest is not None and pod["url"] == "":
			return no_podcast_guest(podcast["name"],guest)
		else:
			card = a.build_card(pod["title"],pod["description"],"Standard",pod["image"])
			response = build_response(pod["url"],card)
			return response
	else: 
		response = no_podcast_response(text)
		return response

# ----------- HELPERS ----------------
def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext
def cleanCDATA(text):
	cleanr = re.compile('<!\[CDATA\[.*?\]\]>')
	cleantext = re.sub(cleanr,'',text)
	return cleantext
