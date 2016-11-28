import re

def podcast_map(key):

	podcast_map = {
		"dlm" : "http://feeds.feedburner.com/DougLovesMovies",
		"jericho" : "http://www.podcastone.com/podcast?categoryID2=593",
		"stonecold" : "http://www.podcastone.com/podcast?categoryID2=436",
		"snap" : "http://feeds.wnyc.org/snapjudgment-wnyc",
		"whatculture" : "http://feeds.soundcloud.com/users/soundcloud:users:190525730/sounds.rss"
	}
	try:
		return podcast_map[key]
	except KeyError:
		return None

def podcast_img(img):
	podcast_map = {
		"dlm" : "https://cdn-radiotime-logos.tunein.com/p207738g.png",
		"jericho" : "http://webveeguide.com/wp-content/uploads/2016/01/talk-is-jericho.jpeg",
		"stonecold" : "https://www.podcastonesales.com/images/podcast/steveaustinunleashed1400x1400.jpg",
		"snap" : "https://media2.wnyc.org/i/1400/1400/l/80/1/wn16_wnycstudios_SnapJudgement.png",
		"whatculture" : ""
	}
	try:
		return podcast_map[img]
	except KeyError:
		return None

def podcast_key(text):
	if re.search(r'(?i)doug loves movie',text):
		key = "dlm"
	elif re.search(r'(?i)(jericho|jerico)',text):
		key = "jericho"
	elif re.search(r'(?i)(stone cold|steve austin)',text):
		key = "stonecold"
	elif re.search(r'(?i)(snap)',text):
		key = "snap"
	elif re.search(r'(?i)(what culture|whatculture)'):
		key = "whatculture"
	else:
		key = None

	return key

