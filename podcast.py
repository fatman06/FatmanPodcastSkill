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
import random
from lambda_function import *
from datetime import *
import boto3
# --------------- Podcast Response -------------
def recent_podcast_stream(stream_url, guest=None,allfeed=None,stop=10,redirect=False,podtrac=False,shuffle=None):

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
			return return_guest_object(item, guest,redirect,podtrac)
		elif allfeed is not None:
			return return_all_object(item)
		elif shuffle is not None:
			return return_rando_object(item,redirect,podtrac)
		else:
			return return_recent_object(item,redirect,podtrac)
	except urllib2.HTTPError:
		print("Stream Is Bad: " + stream_url)
		#traceback.print_exc()
		return {"url": "", "description": "","title" : ""}
	except urllib2.URLError:
		print("Stream is Bad: " + stream_url)
		return None
	except etree.ParseError:
		None

def return_guest_object(item, guest,redirect=False,podtrac=False):

	url = ""
	orig_url = ""
	desc = ""
	title = ""
	duration = 0
	g = re.sub(re.compile("['!$&]"),"(.|)",guest).encode("utf8").replace(" ",".+")
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
			if  re.search(re.compile("(?i){}".format(g)), str(t)) or re.search(re.compile("(?i){}".format(g)), str(title)):
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
		except UnicodeEncodeError:
			continue   
		except AttributeError:
			continue
	if redirect and orig_url != "":
		response = urllib2.urlopen(orig_url)
		url = response.geturl().replace("http:","https:").replace("//hwcdn.libsyn.com","//secure-hwcdn.libsyn.com").replace("ec.libsyn.com","secure-hwcdn.libsyn.com")
	elif podtrac and orig_url != "":
		url = "https://www.podtrac.com/pts/redirect.mp3/{}".format(orig_url.replace("www.podtrac.com/pts/redirect.mp3/","").replace("https://","http://"))

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

def return_recent_object(item,redirect=False,podtrac=False):
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
		url = response.geturl().replace("http:","https:").replace("hwcdn.libsyn.com","secure-hwcdn.libsyn.com").replace("ec.libsyn.com","secure-hwcdn.libsyn.com")
	elif podtrac and orig_url != "":
		url = "https://www.podtrac.com/pts/redirect.mp3/{}".format(orig_url.replace("www.podtrac.com/pts/redirect.mp3/","").replace("https://","http://"))
	return {"url": url, "description": desc, "title" : title,"duration":duration}

def return_rando_object(item,redirect=False,podtrac=False):
	url = ""
	orig_url = ""
	desc = ""
	title = ""
	duration = 0

	for attempt in range(5):
		total_items = len(item) - 1 
		rando_num = random.randint(0,total_items)
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
				desc = desc = cleanhtml(cleanCDATA(entry.find('description').text.strip()))
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
def update_no_podcast(podcast):
	client = boto3.resource('dynamodb',region_name='us-east-1')
	table = client.Table('pb_not_found')
	table.update_item(
		Key={
			'spoken_phrase' : podcast
		},
		UpdateExpression="ADD total_count :num",
		ExpressionAttributeValues = {
			":num" : 1
		},
		ReturnValues="NONE"
		)
def save_podcast_play(podcast):
	client = boto3.resource('dynamodb',region_name='us-east-1')
	table = client.Table('pb_play_totals')
	today = datetime.today()
	table.update_item(
		Key={
			'podcast_name' : podcast,
			'date_week' : today.strftime("%Y-%U")
		  },
		UpdateExpression="ADD total_count :num",
		ExpressionAttributeValues = {
			":num" : 1
		},
		ReturnValues="NONE"
		)
def no_podcast_response(podcast):
	update_no_podcast(podcast)
	return a.basic_response("Was Unable to Locate A Podcast by the name: " + podcast)

def no_podcast_guest(podcast,guest):
	return a.basic_response("Was Unable To Locate an episode of " + podcast + " featuring " + guest)

def no_podcast_number(podcast,epnum):
	return a.basic_response("Was Unable To Locate episode number " + str(int(epnum)) + " of " + podcast )

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
	number = None
	ep_num = None
	shuffle = None
	if 'value' in slots["podcast"]:
		text = slots['podcast']['value'].lower()
	else:
		response = a.basic_response_reprompt("I was unable to hear a Podcast name. Which podcast would you like to listen to? ","Which Podcast would you like to listen to?",False)
		response["sessionAttributes"] = {"prevIntent" : "RecentPodcast"}
		return response

	try:
		if 'value' in slots['guest']:
			guest = slots['guest']['value']
		elif 'value' in slots['keyword']:
			guest = slots['keyword']['value']
		else:
			guest = None

	except KeyError:
		guest = None
		e = 0

	if intent_request["name"] == "RecentPodcastEpisode":
		if 'value' in slots['epnumber']:
			guest = "(\\s|eps|#|episode|ep|^|E|Hr|-){}(\\s|-|:|,|\\.)".format(slots['epnumber']['value'])
			number = True
			ep_num = slots['epnumber']['value']
		else:
			guest = None
	elif intent_request["name"] == "RecentPodcastShuffle":
		shuffle = True

	podcast = find_podcast_regex(text)
	if podcast is not None:
		feed = podcast["stream"]
		if 'redirect' in podcast:
			redirect = True
		else:
			redirect = False
		if 'podtrac' in podcast:
			podtrac = True
		else:
			podtrac = False

		try:
			if session['user']['userId'] !="amzn1.ask.account.TEST" and getStage() == "Release":
				save_podcast_play(podcast["name"])
		except:
			r = 1

		pod = recent_podcast_stream(feed,guest,None,10,redirect,podtrac,shuffle)
		pod["image"] = podcast["image"]
		pod["podcast"] = podcast["name"]
		if guest is not None and pod["url"] == "" and number is None:
			return no_podcast_guest(podcast["name"],guest)
		elif guest is not None and pod["url"] == "" and number is not None:
			return no_podcast_number(podcast["name"],ep_num)
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
		try:
			speech = "The most recent episode of " + podcast["name"] + " is titled " + pod[0]["title"] + " ...Look at the Alexa App to see a list of recent episodes of " + podcast["name"] + " . . . Would you like to play the most recent episode now? "
			prompt = False
		except:
			speech = "Look at the Alexa App to see a list of recent episodes of " + podcast["name"]
			prompt = True

		title = "Recent Episodes of: " + podcast["name"]
		response = a.build_response_with_card(speech,title,streamToList(pod),"Standard","")
		response["sessionAttributes"] = {"stream" : pod[0]["url"],"title": pod[0]["title"],"name":podcast["name"],"prevIntent":"ListRecentPodcast" }
		response["response"]["shouldEndSession"] = prompt
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

