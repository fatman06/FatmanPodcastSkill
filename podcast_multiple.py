from __future__ import print_function

# encoding: utf-8
import json
import urllib2
import re
from xml.etree import ElementTree as etree
from podcast_map import *
import traceback
import alexa as alexa
import uuid
import time
import random
from podcast import *
from lambda_function import *
from datetime import *
import boto3


def multiple_recent_podcast_stream(podcast,reqtype,prev=None):

    #'http://feeds.feedburner.com/DougLovesMovies'
    stream = podcast["stream"]
    podtrac = False
    redirect = False

    if 'podtrac' in podcast:
    	podtrac = True
    if 'redirect' in podcast:
    	redirect = True

    try:
		item = get_item_streams(stream)
		url = ""
		reddit_feed=[]
		if reqtype == "Random":
			print("rando")
			return return_rando_object(item,redirect,podtrac,prev)
		if reqtype == "Serial":
			print("serial")
			return return_next_episode(item,prev,redirect,podtrac)
    except: 
    	return {"url":"","title":"","description":"","index":0}
        e = 0

def return_next_episode(item,index=0,redirect=False,podtrac=False):
	url = ""
	orig_url = ""
	desc = ""
	title = ""
	duration = 0
	next_index = 0

	if (len(item) -1) > index[-1]:
		try:
			next_index = index[-1]+1
			entry = item[next_index]
			orig_url = entry.find('enclosure').attrib['url']
			url = orig_url.replace('http:', 'https:')
			duration = 0
			if entry.find('description') is not None:
				desc = cleanhtml(cleanCDATA(entry.find('description').text.strip()))
			title = entry.find('title').text.strip()
		except:
			e = 1

	if redirect and orig_url != "":
		response = urllib2.urlopen(orig_url)
		url = response.geturl().replace("http:","https:").replace("hwcdn.libsyn.com","secure-hwcdn.libsyn.com").replace("ec.libsyn.com","secure-hwcdn.libsyn.com")
	elif podtrac and orig_url != "":
		url = "https://www.podtrac.com/pts/redirect.mp3/{}".format(orig_url.replace("www.podtrac.com/pts/redirect.mp3/","").replace("https://","http://"))
	return {"url": url, "description": desc, "title" : title,"duration":duration,"index":next_index}



def return_rando_object(item,redirect=False,podtrac=False,prev=None,specific=None):
	url = ""
	orig_url = ""
	desc = ""
	title = ""
	duration = 0
	index = 0

	for attempt in range(10):
		total_items = len(item) - 1 
		rando_num = random.randint(0,total_items)
		if prev is not None:
			s = set(prev)
			if rando_num in s:
				continue
			if len(prev) > 10:
				break

		index = rando_num
		try: 
			entry = item[rando_num]
			orig_url = entry.find('enclosure').attrib['url']
			url = orig_url.replace('http:', 'https:')
			try:
				duration = int(entry.find('enclosure').attrib['length'])
			except KeyError:
				duration = 0
			except ValueError:
				duration = 0

			if entry.find('description') is not None:
				desc = cleanhtml(cleanCDATA(entry.find('description').text.strip()))
			title = entry.find('title').text.strip()
			if re.search(r'(?i)mp3',url):
				break
			else: 
				continue
		except AttributeError: 
			continue

	if redirect and orig_url != "":
		response = urllib2.urlopen(orig_url)
		url = response.geturl().replace("http:","https:").replace("hwcdn.libsyn.com","secure-hwcdn.libsyn.com").replace("ec.libsyn.com","secure-hwcdn.libsyn.com")
	elif podtrac and orig_url != "":
		url = "https://www.podtrac.com/pts/redirect.mp3/{}".format(orig_url.replace("www.podtrac.com/pts/redirect.mp3/","").replace("https://","http://"))
	return {"url": url, "description": desc, "title" : title,"duration":duration,"index":index}

def build_shuffle_response_new(pod,card,index):
    print("INDEX TYPE: {}".format(type(index)))
    if type(index) is list:
		ind = index
    else:
		ind = [index]

    token = {
    	"url": pod["url"],
    	"type": 2,
    	"index": ind,
    	"name" : pod["podcast"]
    }

    response =  {
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
                    "audioItem": {
                        "stream": {
                            "token": str(token),
                            "url": pod["url"],
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
       
    }
    if card is not None:
    	response["response"]["card"] = card["card"]

    return response

def intent_shuffle_stream(intent_request, session):

	slots = intent_request['slots']
	number = None
	ep_num = None
	shuffle = None
	if 'value' in slots["podcast"]:
		text = slots['podcast']['value'].lower()
	else:
		response = alexa.basic_response_reprompt("I was unable to hear a Podcast name. Which podcast would you like to listen to? ","Which Podcast would you like to listen to?",False)
		response["sessionAttributes"] = {"prevIntent" : "RecentPodcast"}
		return response

	podcast = find_podcast_regex(text)
	if podcast is not None:
		pod = multiple_recent_podcast_stream(podcast,"Random",None)
		print(pod)
		pod["image"] = podcast["image"]
		pod["podcast"] = podcast["name"]
		card = alexa.build_card(pod["title"],pod["description"],"Standard",pod["image"])
		response = build_shuffle_response_new(pod,card,pod["index"])
		return response
	else:
		print("handle intent_shuffle_stream exception")
		return alexa.basic_response_reprompt("I was unable to hear a Podcast name. Which podcast would you like to listen to? ","Which Podcast would you like to listen to?",False)

