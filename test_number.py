from __future__ import print_function
from lambda_function import *

event = {
  "session": {
    "sessionId": "SessionId.2130ddea-28d6-4d65-9fb1-31834086e17b",
    "application": {
      "applicationId": "amzn1.ask.skill.7d942caa-da0f-45e5-81c8-08479081e33a"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AFP3ZWPOS2BGJR7OWJZ3DHPKMOMHLFC7TB5KHJ7GPZMTRY2ABHXVF67VSFYOFMFF2EMNPHYJDAKTY4YRATDUUZZKZPXEAKUEL72BPVAZWXLIKKNXO62B6SDZ3322V6JVBGZ7VB7ZZX7HYNK54RCAYPOTTZQGM55T2XBOKVTUZP6PFU2H6MQXLH4VYT4GSSY5FWV7YTIQAG3M24A"
    },
    "new": True
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.98163978-5f5f-42eb-a6f6-88a09696e5ed",
    "locale": "en-US",
    "timestamp": "2017-01-08T08:45:58Z",
    "intent": {
      "name": "RecentPodcastShuffle",
      "slots": {
        "timeframe": {
          "name": "timeframe"
        },
        "number": {
          "name": "number"
        },
        "podcast": {
          "name": "podcast",
          "value": "the joe rogan podcast"
        },
        "epnumber": {
          "name": "epnumber",
          "value": "890"
        }
      }
    }
  },
  "version": "1.0"
}

print(lambda_handler(event,"context"))
