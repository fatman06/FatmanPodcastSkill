from __future__ import print_function
version = "2.0.11"
stage = "Beta"
print("Pod Buddy Version " + version + " - " + stage)

import json
import urllib2
import re
from xml.etree import ElementTree as etree
from alexa import *
from podcast import *
from podcast_map import *
from podcast_audio_player import *
from voicelabs import VoiceInsights

import boto3

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def my_logging_handler(event, context):
    print(str(event))
    #logger.info('got event{}'.format(event))
    return True

def getVersion():
	return version

def getStage():
	return stage

# --------------- Main handler ------------------
def handle_request_event(event,context):
	if event['request']['type'] == "LaunchRequest":
	    return on_launch(event['request'], event['session'])
	elif event['request']['type'] == "IntentRequest":
		if 'context' in event:
			context = event['context']
		else:
			context = None

		return on_intent(event, event['session'],context)

	elif event['request']['type'] == "SessionEndedRequest":
	    return on_session_ended(event['request'], event['session'])
	elif event['request']['type'] == "AudioPlayer.PlaybackFailed":
		print(event)
	elif event['request']['type'] == "AudioPlayer.PlaybackNearlyFinished":
		return on_playback_started_handling(event["request"],event["context"])
	elif event['request']['type'] == "AudioPlayer.PlaybackStopped" or event['request']['type'] == "AudioPlayer.PlaybackStarted":
		print(event["context"])
		x = 1
	elif event['request']['type'] == "System.ExceptionEncountered":
		print("System.ExceptionEncountered: {}".format(event['request']))
	else:
		print("Unknown Intent Option: {}".format(event['request']['type']))
		return on_session_ended(event['request'], context)

def add_customer_ddb(customerID):
	client = boto3.resource('dynamodb',region_name='us-east-1')
	table = client.Table('pod_buddy_custid_total')
	table.update_item(
			Key={
				'customer_id' : customerID
			},
			UpdateExpression="ADD total_count :num",
			ExpressionAttributeValues = {
				":num" : 1
			},
			ReturnValues="NONE"
		)
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
    if getStage() == "Beta":
    	my_logging_handler(event,context)

    #url = recent_podcast_stream(event['request'], event['session'])
    try:
	    if (event['session']['application']['applicationId'] !=
	            "amzn1.ask.skill.7d942caa-da0f-45e5-81c8-08479081e33a"):
	        raise ValueError("Invalid Application ID")
    except KeyError: 
        x = 1

    try:
	    if event['session']["new"]:
	    	try:
	    		if event['session']['user']['userId'] !="amzn1.ask.account.TEST":
	    			add_customer_ddb(event['session']['user']['userId'])
	    	except:
	    		print("Did Not Add Customer ID")
	    		x = 1 
	    	return handle_request_event(event,context)
	    else:
	    	try:
				#print("Not New: {}".format(event['session']["attributes"]))
				if 'session' not in event:
					return handle_request_event(event,context)
				elif event['session']["attributes"]["prevIntent"] == "help":
				   return handle_request_event(event,context)
				elif event["request"]["intent"]["name"] == "ConfirmRequest":
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