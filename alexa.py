from __future__ import print_function

import json
import urllib2
import re
from xml.etree import ElementTree as etree
from podcast import *
from podcast_multiple import *
from podcast_audio_player import *
import ast

from confirm_request import *

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session,cardtext=None):
    response = {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    } 
    if title is not None and cardtext is not None:
    	response["card"] = {
            'type': 'Simple',
            'title': title,
            'content': cardtext
        }
    return response

def basic_response(text):
	return {
		'response' : {
			'outputSpeech' : {
				'type' : 'PlainText',
				'text' : text
			},
			'shouldEndSession':True
		}
	}

def basic_response_reprompt(text,reprompt,session_end=False):
	return  {
		'response' : {
			'outputSpeech' : {
				'type' : 'PlainText',
				'text' : text
			},
			'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt
	            }
	        },
			'shouldEndSession':session_end
		}
	}

def build_response_with_card(speech,title,description,ctype,image=''):
	response = basic_response(speech)
	response["response"].update(build_card(title,description,ctype,image))
	return response

def alexa_build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def build_card(title, content, ctype='Simple',image=''):
	#removing image unitl i can find a better option
	if ctype=='Standard':
		return {'card': {'type':ctype, 'title': title, 'text': content[:1800]}}
	else:
		return {'card': {'type':ctype, 'title': title, 'content': content[:1800]}}
# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {"prevIntent":"Launch"}
    card_title = "Welcome to Pod Buddy"
    speech_output = "Welcome to Pod Buddy " \
                    "You can ask me to play your favorite podcast . . ." \
                    " For Example Say . . . Play the Disney Story Central Podcast . . . What Podcast would you like to listen to?"
    cardtext = "For more Help and list of additional features visit: \nhttp://fatmandev.net/pod-buddy/help"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please say a podcast you would like to listen to . . ." \
                    " "
    should_end_session = False
    return alexa_build_response(session_attributes, build_speechlet_response(
        "Welcome To Pod Buddy", speech_output, reprompt_text, should_end_session,cardtext))

def get_help_response():

    session_attributes = {"prevIntent":"AMAZON.HelpIntent"}
    card_title = "Welcome to Pod Buddy"
    speech_output = "" \
                    "You can ask me to play your favorite podcast " \
                    "by saying play and the name of the podcast . . . For Example you can say . . . Play the Disney Story Central Podcast . . . What Podcast would you like to listen to?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please say a podcast you would like to listen to . . ." \
                    " "
    cardtext = "For more Help and list of additional features visit: \nhttp://fatmandev.net/pod-buddy/help"
    should_end_session = False
    return alexa_build_response(session_attributes, build_speechlet_response(
        "Pod Buddy Help", speech_output, reprompt_text, should_end_session,cardtext))


def handle_session_end_request():
	card_title = "Session Ended"
	res={'response':
		{'directives':[
			{"type": "AudioPlayer.Stop"}
			],
		'shouldEndSession':True
		}
	}
	return res


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def parseToken(token):
    print(token)
    return ast.literal_eval(token)

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session, context=None):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request["request"]['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request["request"]['intent']
    intent_name = intent_request["request"]['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent" or intent_name == "AMAZON.PauseIntent":
        return handle_session_end_request()
    elif intent_name == "ConfirmRequest":
        return handle_confirm_request(intent,session) 
    elif intent_name == "SkipAhead":
        if context is not None:
            return on_media_direction_handling("forward",context,intent)
        else:
            print("on_intent SkipAhead No Context")
    elif intent_name == "AMAZON.NextIntent":
        if context is not None:
            return on_playback_next_handling(intent,context)
        else:
            print("on_intent NextIntent No context")

    elif intent_name == "AMAZON.ResumeIntent":
    	try:
            token = parseToken(intent_request["context"]["AudioPlayer"]["token"])
    		return build_response(token["url"], None, intent_request["context"]["AudioPlayer"]["offsetInMilliseconds"],token) 
    	except:
            print(intent_request)
            print("Resume Failed")
            response = a.basic_response_reprompt("I was unable to resume your podcast. Which podcast would you like to listen to? ","Which podcast would you like to listen to",False)
            response["sessionAttributes"] = {"prevIntent" : "AMAZON.ResumeIntent"}
            return response
    elif intent_name == "RecentPodcast" or intent_name == "RecentPodcastEpisode":
    	return intent_recent_podcast(intent, session)
    elif intent_name == "RecentPodcastShuffle":
        return intent_shuffle_stream(intent,session)
    elif intent_name == "ListRecentPodcast":
    	return intent_list_recent_podcast(intent,session)
    else:
        print("Invalid Intent: " + intent_name)
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    #print("on_session_ended requestId=" + session_ended_request['requestId'] +
          #", sessionId=" + session['sessionId'])
    # add cleanup logic here
