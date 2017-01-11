from __future__ import print_function
from alexa import *
from podcast import *
from podcast_multiple import *
from podcast_map import *
import ast

# Token Types:
# 1 - Single Stream
# 2 - Shuffle of podcast
# 3 - Streams in Order Newest to Oldest

def build_enqueue_response(newstream,prevtoken,ttype=2):
	prev_index = list(prevtoken["index"])
	prev_index.append(newstream["index"])
	new_token = {
    	"url": newstream["url"],
    	"type": ttype,
    	"index": prev_index,
    	"name" : newstream["podcast"]
    }
	response = {
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "ENQUEUE",
                    "audioItem": {
                        "stream": {
                            "token": str(new_token),
                            "expectedPreviousToken" : str(prevtoken),
                            "url": newstream["url"],
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
       
    }
	return response
def on_playback_next_handling(request,context): 
	token = parseToken(context["AudioPlayer"]["token"])
	if token["type"] == 1:
		print("Token Type One Do Nothing")
	elif token["type"] == 2:
		podcast = find_podcast_regex(token["name"])
		if podcast is not None: 
			pod = multiple_recent_podcast_stream(podcast,"Random",token["index"])
			pod["podcast"] = podcast["name"]
			token["index"].append(pod["index"])
			response = build_shuffle_response_new(pod,None,token["index"])
		else:
			response = {}
		return response
	elif token["type"] == 3:
		podcast = find_podcast_regex(token["name"])
		if podcast is not None:
			pod = multiple_recent_podcast_stream(podcast,"Serial",token["index"])
			pod["podcast"] = podcast["name"]
			token["index"].append(pod["index"])
			return build_response(pod["url"],None,0,token)
		else:
			return ""
	else:
		return ""


def on_playback_started_handling(request,context):
	token = parseToken(context["AudioPlayer"]["token"])
	if token["type"] == 1: 
		print("Token Type 1 Do Nothing")
	elif token["type"] == 2:
		podcast  = find_podcast_regex(token["name"])
		if podcast is not None:
			pod = multiple_recent_podcast_stream(podcast,"Random",token["index"])
			if pod["url"] != "":
				pod["podcast"] = podcast["name"]
				response = build_enqueue_response(pod,token,2)
			else:
				response = ""
			return response
		else:
			return ""
	elif token["type"] == 3:
		podcast = find_podcast_regex(token["name"])
		if podcast is not None:
			pod = multiple_recent_podcast_stream(podcast,"Serial",token["index"])
			if pod["url"] != "":
				pod["podcast"] = podcast["name"]
				return build_enqueue_response(pod,token,3)
			else:
				return ""
		else:
			return ""
	else:
		print("Hmmm")

def on_media_direction_handling(direction,context,intent):
	if direction == "rewind":
		n = -1
	else: 
		n = 1
	token = parseToken(context["AudioPlayer"]["token"])
	if 'value' in intent["slots"]["number"] and 'value' in intent["slots"]["timeframe"]:
		offset = get_offset_miliseconds(intent["slots"]["number"]["value"],intent["slots"]["timeframe"]["value"])
	else:
		offset = get_offset_miliseconds(30,"seconds") * n
	new_offset = (context["AudioPlayer"]["offsetInMilliseconds"] + offset)
	return build_response(token["url"], None, new_offset,token)


