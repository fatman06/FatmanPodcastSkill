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
	   r'(?i)(stone cold|steve austin).+(unleash)':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=436",
	      "image":"",
	      "name":"Steve Austin Unleashed Podcast"
	   },
	   r'(?i)(stone cold|steve austin)':{
	   	  "stream" : "http://www.podcastone.com/podcast?categoryID2=542",
	   	  "image" : "",
	   	  "name" : "The Steve Austin Show"

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
	   r'(?i)(Ninety-Nine|Ninety Nine|99) (percent| per |) (inv)+':{
	      "stream":"http://feeds.99percentinvisible.org/99percentinvisible",
	      "image":"",
	      "name":"99 Percent Invisible"
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
	   r'(?i)((remark).+(live)|(trag).+(dea))':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:242596778/sounds.rss",
	      "image":"",
	      "name":"Remarkable Lives. Tragic Deaths."
	   },
	   r'(?i)(reveal)':{
	      "stream":"http://feeds.revealradio.org/revealpodcast",
	      "image":"",
	      "name":"Reveal"
	   },
	   r'(?i)(sci).+(vers|vs)':{
	      "stream":"http://feeds.gimletmedia.com/sciencevs",
	      "image":"",
	      "name":"Science Vs - New Season"
	   },
	   r'(?i)serial':{
	      "stream":"http://feeds.serialpodcast.org/serialpodcast",
	      "image":"",
	      "name":"Serial"
	   },
	   r'(?i)(star)(.|)(talk)(\srad|||$)':{
	      "stream":"https://feeds.soundcloud.com/users/soundcloud:users:38128127/sounds.rss",
	      "image":"",
	      "name":"StarTalk Radio"
	   },
	   r'(?i)(stuff|thing).+(miss).+(hist).+(class)':{
	      "stream":"http://www.howstuffworks.com/podcasts/stuff-you-missed-in-history-class.rss",
	      "image":"",
	      "name":"Stuff You Missed in History Class"
	   },
	   r'(?i)(stuff).+(should).+(know)':{
	      "stream":"http://www.howstuffworks.com/podcasts/stuff-you-should-know.rss",
	      "image":"",
	      "name":"Stuff You Should Know"
	   },
	   r'(?i)(sword).+(scale)':{
	      "stream":"http://rss.art19.com/sword-and-scale",
	      "image":"",
	      "name":"Sword and Scale"
	   },
	   r'(?i)(Ted).(radio).(hour)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510298",
	      "image":"",
	      "name":"TED Radio Hour"
	   },
	   r'(?i)(tell).(me).(some).+(know)':{
	      "stream":"http://feeds.feedburner.com/freakonomicsradio",
	      "image":"",
	      "name":"Tell Me Something I Don't Know"
	   },
	   r'(?i)((Dave).(Ram))(.+show|.+$)':{
	      "stream":"https://www.daveramsey.com/rss/view-feed/strFeeds/CrcSuccessStories-PressRelease-DaveSays",
	      "image":"",
	      "name":"The Dave Ramsey Show"
	   },
	   r'(?i)((Dollop)|(dave.anthony)|(Gareth Reynolds))':{
	      "stream":"http://thedollop.libsyn.com/rss",
	      "image":"",
	      "name":"The Dollop with Dave Anthony and Gareth Reynolds"
	   },
	   r'(?i)(hist).+(rome)':{
	      "stream":"http://feeds.feedburner.com/TheHistoryOfRome",
	      "image":"",
	      "name":"The History of Rome"
	   },
	   r'(?i)(Joe Rogan)':{
	      "stream":"http://joeroganexp.joerogan.libsynpro.com/rss",
	      "image":"",
	      "name":"The Joe Rogan Experience"
	   },
	   r'(?i)the moth':{
	      "stream":"http://feeds.themoth.org/themothpodcast",
	      "image":"",
	      "name":"The Moth"
	   },
	   r'(?i)(nerd)(.+|)(is)':{
	      "stream":"http://nerdist.libsyn.com/rss",
	      "image":"",
	      "name":"The Nerdist"
	   },
	   r'(?i)(Tim).+(Ferr)':{
	      "stream":"http://feeds.feedburner.com/thetimferrissshow",
	      "image":"",
	      "name":"The Tim Ferriss Show"
	   },
	   r'(?i)(th).+(Amer).+(life)':{
	      "stream":"http://feed.thisamericanlife.org/talpodcast",
	      "image":"",
	      "name":"This American Life"
	   },
	   r'(?i)(un)(.|)(done)':{
	      "stream":"http://feeds.gimletmedia.com/undoneshow",
	      "image":"",
	      "name":"Undone"
	   },
	   r'(?i)(up)(.+)(vanish)':{
	      "stream":"http://rss.art19.com/the-vanished-podcast",
	      "image":"",
	      "name":"Up and Vanished"
	   },
	   r'(?i)(wait)(.+)(don).+(tel).+(me)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=344098539",
	      "image":"",
	      "name":"Wait Wait... Don't Tell Me!"
	   },
	   r'(?i)(wom[ae]).+(hour)':{
	      "stream":"https://rss.art19.com/women-of-the-hour",
	      "image":"",
	      "name":"Women Of The Hour"
	   },
	   r'(?i)((wtf|what the)|^|)(.+|^|)(mar[ck]).+(mar)':{
	      "stream":"https://wtfpod.libsyn.com/rss",
	      "image":"",
	      "name":"WTF with Marc Maron Podcast"
	   },
	   r'(?i)(accused)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:234220545/sounds.rss",
	      "image":"",
	      "name":"Accused"
	   },
	   r'(?i)((Anna).(Far)|(Unqualified))':{
	      "stream":"http://annafarisisunqualified.libsyn.com/rss",
	      "image":"",
	      "name":"Anna Faris Is Unqualified"
	   },
	   r'(?i)((ask).(me).(another))':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510299",
	      "image":"",
	      "name":"Ask Me Another"
	   },
	   r'(?i)((Back)(.|)(story)|(America).+(his).+(guy).+)':{
	      "stream":"http://feeds.feedburner.com/BackStoryRadio",
	      "image":"",
	      "name":"BackStory with the American History Guys"
	   },
	   r'(?i)(car).(talk)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510208",
	      "image":"",
	      "name":"Car Talk"
	   },
	   r'(?i)(case)(.|)(file).(true).(crime)':{
	      "stream":"http://casefile.libsyn.com/rss",
	      "image":"",
	      "name":"Casefile True Crime"
	   },
	   r'(?i)(code)(.|)(switch)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510312",
	      "image":"",
	      "name":"Code Switch"
	   },
	   r'(?i)(comm).+(sense)':{
	      "stream":"http://www.dancarlin.com/cswdc-feedburner.xml",
	      "image":"",
	      "name":"Common Sense with Dan Carlin"
	   },
	   r'(?i)(death).+(sex).+(money)':{
	      "stream":"https://public-static.disneystorycentral.com/ddb/storycast/DSC_Podcast.xml",
	      "image":"",
	      "name":"Death, Sex & Money"
	   },
	   r'(?i)(do).+(listen).+(twice)':{
	      "stream":"http://feed.thisamericanlife.org/DoListenTwice",
	      "image":"",
	      "name":"Do Listen Twice"
	   },
	   r'(?i)((five)(.|)(thirty)(.|)(eight)).+(pol)':{
	      "stream":"https://secure.espn.com/espnradio/podcast/feeds/itunes/podCast?id=14554755",
	      "image":"",
	      "name":"FiveThirtyEight Politics"
	   },
	   r'(?i)(gilm|gil.+mor).+(guy)':{
	      "stream":"http://www.spreaker.com/user/8249928/episodes/feed?clickid=wAUT5HVl%3A3oTySq3AnxOUwK2UkkQJcU1y0u-180&irpid=27795&sharedid=&mp_value1=VigLink",
	      "image":"",
	      "name":"Gilmore Guys"
	   },
	   r'(?i)(BBC|^).(glob).+(new)':{
	      "stream":"http://www.bbc.co.uk/programmes/p02nq0gn/episodes/downloads.rss",
	      "image":"",
	      "name":"BBC Global News Podcast"
	   },
	   r'(?i)((Gramm).+(girl))|(quick).+(dirty).+(tip).+(writing)':{
	      "stream":"http://www.qdnow.com/grammar.xml",
	      "image":"",
	      "name":"Grammar Girl Quick and Dirty Tips for Better Writing"
	   },
	   r'(?i)(guy).+(we).(f.+d|screw|f.+k)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:68891950/sounds.rss",
	      "image":"",
	      "name":"Guys We Fucked"
	   },
	   r'(?i)(Harry).+(Potter).+(sac).+(tex)':{
	      "stream":"http://feeds.feedburner.com/HarryPotterAndTheSacredText",
	      "image":"",
	      "name":"Harry Potter and the Sacred Text"
	   },
	   r'(?i)(heavy)(\s|)(weight)':{
	      "stream":"http://feeds.gimletmedia.com/heavyweightpodcast",
	      "image":"",
	      "name":"Heavyweight"
	   },
	   r'(?i)(hor[a-z]+)\s(line)':{
	      "stream":"https://feeds.megaphone.fm/horizonline",
	      "image":"",
	      "name":"Horizon Line"
	   },
	   r'(?i)(how).+(get).+(made)':{
	      "stream":"http://rss.earwolf.com/how-did-this-get-made",
	      "image":"",
	      "name":"How Did This Get Made?"
	   },
	   r'(?i)(in).+(the).+(dark)':{
	      "stream":"https://feeds.publicradio.org/public_feeds/in-the-dark/itunes/rss",
	      "image":"",
	      "name":"In the Dark"
	   },
	   r'(?i)(jock)(.o|o)':{
	      "stream":"http://jockopodcast2.com/feed/podcast/",
	      "image":"",
	      "name":"Jocko Podcast"
	   },
	   r'(?i)(joe).+(osteen|austin)':{
	      "stream":"https://www.joelosteen.com/Views/RSS/Feed?t=PodcastAudio&ct=CustomList&cst=Podcasts",
	      "image":"",
	      "name":"Joel Osteen Podcast"
	   },
	   r'(?i)(keep).+(it).+(1600|(six)(.|)(teen).+(hun))':{
	      "stream":"http://feeds.feedburner.com/KeepinIt1600",
	      "image":"",
	      "name":"Keepin' it 1600"
	   },
	   r'(?i)(ma[ue]ve).+(amer)':{
	      "stream":"http://feeds.feedburner.com/MaeveInAmerica",
	      "image":"",
	      "name":"Maeve In America"
	   },
	   r'(?i)(mod).+(love)':{
	      "stream":"http://feeds.wbur.org/modernlove/podcast",
	      "image":"",
	      "name":"Modern Love"
	   },
	   r'(?i)(myth).+(legend)':{
	      "stream":"http://mythpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Myths and Legends"
	   },
	   r'(?i)(Note).+(t).+(Self)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510310",
	      "image":"",
	      "name":"Note to Self"
	   },
	   r'(?i)(On).+(Being)|((k|ch)ris).+(tip)':{
	      "stream":"http://www.onbeing.org/podcasts/podcast.xml",
	      "image":"",
	      "name":"On Being with Krista Tippett"
	   },
	   r'(?i)(pard).+(m).+(take)':{
	      "stream":"http://feeds.feedburner.com/PardonMyTake",
	      "image":"",
	      "name":"Pardon My Take"
	   },
	   r'(?i)(Real).+(Time).+(bill).+(m)':{
	      "stream":"http://billmaher.hbo.libsynpro.com/rss",
	      "image":"",
	      "name":"Real Time with Bill Maher"
	   },
	   r'(?i)(repl).+(al)':{
	      "stream":"http://feeds.gimletmedia.com/hearreplyall",
	      "image":"",
	      "name":"Reply All"
	   },
	   r'(?i)(revis).+(hist)':{
	      "stream":"http://feeds.feedburner.com/RevisionistHistory",
	      "image":"",
	      "name":"Revisionist History"
	   },
	   r'(?i)(sci).+(fri)':{
	      "stream":"http://www.sciencefriday.com/feed/podcast/podcast-episode",
	      "image":"",
	      "name":"Science Friday"
	   },
	   r'(?i)(secret).+(crime).+(audio)':{
	      "stream":"https://rss.art19.com/secrets-crimes-audiotape",
	      "image":"",
	      "name":"Secrets, Crimes & Audiotape"
	   },
	   r'(?i)(sha).+(friend)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:44683272/sounds.rss",
	      "image":"",
	      "name":"Shane And Friends"
	   },
	   r'(?i)(slate).+(trump(.|)cast)':{
	      "stream":"http://feeds.megaphone.fm/trumpcast",
	      "image":"",
	      "name":"Slate's Trumpcast"
	   },
	   r'(?i)(sleep).+(me)':{
	      "stream":"http://www.sleepwithmepodcast.com/feed/podcast/",
	      "image":"",
	      "name":"Sleep With Me"
	   },
	   r'(?i)(some).+(kno).+(some)':{
	      "stream":"http://www.cbc.ca/podcasting/includes/sks.xml",
	      "image":"",
	      "name":"Someone Knows Something"
	   },
	   r'(?i)(some).+(sho).+(kno)':{
	      "stream":"http://syskpod.libsyn.com/rss",
	      "image":"",
	      "name":"Something You Should Know"
	   },
	   r'(?i)(strangler)':{
	      "stream":"http://rss.earwolf.com/stranglers",
	      "image":"",
	      "name":"Stranglers"
	   },
	   r'(?i)(TED)(.|)(talk)':{
	      "stream":"http://feeds.feedburner.com/TEDTalks_audio",
	      "image":"",
	      "name":"TEDTalks (audio)"
	   },
	   r'(?i)(Adv).+(zone)':{
	      "stream":"http://adventurezone.libsyn.com/rss",
	      "image":"",
	      "name":"The Adventure Zone"
	   },
	   r'(?i)(art).+(charm)':{
	      "stream":"http://theartofcharmpodcast.theartofcharm.libsynpro.com/rss",
	      "image":"",
	      "name":"The Art of Charm"
	   },
	   r'(?i)(art).+(man)':{
	      "stream":"http://feeds.feedburner.com/artofmanlinesspodcast",
	      "image":"",
	      "name":"The Art of Manliness"
	   },
	   r'(?i)(new).+(york).+(rad).+(hour)':{
	      "stream":"http://feeds.wnyc.org/newyorkerradiohour",
	      "image":"",
	      "name":"The New Yorker Radio Hour"
	   },
	   r'(?i)(run)(\s|-|)(up)':{
	      "stream":"https://feeds.podtrac.com/pLNosqouzJak",
	      "image":"",
	      "name":"The Run-Up"
	   },
	   r'(?i)(anthony|tony).+(rob)':{
	      "stream":"http://tonyrobbins.libsyn.com/rss",
	      "image":"",
	      "name":"The Tony Robbins Podcast"
	   },
	   r'(?i)(way).+(hear).+\s(it)|(mike).+(row)':{
	      "stream":"http://thewayiheardit.rsvmedia.com/rss/",
	      "image":"",
	      "name":"The Way I Heard It with Mike Rowe"
	   },
	   r'(?i)((wak[ei]).+(up))|(sam).+(har)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:59753170/sounds.rss",
	      "image":"",
	      "name":"Waking Up with Sam Harris"
	   },
	   r'(?i)(wel).+(night).+(vale)':{
	      "stream":"http://nightvale.libsyn.com/rss",
	      "image":"",
	      "name":"Welcome to Night Vale"
	   }
	}
	return podcast_map

def find_podcast_regex(text):
	response = None
	podcast = podcast_map()
	for k,v in podcast.items():
		if re.search(re.compile(k),text):
			return  v
			break
	return response	

