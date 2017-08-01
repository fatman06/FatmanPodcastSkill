import account
import boto3
import difflib
from boto3.dynamodb.conditions import Key
import podcast_map as pm
import podcast as pc
import alexa
import podcast_audio_player as pap
import traceback

"""INTENTS"""

def intent_playlist_podcast(intent,session):
	if "accessToken" in session["user"]:
		token = session["user"]["accessToken"]
		accountId = account.get_account_id(token)
		playlists = get_all_playlists(accountId)
		if len(playlists) < 1 :
			return alexa.build_response_with_card("There was No Playlist found for this account, visit the Alexa app for instructions on how to create a new playlist","Creating a PodBuddy Playlist","You can create PodBuddy playlist by visiting the PodBuddy website. To get started visit: \n\n https://fatmandev.net/playlist","Standard")
		play_names = []
		play_dict = {}
		for p in playlists:
			play_names.append(p["playlist_name"].upper())
			play_dict[p["playlist_name"].upper()] = p
		guess = difflib.get_close_matches(intent["slots"]["keywords"]["value"].upper(),play_names)
		if len(guess) > 0:
			playlist = play_dict[guess[0]]
			return build_playlist_response(playlist,0)
		else:
			return alexa.basic_response("I was not able to found a playlist named {}".format(intent["slots"]["keywords"]["value"]))
	else: 
		description = "It appears your account is not currently link. You can use Pod Buddy without linking your account, however the Playlist feature requires an account to be linked.\n\nSelect 'Skills' from the menu > Select 'Your Skills' > Locate Pod Buddy > Select 'Link Account' and use the Login with Amazon. \n\nYou Can Create a Playlist by visiting \n\n https://fatmandev.net/playlist"
		return alexa.build_response_with_card("To utilize the Playlist feature you must link your account. Visit the Alexa App to link your account","Account Not Linked",description,"LinkAccount")

def next_playlist_podcast(token):
	accountId = token["accountId"]
	playlistId = token["playlistId"]
	index = (token["index"] + 1)
	playlist = get_specific_playlist(accountId,playlistId)
	if index < len(playlist[0]["tracks"]):
		try: 
			return build_playlist_response(playlist[0],index)
		except:
			return alexa.basic_response("There was a Problem Retrieving the next track in the playlist")
	else:
		return alexa.basic_response("No More Episodes in the Playlist")

def enqueue_next_playlist(token):
	accountId = token["accountId"]
	playlistId = token["playlistId"]
	index = (token["index"] + 1)
	playlist = get_specific_playlist(accountId,playlistId)
	if index < len(playlist[0]["tracks"]):
		try: 
			track = playlist[0]["tracks"][index]
			podcast = pm.find_podcast_regex(track["name"])
			url = build_url(podcast,track["url"])
			newtoken = build_playlist_token(url,index,track["name"],playlistId,accountId)
			return pap.build_enqueue_response({"url":url},token,4,newtoken)
		except:
			traceback.print_exc()
			return alexa.basic_response("There was a Problem Retrieving the next track in the playlist")
	else:
		return alexa.basic_response("No More Episodes in the Playlist")

"""END INTENTS"""

def get_all_playlists(accountId):
	client = boto3.resource('dynamodb',region_name='us-east-1')
	table = client.Table('pb_customer_playlist')
	playlists = scan_table_allpages('pb_customer_playlist','account_id',accountId)
	return playlists

def build_playlist_response(playlist,index=0):
	podcast = pm.find_podcast_regex(playlist["tracks"][index]["name"])
	url = build_url(podcast,playlist["tracks"][index]["url"])
	ep_name = playlist["tracks"][index]["ep_name"]
	token = build_playlist_token(url,index,playlist["tracks"][index]["name"],playlist["playlist_id"],playlist["account_id"])
	card = alexa.build_card(ep_name, playlist["tracks"][index]["name"], "Standard",podcast["image"])
	return pc.build_response(url, card, 0,token)
def build_playlist_token(url,index,name,playlistid,accountId):
	token = {
		"url" : url,
		"index" : index,
		"name" : name,
		"playlistId": playlistid,
		"type": 4,
		"accountId": accountId
	}
	return token

def build_url(podcast,url):
	if 'redirect' in podcast:
		redirect = True
	else:
		redirect = False
	if 'podtrac' in podcast:
		podtrac = True
	else:
		podtrac = False
	return pc.build_url(url,podtrac,redirect)

def get_specific_playlist(accountId,playlistId):
	client = boto3.resource('dynamodb',region_name='us-east-1')
	table = client.Table("pb_customer_playlist")
	response = table.query(
			Select='ALL_ATTRIBUTES',
			KeyConditionExpression=Key('account_id').eq(accountId) & Key('playlist_id').eq(playlistId)
		)
	return response["Items"]

"""
HELPERS

"""

def scan_table_allpages(table_name, filter_key=None, filter_value=None):
	"""
	Perform a scan operation on table. 
	Can specify filter_key (col name) and its value to be filtered. 
	This gets all pages of results. Returns list of items.
	"""
	client = boto3.resource('dynamodb',region_name='us-east-1')
	table = client.Table(table_name)

	if filter_key and filter_value:
		filtering_exp = Key(filter_key).eq(filter_value)
		response = table.scan(FilterExpression=filtering_exp)
	else:
		response = table.scan()

	items = response['Items']
	while True:
		if response.get('LastEvaluatedKey'):
			response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
			items += response['Items']
		else:
			break

	return items


