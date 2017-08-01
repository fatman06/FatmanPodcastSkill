import urllib2
import json

def get_account_id(accessToken):
	print("hello")
	url = "https://api.amazon.com/user/profile?access_token={}".format(accessToken)
	req =  urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	token = urllib2.urlopen(req).read()
	obj = json.loads(token)
	return obj["user_id"].replace('amzn1.account.','')




