from __future__ import print_function
version = "0.4.0"
print("Pod Buddy Version " + version + " - Release")

import json
import urllib2
import re
from xml.etree import ElementTree as etree
from alexa import *
from podcast import *
from podcast_map import *

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def my_logging_handler(event, context):
    print(event)
    #logger.info('got event{}'.format(event))
    return True

def getVersion():
	return version

# --------------- Main handler ------------------
def handle_request_event(event,context):
	if event['request']['type'] == "LaunchRequest":
	    return on_launch(event['request'], event['session'])
	elif event['request']['type'] == "IntentRequest":
	    return on_intent(event, event['session'])
	elif event['request']['type'] == "SessionEndedRequest":
	    return on_session_ended(event['request'], event['session'])
	else:
		print("Unknown Intent Option")
		return on_session_ended(event['request'], context)

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    #print("event.session.application.applicationId=" +
          #event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    #my_logging_handler(event,context)

    #url = recent_podcast_stream(event['request'], event['session'])
    try:
	    if (event['session']['application']['applicationId'] !=
	            "amzn1.ask.skill.7d942caa-da0f-45e5-81c8-08479081e33a"):
	        raise ValueError("Invalid Application ID")
    except KeyError: 
        x = 1
    try:
	    if event['session']["new"]:
	    	return handle_request_event(event,context)
	    else:
	    	try:
				#print("Not New: {}".format(event['session']["attributes"]))
				if 'session' not in event:
					return handle_request_event(event,context)
				elif event['session']["attributes"]["prevIntent"] == "help":
				   return handle_request_event(event,context)
				elif event['session']['attributes']['prevIntent'] == "ListRecentPodcast":
					event["request"]["intent"]["name"] = "ListRecentPodcast"
					return handle_request_event(event,context)
				else:
					return handle_request_event(event,context)

	        except KeyError:
				return on_session_ended(event['request'], context)
    except KeyError:
		return handle_request_event(event,context)

    
    #return build_response(pod["url"],card)