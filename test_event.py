def test_event_obj():
	return  {
	  "session": {
	    "sessionId": "SessionId.25cc59d7-43c0-4c68-8f82-6608d9a24a68",
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
	    "requestId": "EdwRequestId.45bc0da7-279e-4a69-add6-ac61a3eddf62",
	    "locale": "en-US",
	    "timestamp": "2016-11-27T23:29:36Z",
	    "intent": {
	      "name": "RecentPodcast",
	      "slots": {
	        "podcast": {
	          "name": "podcast",
	          "value": "snap judgment"
	        },
	        "guest": {
	          "name": "guest"
	        }
	      }
	    }
	  },
	  "version": "1.0"
	}

def test_event_obj_guest():
	return  {
	  "session": {
	    "sessionId": "SessionId.a3d65d2a-36bf-4b1a-8c40-2e8b20d97a9a",
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
	    "requestId": "EdwRequestId.3811ff3f-b296-4ba3-ab11-37071f37af99",
	    "locale": "en-US",
	    "timestamp": "2016-11-27T00:02:39Z",
	    "intent": {
	      "name": "RecentPodcast",
	      "slots": {
	        "podcast": {
	          "name": "podcast",
	          "value": "doug loves movies"
	        },
	        "guest" : {
	        	"name" : "guest",
	        	"value" : "Mark Wahlberg"
	        }
	      }
	    }
	  },
	  "version": "2.0"
	}