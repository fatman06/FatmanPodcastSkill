import re

def podcast_map():

	podcast_map = {
	   r'(?i)doug loves movie':{
	      "stream":"http://feeds.feedburner.com/DougLovesMovies",
	      "image":"",
	      "name":"Doug Loves Movies"
	   },
	   r'(?i)(jericho|jerico)':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=593",
	      "image":"",
	      "name":"Talk Is Jericho"
	   },
	   r'(?i)(stone cold|steve austin)':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=436",
	      "image":"",
	      "name":"Steve Austin Podcast"
	   },
	   r'(?i)(snap)':{
	      "stream":"http://feeds.wnyc.org/snapjudgment-wnyc",
	      "image":"",
	      "name":"Snap Judgement"
	   },
	   r'(?i)(what culture|whatculture)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:190525730/sounds.rss",
	      "image":"",
	      "name":"What Culture Wrestling"
	   },
	   r'(?i)(two dope|dope queen|2 dope)':{
	      "stream":"http://feeds.wnyc.org/2dopequeens",
	      "image":"",
	      "name":"2 Dope Queens"
	   },
	   r'(?i)(Ninety-Nine|Ninety Nine) (percent| per) (inv)+':{
	      "stream":"http://feeds.99percentinvisible.org/99percentinvisible",
	      "image":"",
	      "name":"99% Invisible"
	   },
	   r'(?i)(Comedy Bang)':{
	      "stream":"http://rss.earwolf.com/comedy-bang-bang",
	      "image":"",
	      "name":"Comedy Bang Bang: The Podcast"
	   },
	   r'(?i)(crimetown|crime town)':{
	      "stream":"http://feeds.gimletmedia.com/crimetownshow",
	      "image":"",
	      "name":"Crimetown"
	   },
	   r'(?i)(criminal)':{
	      "stream":"http://thisiscriminal.com/feed/",
	      "image":"",
	      "name":"Criminal"
	   },
	   r'(?i)(Dan Carlin.+|^)(Hard).+(Hist)':{
	      "stream":"http://feeds.feedburner.com/dancarlin/commonsense?format=xml",
	      "image":"",
	      "name":"Dan Carlin's Hardcore History"
	   },
	   r'(?i)(Disney.+|^)(Story).+(Central)':{
	      "stream":"https://public-static.disneystorycentral.com/ddb/storycast/DSC_Podcast.xml",
	      "image":"",
	      "name":"Disney Story Central Podcast"
	   },
	   r'(?i)(freak).+(radio|$)':{
	      "stream":"http://feeds.feedburner.com/freakonomicsradio",
	      "image":"",
	      "name":"Freakonomics Radio"
	   },
	   r'(?i)(fresh air)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=381444908",
	      "image":"",
	      "name":"Fresh Air"
	   },
	   r'(?i)(Hidden).+(brain|brian)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510308",
	      "image":"",
	      "name":"Hidden Brain"
	   },
	   r'(?i)(home)(.+|)(coming|cumming)':{
	      "stream":"http://feeds.gimletmedia.com/homecomingshow",
	      "image":"",
	      "name":"Homecoming"
	   },
	   r'(?i)(how).+(I|eye).+(built|build)(.+|$)(this|$)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510313",
	      "image":"",
	      "name":"How I Built This"
	   },
	   r'(?i)(invisibil)(e|ia|$)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510307",
	      "image":"",
	      "name":"Invisibilia"
	   },
	   r'(?i)(last)(.+)(pod)(.+)(left|$)':{
	      "stream":"http://cavecomedyradio.com/pod-series/last-podcast-on-the-left/feed/",
	      "image":"",
	      "name":"Last Podcast On The Left"
	   },
	   r'(?i)(life)(.+|)(after)':{
	      "stream":"http://feeds.megaphone.fm/themessage",
	      "image":"",
	      "name":"LifeAfter"
	   },
	   r'(?i)(lore|loar)':{
	      "stream":"http://lorepodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Lore"
	   },
	   r'(?i)(making)(.+)(oprah)':{
	      "stream":"http://feeds.feedburner.com/wbez-making",
	      "image":"",
	      "name":"Making Oprah"
	   },
	   r'(?i)(mon)(.+)(morn)(.+)(pod|$)':{
	      "stream":"http://billburr.libsyn.com/rss",
	      "image":"",
	      "name":"Monday Morning Podcast"
	   },
	   r'(?i)(My|^)(.+)(dad).+(wrote|write).+(porn|$)':{
	      "stream":"http://rss.acast.com/mydadwroteaporno",
	      "image":"",
	      "name":"My Dad Wrote A Porno"
	   },
	   r'(?i)((My|^).+(Fav).+(Mur).+(\s|$)|Karen Kilgariff|Georgia Hardstark)':{
	      "stream":"http://rss.art19.com/my-favorite-murder-with-karen-kilgariff-and-georgia-hardstark",
	      "image":"",
	      "name":"My Favorite Murder with Karen Kilgariff and Georgia Hardstark"
	   },
	   r'(?i)(NPR).+(pol).+$':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510310",
	      "image":"",
	      "name":"NPR Politics Podcast"
	   },
	   r'(?i)(plan).+(mon).+$':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510289",
	      "image":"",
	      "name":"Planet Money"
	   },
	   r'(?i)((radio)(.+|)(lab).+(pres).+|^)(more).+(perfect)':{
	      "stream":"http://feeds.wnyc.org/moreperfect",
	      "image":"",
	      "name":"Radiolab Presents: More Perfect"
	   },
	   r'(?i)(radio)(.+|)(lab)':{
	      "stream":"http://feeds.wnyc.org/radiolab",
	      "image":"",
	      "name":"Radiolab"
	   },
	   r'(?i)((Remark).+(live)|^)(.+|)((trag).+(death)|$)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:242596778/sounds.rss",
	      "image":"",
	      "name":"Remarkable Lives. Tragic Deaths."
	   },
	   "reveal":{
	      "stream":"http://feeds.revealradio.org/revealpodcast",
	      "image":"",
	      "name":"Reveal"
	   },
	   "spacevs":{
	      "stream":"http://feeds.gimletmedia.com/sciencevs",
	      "image":"",
	      "name":"Science Vs - New Season"
	   },
	   "serial":{
	      "stream":"http://feeds.serialpodcast.org/serialpodcast",
	      "image":"",
	      "name":"Serial"
	   },
	   "startalk":{
	      "stream":"https://feeds.soundcloud.com/users/soundcloud:users:38128127/sounds.rss",
	      "image":"",
	      "name":"StarTalk Radio"
	   },
	   "symihc":{
	      "stream":"http://www.howstuffworks.com/podcasts/stuff-you-missed-in-history-class.rss",
	      "image":"",
	      "name":"Stuff You Missed in History Class"
	   },
	   "sysk":{
	      "stream":"http://www.howstuffworks.com/podcasts/stuff-you-should-know.rss",
	      "image":"",
	      "name":"Stuff You Should Know"
	   },
	   "sword_scale":{
	      "stream":"http://rss.art19.com/sword-and-scale",
	      "image":"",
	      "name":"Sword and Scale"
	   },
	   "ted_radio_hour":{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510298",
	      "image":"",
	      "name":"TED Radio Hour"
	   },
	   "tmsidk":{
	      "stream":"http://feeds.feedburner.com/freakonomicsradio",
	      "image":"",
	      "name":"Tell Me Something I Don't Know"
	   },
	   "dave_ramsey":{
	      "stream":"https://www.daveramsey.com/rss/view-feed/strFeeds/CrcSuccessStories-PressRelease-DaveSays",
	      "image":"",
	      "name":"The Dave Ramsey Show"
	   },
	   "dollop":{
	      "stream":"http://thedollop.libsyn.com/rss",
	      "image":"",
	      "name":"The Dollop with Dave Anthony and Gareth Reynolds"
	   },
	   "history_of_rome":{
	      "stream":"http://feeds.feedburner.com/TheHistoryOfRome",
	      "image":"",
	      "name":"The History of Rome"
	   },
	   "joe_rogan":{
	      "stream":"http://joeroganexp.joerogan.libsynpro.com/rss",
	      "image":"",
	      "name":"The Joe Rogan Experience"
	   },
	   "moth":{
	      "stream":"http://feeds.themoth.org/themothpodcast",
	      "image":"",
	      "name":"The Moth"
	   },
	   "nerdist":{
	      "stream":"http://nerdist.libsyn.com/rss",
	      "image":"",
	      "name":"The Nerdist"
	   },
	   "tim_ferris":{
	      "stream":"http://feeds.feedburner.com/thetimferrissshow",
	      "image":"",
	      "name":"The Tim Ferriss Show"
	   },
	   "american_life":{
	      "stream":"http://feed.thisamericanlife.org/talpodcast",
	      "image":"",
	      "name":"This American Life"
	   },
	   "undone":{
	      "stream":"http://feeds.gimletmedia.com/undoneshow",
	      "image":"",
	      "name":"Undone"
	   },
	   "up_and_vanished":{
	      "stream":"http://rss.art19.com/the-vanished-podcast",
	      "image":"",
	      "name":"Up and Vanished"
	   },
	   "wwdtm":{
	      "stream":"http://www.npr.org/rss/podcast.php?id=344098539",
	      "image":"",
	      "name":"Wait Wait... Don't Tell Me!"
	   },
	   "wofh":{
	      "stream":"https://rss.art19.com/women-of-the-hour",
	      "image":"",
	      "name":"Women Of The Hour"
	   },
	   "wtf_marc_maron":{
	      "stream":"https://wtfpod.libsyn.com/rss",
	      "image":"",
	      "name":"WTF with Marc Maron Podcast"
	   }
	}
	return podcast_map

def find_podcast_regex(text):
	response = None
	podcast = podcast_map()
	for k,v in podcast.items():
		if re.search(k,text):
			return  v
	return response	

