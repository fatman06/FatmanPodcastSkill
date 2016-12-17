from __future__ import print_function

# encoding: utf-8
import json
import urllib2
import re
from xml.etree import ElementTree as etree
from podcast_map import *
import traceback
import alexa as a
import uuid
import time
# --------------- Podcast Response -------------
def recent_podcast_stream(stream_url, guest=None,allfeed=None,stop=10,redirect=False):

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
			return return_guest_object(item, guest,redirect)
		elif allfeed is not None:
			return return_all_object(item)
		else:
			return return_recent_object(item,redirect)
	except urllib2.HTTPError:
		print("Stream Is Bad: " + stream_url)
		#traceback.print_exc()
		return {"url": "", "description": "","title" : ""}
	except urllib2.URLError:
		print("Stream is Bad: " + stream_url)
		return None
	except etree.ParseError:
		None

def return_guest_object(item, guest,redirect=False):

	url = ""
	orig_url = ""
	desc = ""
	title = ""
	duration = 0
	g = re.sub(re.compile("[',.!$&]"),"(.|)",guest).encode("utf8").replace(" ",".+")
	for entry in item:
	    # get description, url, and thumbnail
	    # print(entry.find('description').text)
	    #print(re.match(r'(?i)geoff tate', entry.find('description').text.strip()))
		#print(entry.find('description').text)
		if (entry.find('description') is not None):
			t = entry.find('description').text
		else:
			t = " "
			#print(t)

		#print(entry.find('description').text is None)
		#print (t)
		title = entry.find('title').text.strip()
		desc = ""
		url = ""
		try:
			if  re.search(r'(?i)' + g, t) or re.search(r'(?i)' + g, title):
				print("Found Guest: " + guest)
				orig_url = entry.find('enclosure').attrib['url']
				url = orig_url.replace('http:', 'https:')
				desc = cleanhtml(cleanCDATA(t))
				title = entry.find('title').text.strip()
				try:
					duration = int(entry.find('enclosure').attrib['length'])
				except KeyError:
					duration = 0
				except ValueError:
					duration = 0

				if re.search(r'(?i)mp3',url):
					break
				else:
					#print("Stream Does Not Have Mp3")
					continue
			else: 
				continue     
		except AttributeError:
			continue
	if redirect and orig_url != "":
		response = urllib2.urlopen(orig_url)
		url = response.geturl().replace("http:","https:")

	return {"url": url, "description": desc,"title" : title, "duration":duration}

def return_all_object(item,stop=10):
	i = 1
	t = []
	for entry in item:
		desc = ""
		url = ""
		title = ""
		try:
			if i > stop:
				break
			url = entry.find('enclosure').attrib['url'].replace('http:', 'https:')
			if entry.find('description') is not None:
				desc = cleanhtml(cleanCDATA(entry.find('description').text.strip().encode("utf8")))

			title = entry.find('title').text.strip()
			t.append({"url": url, "description": desc, "title" : title})
			i = i+1

		except AttributeError:
			continue

	return t
def return_recent_object(item,redirect=False):
	url = ""
	orig_url = ""
	desc = ""
	title = ""
	duration = 0
	for entry in item:
	    # get description, url, and thumbnail
	    # print(entry.find('description').text)

		desc = ""
		url = ""
		title = ""

		try:
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
			#traceback.print_exc()
			continue
		# 	break
		# except AttributeError:
		# 	continue
	if redirect and orig_url != "":
		response = urllib2.urlopen(orig_url)
		url = response.geturl().replace("http:","https:")
	return {"url": url, "description": desc, "title" : title,"duration":duration}


def build_response(url, card, offset=0):
    response =  {
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
                    "audioItem": {
                        "stream": {
                            "token": url,
                            "url": url,
                            "offsetInMilliseconds": offset
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

def no_podcast_response(podcast):
	return a.basic_response("Was Unabled to Locate A Podcast by the name: " + podcast)

def no_podcast_guest(podcast,guest):
	return a.basic_response("Was Unabled To Locate an episode of " + podcast + " featuring " + guest)

def get_offset_miliseconds(number,timeframe):
	num = int(number)
	if re.search(r'(?i)min',timeframe):
		n = 1000*60
	elif re.search(r'(?i)sec',timeframe):
		n = 1000
	elif re.search(r'(?i)hour',timeframe):
		n = 1000*60*60
	else: 
		n = 1000*60

	return (num * n)

def intent_recent_podcast(intent_request, session):

	slots = intent_request['slots']

	if 'value' in slots["podcast"]:
		text = slots['podcast']['value'].lower()
	else:
		response = a.basic_response_reprompt("I was unable to hear a Podcast name. Which podcast would you like to listen to? ","Which Podcast would you like to listen to?",False)
		response["sessionAttributes"] = {"prevIntent" : "RecentPodcast"}
		return response

	if 'value' in slots['guest']:
		guest = slots['guest']['value']
	elif 'value' in slots['keyword']:
		guest = slots['keyword']['value']
	else:
		guest = None

	podcast = find_podcast_regex(text)
	if podcast is not None:
		feed = podcast["stream"]
		if 'redirect' in podcast:
			redirect = True
		else:
			redirect = False

		pod = recent_podcast_stream(feed,guest,None,10,redirect)
		pod["image"] = podcast["image"]
		pod["podcast"] = podcast["name"]

		if guest is not None and pod["url"] == "":
			return no_podcast_guest(podcast["name"],guest)
		else:
			card = a.build_card(pod["title"],pod["description"],"Standard",pod["image"])
			if 'value' in slots['number'] and 'value' in slots['timeframe']:
				offset = get_offset_miliseconds(slots['number']["value"],slots['timeframe']["value"])
				if offset > pod["duration"] and pod["duration"] > 0:
					offset = 0
				response = build_response(pod["url"],card,offset)
			else:
				response = build_response(pod["url"],card)
			return response
	else: 
		response = no_podcast_response(text)
		return response

def intent_list_recent_podcast(intent_request,session):
	slots = intent_request['slots']
	if 'value' in slots['podcast']:
		text = intent_request['slots']['podcast']['value'].lower()
	else:
		response = a.basic_response_reprompt("I was unable to hear a Podcast name. What podcast would you like me to list? ","What podcast would you like me to list?",False)
		response["sessionAttributes"] = {"prevIntent" : "ListRecentPodcast"}
		return response

	podcast = find_podcast_regex(text)
	if podcast is not None:
		feed = podcast["stream"]
		pod = recent_podcast_stream(feed,None,True,10)
		speech = "Look at the Alexa App to see a list of recent episodes of " + podcast["name"]
		title = "Recent Episodes of: " + podcast["name"]
		response = a.build_response_with_card(speech,title,streamToList(pod),"Standard","")
		return response
	else:
		response = no_podcast_response(text)
		return response 


# ----------- HELPERS ----------------
def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>|&.*?;')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext
def cleanCDATA(text):
	cleanr = re.compile('<!\[CDATA\[.*?\]\]>')
	cleantext = re.sub(cleanr,'',text)
	return cleantext
def streamToList(lists):
	t = []
	for l in lists:
		t.append(l["title"])
	return "-" + ("\n-").join(t)

