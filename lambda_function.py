from __future__ import print_function
version = "0.0.30"
print("Podcast Network Version " + version + " - Alpha")

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
    logger.info('got event{}'.format(event))
    return True

def getVersion():
	return version

# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    #url = recent_podcast_stream(event['request'], event['session'])
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.ask.skill.7d942caa-da0f-45e5-81c8-08479081e33a"):
    #     raise ValueError("Invalid Application ID")


    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
    
    #return build_response(pod["url"],card)