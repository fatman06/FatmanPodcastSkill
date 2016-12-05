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
	   },
	   r'':{
	      "stream":"http://nightvale.libsyn.com/rss",
	      "image":"",
	      "name":"Welcome to Night Vale"
	   },
	   r'':{
	      "stream":"https://rss.art19.com/women-of-the-hour",
	      "image":"",
	      "name":"Women Of The Hour"
	   },
	   r'':{
	      "stream":"https://wtfpod.libsyn.com/rss",
	      "image":"",
	      "name":"WTF with Marc Maron Podcast"
	   },
	   r'':{
	      "stream":"https://rss.art19.com/these-are-their-stories-the-law-and-order-podcast",
	      "image":"",
	      "name":"...These Are Their Stories: The Law & Order Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/dailyaudiobible",
	      "image":"",
	      "name":"1 Year Daily Audio Bible"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/abcradio/10percenthappier",
	      "image":"",
	      "name":"10% Happier with Dan Harris"
	   },
	   r'':{
	      "stream":"http://meetthepress1947.nbcnews.libsynpro.com/rss",
	      "image":"",
	      "name":"1947: The Meet the Press Podcast"
	   },
	   r'':{
	      "stream":"http://2docstalk.libsyn.com/rss",
	      "image":"",
	      "name":"2 Docs Talk:  Medicine | Health | Healthcare Policy | Evidence Based Medicine"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/yogadownload",
	      "image":"",
	      "name":"20 min. Yoga Sessions from YogaDownload.com"
	   },
	   r'':{
	      "stream":"https://dmv.ca.gov/web/audio_hdbk/dmv_podcast.xml",
	      "image":"",
	      "name":"2016 California Driver Audio Handbook"
	   },
	   r'':{
	      "stream":"http://dj3lau.podbean.com/feed/",
	      "image":"",
	      "name":"3LAU HAUS"
	   },
	   r'':{
	      "stream":"http://40weeks.libsyn.com/rss",
	      "image":"",
	      "name":"40 Weeks Pregnancy Podcast"
	   },
	   r'':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1222?format=MP3_128K",
	      "image":"",
	      "name":"48 Hours"
	   },
	   r'':{
	      "stream":"https://www.buzzsprout.com/57707.rss",
	      "image":"",
	      "name":"5 Minute Marketing: Shortcuts to Growing Your Business Online, 5 Minutes at a Time"
	   },
	   r'':{
	      "stream":"http://feeds.5minutesinchurchhistory.com/5ChurchHistory",
	      "image":"",
	      "name":"5 Minutes in Church History - A Weekly Christian Podcast with Stephen Nichols"
	   },
	   r'':{
	      "stream":"http://www.bbc.co.uk/programmes/p02pc9tn/episodes/downloads.rss",
	      "image":"",
	      "name":"6 Minute English"
	   },
	   r'':{
	      "stream":"https://www.scientificamerican.com/sciam/xml/iTunes.cfm?id=60-second-mind",
	      "image":"",
	      "name":"60-Second Mind"
	   },
	   r'':{
	      "stream":"https://www.scientificamerican.com/sciam/xml/iTunes.cfm?id=60-second-science",
	      "image":"",
	      "name":"60-Second Science"
	   },
	   r'':{
	      "stream":"http://eightfour.libsyn.com/rss",
	      "image":"",
	      "name":"8-4 Play"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/castofkings",
	      "image":"",
	      "name":"A Cast of Kings - A Game of Thrones Podcast"
	   },
	   r'':{
	      "stream":"http://www.loyalbooks.com/book/a-christmas-carol-by-charles-dickens/feed",
	      "image":"",
	      "name":"A Christmas Carol by Charles Dickens"
	   },
	   r'':{
	      "stream":"http://carol.audiobooks.libsynpro.com/rss",
	      "image":"",
	      "name":"A Christmas Carol by Charles Dickens Audio Book"
	   },
	   r'':{
	      "stream":"http://www.bbc.co.uk/programmes/b00nrtd2/episodes/downloads.rss",
	      "image":"",
	      "name":"A History of the World in 100 Objects"
	   },
	   r'':{
	      "stream":"http://feeds.harvest.org/ANB",
	      "image":"",
	      "name":"A New Beginning with Greg Laurie"
	   },
	   r'':{
	      "stream":"https://feeds.publicradio.org/public_feeds/a-prairie-home-companion-highlights/itunes/rss",
	      "image":"",
	      "name":"A Prairie Home Companion Highlights"
	   },
	   r'':{
	      "stream":"http://podcast.armadamusic.com/asot/podcast.xml",
	      "image":"",
	      "name":"A State of Trance Official Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/AStormOfSpoilers",
	      "image":"",
	      "name":"A STORM OF SPOILERS - A Game Of Thrones Podcast"
	   },
	   r'':{
	      "stream":"http://asustainablemind.libsyn.com/rss",
	      "image":"",
	      "name":"A Sustainable Mind"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"A WAY TO GARDEN WITH MARGARET ROACH,"
	   },
	   r'':{
	      "stream":"http://feeds.waywordradio.org/awwwpodcast",
	      "image":"",
	      "name":"A Way with Words"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:62921190/sounds.rss",
	      "image":"",
	      "name":"a16z"
	   },
	   r'':{
	      "stream":"http://ltn.net.libsyn.com/aba",
	      "image":"",
	      "name":"ABA Journal Podcasts - Legal Talk Network"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/AboutBuildingsAndCities",
	      "image":"",
	      "name":"About Buildings + Cities"
	   },
	   r'':{
	      "stream":"http://static.aboveandbeyond.nu/grouptherapy/podcast.xml",
	      "image":"",
	      "name":"Above & Beyond: Group Therapy"
	   },
	   r'':{
	      "stream":"http://acceleratedspanishmasterofmemory.libsyn.com/rss",
	      "image":"",
	      "name":"Accelerated Spanish: Learn Spanish online the fastest and best way, by Master of Memory"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"Accidental Tech Podcast,"
	   },
	   r'':{
	      "stream":"http://halelrod.libsyn.com/rss",
	      "image":"",
	      "name":"Achieve Your Goals with Hal Elrod: Success | Productivity | Personal Development | Lifestyle | Business"
	   },
	   r'':{
	      "stream":"https://www.penny-arcade.com/feed/podcasts-ai",
	      "image":"",
	      "name":"Acquisitions Incorporated: The Series"
	   },
	   r'':{
	      "stream":"http://maximumfun.org/feeds/are.xml",
	      "image":"",
	      "name":"Adam Ruins Everything"
	   },
	   r'':{
	      "stream":"http://paulaandjaymoney.libsyn.com/rss",
	      "image":"",
	      "name":"Afford Anything | Make smart choices about your money, time and productivity"
	   },
	   r'':{
	      "stream":"http://podcast.aafp.org/rss/",
	      "image":"",
	      "name":"AFP: American Family Physician Podcast"
	   },
	   r'':{
	      "stream":"http://airlinepilotguy.com/podcast.xml",
	      "image":"",
	      "name":"Airline Pilot Guy - Aviation Podcast"
	   },
	   r'':{
	      "stream":"http://www.airplanegeeks.com/?feed=podcast",
	      "image":"",
	      "name":"Airplane Geeks Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/awatts",
	      "image":"",
	      "name":"Alan Watts"
	   },
	   r'':{
	      "stream":"http://aliceisntdead.libsyn.com/rss",
	      "image":"",
	      "name":"Alice Isn't Dead"
	   },
	   r'':{
	      "stream":"http://feed.cnet.com/feed/podcast/all/hd.xml",
	      "image":"",
	      "name":"All CNET Video Podcasts (HD)"
	   },
	   r'':{
	      "stream":"http://allearsenglish.libsyn.com/rss",
	      "image":"",
	      "name":"All Ears English Podcast | Real English Vocabulary | Conversation | American Culture"
	   },
	   r'':{
	      "stream":"http://www.navy.mil/podcast/NMCNradio/NMCNradio.xml",
	      "image":"",
	      "name":"All Hands Radio"
	   },
	   r'':{
	      "stream":"http://www.abc.net.au/radionational/feed/2888650/podcast.xml",
	      "image":"",
	      "name":"All In The Mind - ABC Radio National"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510019&uid=n1qe4e85742c986fdb81d2d38ffa0d5d53",
	      "image":"",
	      "name":"All Songs Considered"
	   },
	   r'':{
	      "stream":"http://allthebooks.libsyn.com/rss",
	      "image":"",
	      "name":"All the Books!"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/brickhouse.xml",
	      "image":"",
	      "name":"All TWiT.tv Shows (MP3)"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:157798900/sounds.rss",
	      "image":"",
	      "name":"Allegedly with Theo Von  & Matthew Cole Weiss"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510305",
	      "image":"",
	      "name":"Alt.Latino"
	   },
	   r'':{
	      "stream":"http://roosterteeth.com/show/always-open/feed/mp3",
	      "image":"",
	      "name":"Always Open"
	   },
	   r'':{
	      "stream":"https://owltail.github.io/redrock/feed-bo-ts.xml",
	      "image":"",
	      "name":"Amazing Podcast Episodes: ~3x curated episodes per week"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/AmericasTestKitchenRadio",
	      "image":"",
	      "name":"America's Test Kitchen Radio"
	   },
	   r'':{
	      "stream":"http://acu.libsyn.com/rss",
	      "image":"",
	      "name":"American Conservative University Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:211495990/sounds.rss",
	      "image":"",
	      "name":"American English Pronunciation Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/AnatomyForEM",
	      "image":"",
	      "name":"Anatomy For Emergency Medicine"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/AndyStanleyLeadershipPodcast",
	      "image":"",
	      "name":"Andy Stanley Leadership Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:143463073/sounds.rss",
	      "image":"",
	      "name":"Angela Yee's Lip Service"
	   },
	   r'':{
	      "stream":"http://feeds2.feedburner.com/AnnalsPodcast",
	      "image":"",
	      "name":"Annals of Internal Medicine Podcast"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/anotherround",
	      "image":"",
	      "name":"Another Round"
	   },
	   r'':{
	      "stream":"http://theartofcharmpodcast.theartofcharm.libsynpro.com/rss",
	      "image":"",
	      "name":"AoC | Social Science | Cognitive Psychology | Confidence | Relationship Advice | Behavioral Economics | Biohacking | Productivi"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/aokishouse",
	      "image":"",
	      "name":"AOKI'S HOUSE"
	   },
	   r'':{
	      "stream":"http://americanpublicmedia.publicradio.org/podcasts/xml/prairie_home_companion/news_from_lake_wobegon.xml",
	      "image":"",
	      "name":"APM: A Prairie Home Companion's News from Lake Wobegon"
	   },
	   r'':{
	      "stream":"http://crazymikesapps.com/feed/podcast/",
	      "image":"",
	      "name":"App Reviews for iPhone, iPad and Android Apps"
	   },
	   r'':{
	      "stream":"http://feed.cnet.com/feed/podcast/apple-byte/hd.xml",
	      "image":"",
	      "name":"Apple Byte (HD)"
	   },
	   r'':{
	      "stream":"http://feed.cnet.com/feed/podcast/apple-byte-audio.xml",
	      "image":"",
	      "name":"Apple Byte: Extra Crunchy (MP3)"
	   },
	   r'':{
	      "stream":"http://podcasts.apple.com/apple_keynotes/apple_keynotes.xml",
	      "image":"",
	      "name":"Apple Keynotes"
	   },
	   r'':{
	      "stream":"http://podcasts.apple.com/apple_keynotes_1080p/apple_keynotes_1080p.xml",
	      "image":"",
	      "name":"Apple Keynotes (1080p)"
	   },
	   r'':{
	      "stream":"http://podcasts.apple.com/apple_keynotes_hd/apple_keynotes_hd.xml",
	      "image":"",
	      "name":"Apple Keynotes (HD)"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/imore-apple-talk",
	      "image":"",
	      "name":"Apple Talk"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:78650636/sounds.rss",
	      "image":"",
	      "name":"AppleInsider Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/atvpodcast",
	      "image":"",
	      "name":"Appointment Television"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:213324253/sounds.rss",
	      "image":"",
	      "name":"Archive 81"
	   },
	   r'':{
	      "stream":"http://shaffir1.libsyn.com/rss",
	      "image":"",
	      "name":"Ari Shaffir's Skeptic Tank"
	   },
	   r'':{
	      "stream":"http://feeds.armedamericanradio.org/ArmedAmericanRadio",
	      "image":"",
	      "name":"Armed American Radio"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=2839445",
	      "image":"",
	      "name":"Around the Horn"
	   },
	   r'':{
	      "stream":"http://aroundtheleague.libsyn.com/rss",
	      "image":"",
	      "name":"Around the NFL"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"ars PARADOXICA,"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:98602096/sounds.rss",
	      "image":"",
	      "name":"Art of Wrestling"
	   },
	   r'':{
	      "stream":"http://feed.desiringgod.org/ask-pastor-john.rss",
	      "image":"",
	      "name":"Ask Pastor John"
	   },
	   r'':{
	      "stream":"http://asksciencemike.podbean.com/feed/",
	      "image":"",
	      "name":"Ask Science Mike"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4322549.rss",
	      "image":"",
	      "name":"Astonishing Legends"
	   },
	   r'':{
	      "stream":"http://www.astronomy.ohio-state.edu/~pogge/Ast161/Audio/Podcast.xml",
	      "image":"",
	      "name":"Astronomy 161 - Introduction to Solar System Astronomy"
	   },
	   r'':{
	      "stream":"http://www.astronomycast.com/mp3.xml",
	      "image":"",
	      "name":"Astronomy Cast"
	   },
	   r'':{
	      "stream":"http://sallyclarkson.libsyn.com/rss",
	      "image":"",
	      "name":"At Home With Sally"
	   },
	   r'':{
	      "stream":"http://warriorpoet.libsyn.com/rss",
	      "image":"",
	      "name":"Aubrey Marcus Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/audiodharma",
	      "image":"",
	      "name":"Audio Dharma"
	   },
	   r'':{
	      "stream":"http://www.autoblog.com/category/podcasts/rss.xml",
	      "image":"",
	      "name":"Autoblog Podcasts"
	   },
	   r'':{
	      "stream":"https://simplecast.com/podcasts/1396/rss",
	      "image":"",
	      "name":"Awards Chatter"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:206714635/sounds.rss",
	      "image":"",
	      "name":"AWS Podcast"
	   },
	   r'':{
	      "stream":"http://bloodgodpod.libsyn.com/rss",
	      "image":"",
	      "name":"Axe of the Blood God: USgamer's Official RPG Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.5by5.tv/b2w",
	      "image":"",
	      "name":"Back to Work"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=969",
	      "image":"",
	      "name":"Backseat Rider"
	   },
	   r'':{
	      "stream":"http://balancedbites.libsyn.com/rss",
	      "image":"",
	      "name":"Balanced Bites: Modern paleo living with Diane Sanfilippo & Liz Wolfe."
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:202224578/sounds.rss",
	      "image":"",
	      "name":"Banging Book Club"
	   },
	   r'':{
	      "stream":"http://barbellshrugged.libsyn.com/rss",
	      "image":"",
	      "name":"Barbell Shrugged - Talking Training w/ CrossFit Games Athletes, Strength Coaches & More"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/BarefootBooksPodcastipod",
	      "image":"",
	      "name":"Barefoot Books Podcast (iPod)"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/BarstoolRundown",
	      "image":"",
	      "name":"Barstool Rundown"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=2386164",
	      "image":"",
	      "name":"Baseball Tonight with Buster Olney"
	   },
	   r'':{
	      "stream":"https://ww2.kqed.org/news/category/bay-curious-podcast/feed/podcast",
	      "image":"",
	      "name":"Bay Curious"
	   },
	   r'':{
	      "stream":"http://www.bbc.co.uk/programmes/b036f7w2/episodes/downloads.rss",
	      "image":"",
	      "name":"BBC Inside Science"
	   },
	   r'':{
	      "stream":"http://rachaelobriencomedy.libsyn.com/rss",
	      "image":"",
	      "name":"Be Here For A While"
	   },
	   r'':{
	      "stream":"http://rss.earwolf.com/beautiful-anonymous",
	      "image":"",
	      "name":"Beautiful Stories From Anonymous People"
	   },
	   r'':{
	      "stream":"http://beautyinsideout.libsyn.com/rss",
	      "image":"",
	      "name":"Beauty Inside Out with Kimberly Snyder"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/supermale",
	      "image":"",
	      "name":"Becoming a Super Male"
	   },
	   r'':{
	      "stream":"http://www.onbeing.org/podcasts/becoming-wise.xml",
	      "image":"",
	      "name":"Becoming Wise"
	   },
	   r'':{
	      "stream":"http://talesfromthelilypad.podbean.com/feed/",
	      "image":"",
	      "name":"Bedtime Stories Fairytales and Folk Tales from the Lilypad for kids"
	   },
	   r'':{
	      "stream":"http://beersmith.com/content/feed/podcast/",
	      "image":"",
	      "name":"BeerSmith Home and Beer Brewing Podcast"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=5395837",
	      "image":"",
	      "name":"Behind the Bets"
	   },
	   r'':{
	      "stream":"http://behindtheknife.libsyn.com/rss",
	      "image":"",
	      "name":"Behind The Knife: The Surgery Podcast"
	   },
	   r'':{
	      "stream":"http://bengreenfieldfitness.libsyn.com/rss",
	      "image":"",
	      "name":"Ben Greenfield Fitness: Diet, Fat Loss and Performance"
	   },
	   r'':{
	      "stream":"http://bertcast.libsyn.com/rss",
	      "image":"",
	      "name":"Bertcast's podcast"
	   },
	   r'':{
	      "stream":"http://bestofotr.rnn.beta.libsynpro.com/rss",
	      "image":"",
	      "name":"Best of Old Time Radio"
	   },
	   r'':{
	      "stream":"http://bmoore86456.podomatic.com/rss2.xml",
	      "image":"",
	      "name":"Beth Moore's Podcast"
	   },
	   r'':{
	      "stream":"http://podcasts.ibethel.org/en/podcasts.rss",
	      "image":"",
	      "name":"Bethel Church Sermon of the Week"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/beyondthetodolist",
	      "image":"",
	      "name":"Beyond the To Do List | Personal Productivity Perspectives"
	   },
	   r'':{
	      "stream":"http://rss.art19.com/beyond-yacht-rock",
	      "image":"",
	      "name":"Beyond Yacht Rock"
	   },
	   r'':{
	      "stream":"http://feeds.tvo.org/tvobigideas",
	      "image":"",
	      "name":"Big Ideas (Audio)"
	   },
	   r'':{
	      "stream":"http://arewealone.libsyn.com/rss",
	      "image":"",
	      "name":"Big Picture Science"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/RealEstateNewsForReal",
	      "image":"",
	      "name":"BiggerPockets Podcast : Real Estate Investing and Wealth Building to Help You Get Bigger Pockets"
	   },
	   r'':{
	      "stream":"http://www.latrobe.edu.au/marketing/assets/podcasts/rssfeeds/biography.xml",
	      "image":"",
	      "name":"Biography"
	   },
	   r'':{
	      "stream":"http://faculty.css.edu/gcizadlo/podcast/ap0809/anatphys0809.xml",
	      "image":"",
	      "name":"Biology 2110-2120: Anatomy and Physiology with Doc C"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4785680.rss",
	      "image":"",
	      "name":"Bischoff on Wrestling"
	   },
	   r'':{
	      "stream":"http://rss.earwolf.com/bitch-sesh",
	      "image":"",
	      "name":"Bitch Sesh: A Real Housewives Breakdown"
	   },
	   r'':{
	      "stream":"http://blackagendaradio.podbean.com/feed/",
	      "image":"",
	      "name":"Black Agenda Radio"
	   },
	   r'':{
	      "stream":"https://simplecast.com/podcasts/1996/rss",
	      "image":"",
	      "name":"Black Girl In Om"
	   },
	   r'':{
	      "stream":"https://www.spreaker.com/show/1502744/episodes/feed",
	      "image":"",
	      "name":"Black Girls Talking"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/BlackListTableReads",
	      "image":"",
	      "name":"Black List Table Reads"
	   },
	   r'':{
	      "stream":"http://urbanshooter.libsyn.com/rss",
	      "image":"",
	      "name":"Black Man With A Gun"
	   },
	   r'':{
	      "stream":"http://www.bloomberg.com/feeds/podcasts/benchmark.xml",
	      "image":"",
	      "name":"Bloomberg Benchmark"
	   },
	   r'':{
	      "stream":"http://www.bloomberg.com/feeds/podcasts/surveillance.xml",
	      "image":"",
	      "name":"Bloomberg Surveillance"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/BlurryPhotos",
	      "image":"",
	      "name":"Blurry Photos"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:169774121/sounds.rss",
	      "image":"",
	      "name":"Bodega Boys"
	   },
	   r'':{
	      "stream":"http://feeds.duckfeed.tv/bsc",
	      "image":"",
	      "name":"Bonfireside Chat - A Dark Souls and Bloodborne Podcast"
	   },
	   r'':{
	      "stream":"http://boxcars711.podomatic.com/rss2.xml",
	      "image":"",
	      "name":"Boxcars711 Old Time Radio Pod"
	   },
	   r'':{
	      "stream":"http://brainpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Brain Matters"
	   },
	   r'':{
	      "stream":"http://brainsciencepodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Brain Science with Ginger Campbell, MD: Neuroscience for Everyone"
	   },
	   r'':{
	      "stream":"https://feeds.publicradio.org/public_feeds/brains-on/itunes/rss",
	      "image":"",
	      "name":"Brains On! Science podcast for kids"
	   },
	   r'':{
	      "stream":"http://www.howstuffworks.com/podcasts/brainstuff.rss",
	      "image":"",
	      "name":"BrainStuff"
	   },
	   r'':{
	      "stream":"http://brandinglikeaboss.libsyn.com/rss",
	      "image":"",
	      "name":"Branding Like A Boss"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=592",
	      "image":"",
	      "name":"Bret Easton Ellis Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/hillsong/podcast",
	      "image":"",
	      "name":"Brian Houston Podcast"
	   },
	   r'':{
	      "stream":"http://broadwaybackstory.libsyn.com/rss",
	      "image":"",
	      "name":"Broadway Backstory"
	   },
	   r'':{
	      "stream":"http://brookingsevents.libsyn.com/rss",
	      "image":"",
	      "name":"Brookings Events"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:210076721/sounds.rss",
	      "image":"",
	      "name":"Bruce Lee Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:36655593/sounds.rss",
	      "image":"",
	      "name":"Buddhist Geeks"
	   },
	   r'':{
	      "stream":"http://bufferingthevampireslayer.libsyn.com/rss",
	      "image":"",
	      "name":"Buffering the Vampire Slayer"
	   },
	   r'':{
	      "stream":"http://chalenejohnson.libsyn.com/rss",
	      "image":"",
	      "name":"Build Your Tribe | Creating Community | Email List Building | Internet Marketing Social Media"
	   },
	   r'':{
	      "stream":"http://storybrand.libsyn.com/rss",
	      "image":"",
	      "name":"Building a Story Brand with Donald Miller | Clarify Your Message and Grow Your Business"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=806",
	      "image":"",
	      "name":"Bulletproof Radio"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510309",
	      "image":"",
	      "name":"Bullseye with Jesse Thorn"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/businessenglishpod",
	      "image":"",
	      "name":"Business English Pod :: Learn Business English Online"
	   },
	   r'':{
	      "stream":"http://feedpress.me/vpr-but-why",
	      "image":"",
	      "name":"But Why: A Podcast for Curious Kids"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/internetexplorer",
	      "image":"",
	      "name":"BuzzFeed's Internet Explorer"
	   },
	   r'':{
	      "stream":"https://www.cheapassgamer.com/podcast/cagcast.xml",
	      "image":"",
	      "name":"CAGcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/CallChelseaPeretti",
	      "image":"",
	      "name":"Call Chelsea Peretti"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/callyourgirlfriend",
	      "image":"",
	      "name":"Call Your Girlfriend"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/CarCast",
	      "image":"",
	      "name":"CarCast"
	   },
	   r'':{
	      "stream":"http://podcasts.grantcardone.com/xml/cardonezone.xml",
	      "image":"",
	      "name":"Cardone Zone"
	   },
	   r'':{
	      "stream":"http://careerdayshow.libsyn.com/rss",
	      "image":"",
	      "name":"Career Day"
	   },
	   r'':{
	      "stream":"http://www.carnegiecouncil.org/resources/audio/rss/feed.xml",
	      "image":"",
	      "name":"Carnegie Council Audio Podcast"
	   },
	   r'':{
	      "stream":"http://www.howstuffworks.com/podcasts/carstuff.rss",
	      "image":"",
	      "name":"CarStuff"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/catholic/cal",
	      "image":"",
	      "name":"Catholic Answers Live"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/catholicstuffpodcast/DpqF",
	      "image":"",
	      "name":"Catholic Stuff You Should Know"
	   },
	   r'':{
	      "stream":"http://podcasts.cstv.com/feeds/mensbasketball.xml",
	      "image":"",
	      "name":"CBS Sports Eye On College Basketball Podcast"
	   },
	   r'':{
	      "stream":"http://celticchristmaspodcast.com/rss",
	      "image":"",
	      "name":"Celtic Christmas Podcast"
	   },
	   r'':{
	      "stream":"http://cgpgrey.libsyn.com/rss",
	      "image":"",
	      "name":"CGP Grey"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/Channel33",
	      "image":"",
	      "name":"Channel 33"
	   },
	   r'':{
	      "stream":"http://chatwithtraders.libsyn.com/rss",
	      "image":"",
	      "name":"Chat With Traders | Weekly interviews with profitable & successful stock market traders."
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/feeds/rss/podcast.xml?id=10116533",
	      "image":"",
	      "name":"Cheap Heat"
	   },
	   r'':{
	      "stream":"http://www.curiosoft.com/news/podcasts/storytimepodcasts.xml",
	      "image":"",
	      "name":"Children's Fun Storytime Podcast"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"China in the World,"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=720",
	      "image":"",
	      "name":"Chive Podcast"
	   },
	   r'':{
	      "stream":"http://chrishogan.ramsey.libsynpro.com/itunes",
	      "image":"",
	      "name":"Chris Hogan's Retire Inspired"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"Christmas & Holiday Ringtones, Text Alert Message Tones, Music Songs Alarms - Audio Wallpapers,"
	   },
	   r'':{
	      "stream":"http://www.shilohworshipmusic.com/ShilohWorshipMusic/Christmas_Carols,_Hymns_and_Songs_Free/rss.xml",
	      "image":"",
	      "name":"Christmas Carols, Hymns and Songs Free"
	   },
	   r'':{
	      "stream":"http://www.christmasmusic247.com/cm247.xml",
	      "image":"",
	      "name":"Christmas Carols, Music and Songs"
	   },
	   r'':{
	      "stream":"http://christmas.rnn.libsynpro.com/rss",
	      "image":"",
	      "name":"Christmas Old Time Radio"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/blogspot/WfiDt",
	      "image":"",
	      "name":"Christmas Songs"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ChristmasSongsMusicAndCarols",
	      "image":"",
	      "name":"Christmas Songs, Music and Carols"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/InStereoRadioShow",
	      "image":"",
	      "name":"Chus & Ceballos presents Stereo Productions Podcast"
	   },
	   r'':{
	      "stream":"https://www.houstonpublicmedia.org/podcasts/classical-classroom/",
	      "image":"",
	      "name":"Classical Classroom | Houston Public Media"
	   },
	   r'':{
	      "stream":"http://rss.dw.com/xml/podcast_classical-masterpieces",
	      "image":"",
	      "name":"Classical Masterpieces | Deutsche Welle"
	   },
	   r'':{
	      "stream":"http://www.wgbh.org/online/clas/clas_performance.xml",
	      "image":"",
	      "name":"Classical Performance Podcast"
	   },
	   r'':{
	      "stream":"http://www.classicsforkids.com/podcasts/classicsforkids.xml",
	      "image":"",
	      "name":"Classics For Kids"
	   },
	   r'':{
	      "stream":"http://feed.cnet.com/feed/podcast/first-look/hd.xml",
	      "image":"",
	      "name":"CNET First Look (HD)"
	   },
	   r'':{
	      "stream":"http://feed.cnet.com/feed/podcast/how-to-video/hd.xml",
	      "image":"",
	      "name":"CNET How To (HD)"
	   },
	   r'':{
	      "stream":"http://feed.cnet.com/feed/podcast/cnet-news/hd.xml",
	      "image":"",
	      "name":"CNET News (HD)"
	   },
	   r'':{
	      "stream":"http://feed.cnet.com/feed/podcast/special-features/hd.xml",
	      "image":"",
	      "name":"CNET Special Features (HD)"
	   },
	   r'':{
	      "stream":"http://feed.cnet.com/feed/podcast/cnet-top-5/hd.xml",
	      "image":"",
	      "name":"CNET Top 5 (HD)"
	   },
	   r'':{
	      "stream":"http://feed.cnet.com/feed/podcast/cnet-update/hd.xml",
	      "image":"",
	      "name":"CNET Update (HD)"
	   },
	   r'':{
	      "stream":"http://rss.cnn.com/services/podcasting/studentnews/rss.xml",
	      "image":"",
	      "name":"CNN Student News (video)"
	   },
	   r'':{
	      "stream":"http://coachingforleaders.com/podcast/feed/",
	      "image":"",
	      "name":"Coaching for Leaders - Talent Management | Leadership Strategy | Communication | Productivity | Executive Development"
	   },
	   r'':{
	      "stream":"http://www.glennhughes.com/ctc/podcast/podcast.xml",
	      "image":"",
	      "name":"Coast To Coast Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/CodebreakerByMarketplaceAndTechInsider",
	      "image":"",
	      "name":"Codebreaker"
	   },
	   r'':{
	      "stream":"http://feeds.codenewbie.org/cnpodcast.xml",
	      "image":"",
	      "name":"CodeNewbie"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/tBPkjrcL0_m0",
	      "image":"",
	      "name":"Coding Blocks | Software and Web Programming / Security / Best Practices / Microsoft .NET"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/coffeebreakfrench",
	      "image":"",
	      "name":"Coffee Break French"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/coffeebreakgerman",
	      "image":"",
	      "name":"Coffee Break German"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/coffeebreakitalian",
	      "image":"",
	      "name":"Coffee Break Italian"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/coffeebreakspanish",
	      "image":"",
	      "name":"Coffee Break Spanish"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=13250702",
	      "image":"",
	      "name":"College Football Live"
	   },
	   r'':{
	      "stream":"http://amcmovietalk.libsyn.com/rss",
	      "image":"",
	      "name":"Collider  (Audio Edition - All Shows)"
	   },
	   r'':{
	      "stream":"http://cupodcast.podbean.com/feed/",
	      "image":"",
	      "name":"Completely Unnecessary Podcast"
	   },
	   r'':{
	      "stream":"http://content.complex.com/podcasts/desusvsmero/feeds.rss",
	      "image":"",
	      "name":"Complex Presents: Desus vs. Mero"
	   },
	   r'':{
	      "stream":"http://buildgreatminds.com/feed/podcast/",
	      "image":"",
	      "name":"Conscious Parenting For Confident & Successful Kids // Similar to Focus on the Family, Parental Guidance, TEDTalks"
	   },
	   r'':{
	      "stream":"http://www.buzzsprout.com/73426.rss",
	      "image":"",
	      "name":"Conservation Federation"
	   },
	   r'':{
	      "stream":"https://www.buzzsprout.com/43525.rss",
	      "image":"",
	      "name":"Contracting Officer Podcast: Government Contracting, proposal management, proposal writing, governmental contracting, targeting"
	   },
	   r'':{
	      "stream":"http://conversioncast.libsyn.com/rss",
	      "image":"",
	      "name":"ConversionCast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/CoolGamesInc",
	      "image":"",
	      "name":"CoolGames Inc"
	   },
	   r'':{
	      "stream":"http://feeds.frogpants.com/core_feed.xml",
	      "image":"",
	      "name":"CORE - A Heroes of The Storm podcast!"
	   },
	   r'':{
	      "stream":"https://www.relay.fm/cortex/feed",
	      "image":"",
	      "name":"Cortex"
	   },
	   r'':{
	      "stream":"http://councilonhumanfunction.libsyn.com/rss",
	      "image":"",
	      "name":"Council On Human Function Podcast"
	   },
	   r'':{
	      "stream":"http://feedpress.me/CGLeadershipAudioiTunes",
	      "image":"",
	      "name":"Craig Groeschel Leadership Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/CreativeDogTrainingOnline",
	      "image":"",
	      "name":"Creative Dog Training Online Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:87660023/sounds.rss",
	      "image":"",
	      "name":"Creative Pep Talk"
	   },
	   r'':{
	      "stream":"http://feed.theplatform.com/f/IfSiAC/p5z4rSbJ7OuA",
	      "image":"",
	      "name":"Creflo Dollar Ministries Audio Podcast"
	   },
	   r'':{
	      "stream":"https://rss.art19.com/crime-writers-on",
	      "image":"",
	      "name":"Crime Writers On..."
	   },
	   r'':{
	      "stream":"http://www.majorspoilers.com/media/criticalhit.xml",
	      "image":"",
	      "name":"Critical Hit: A Dungeons and Dragons Campaign"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/CrucibleRadio",
	      "image":"",
	      "name":"Crucible Radio"
	   },
	   r'':{
	      "stream":"https://rss.art19.com/ctrl-walt-delete",
	      "image":"",
	      "name":"Ctrl-Walt-Delete"
	   },
	   r'':{
	      "stream":"http://boldturquoise.com/feed/podcast/",
	      "image":"",
	      "name":"Cultivating the Lovely- The Podcast"
	   },
	   r'':{
	      "stream":"http://shoutengine.com/CumTown.xml",
	      "image":"",
	      "name":"Cum Town"
	   },
	   r'':{
	      "stream":"http://thedailymeditationpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Daily Meditation Podcast"
	   },
	   r'':{
	      "stream":"https://www.intouch.org/listen/podcast/today-on-radio",
	      "image":"",
	      "name":"Daily Radio Program with Charles Stanley - In Touch Ministries"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/DailyTechNewsShow",
	      "image":"",
	      "name":"Daily Tech News Show"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/dansnowshistoryhit",
	      "image":"",
	      "name":"Dan Snow's HISTORY HIT"
	   },
	   r'':{
	      "stream":"https://rss.art19.com/dark-tome",
	      "image":"",
	      "name":"Dark Tome"
	   },
	   r'':{
	      "stream":"http://darkestnight.libsyn.com/rss",
	      "image":"",
	      "name":"Darkest Night"
	   },
	   r'':{
	      "stream":"http://twincitiesnewstalk.iheart.com/podcast/itunes/darknessradio_itunes.xml",
	      "image":"",
	      "name":"Darkness Radio"
	   },
	   r'':{
	      "stream":"http://worldofpiggy.com/podcast.xml",
	      "image":"",
	      "name":"Data Science at Home"
	   },
	   r'':{
	      "stream":"http://dataskeptic.libsyn.com/rss",
	      "image":"",
	      "name":"Data Skeptic"
	   },
	   r'':{
	      "stream":"http://deadpilotssociety.libsyn.com/rss",
	      "image":"",
	      "name":"Dead Pilots Society"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:156542883/sounds.rss",
	      "image":"",
	      "name":"Dear Hank and John"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/HarryPotterSeminar",
	      "image":"",
	      "name":"Dear Mr. Potter: A Harry Potter Seminar"
	   },
	   r'':{
	      "stream":"http://feeds.wbur.org/dearsugar/podcast?feed=podcast",
	      "image":"",
	      "name":"Dear Sugar"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:259871793/sounds.rss",
	      "image":"",
	      "name":"Decoding Westworld"
	   },
	   r'':{
	      "stream":"http://chriswinfield.libsyn.com/rss",
	      "image":"",
	      "name":"Deconstructing Success with Chris Winfield"
	   },
	   r'':{
	      "stream":"http://www.bloomberg.com/feeds/podcasts/decrypted.xml",
	      "image":"",
	      "name":"Decrypted"
	   },
	   r'':{
	      "stream":"http://feeds.djpod.com/djfdb",
	      "image":"",
	      "name":"Deejay FDB - PODCAST"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/DeepEnergy-MusicForMeditationRelaxationMassageAndYoga",
	      "image":"",
	      "name":"Deep Energy 2.0 - Music for Sleep, Meditation, Relaxation, Massage and Yoga"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/PhilDahouseCat",
	      "image":"",
	      "name":"Deep House Cat"
	   },
	   r'':{
	      "stream":"http://www.blogtalkradio.com/deepakchopra/podcast",
	      "image":"",
	      "name":"Deepak Chopra Radio"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/dsoh",
	      "image":"",
	      "name":"Deeper Shades of House - Deep House Podcast with Lars Behrenroth"
	   },
	   r'':{
	      "stream":"http://www.defensivesecurity.org/feed/podcast/",
	      "image":"",
	      "name":"Defensive Security Podcast - Malware, Hacking, Cyber Security & Infosec"
	   },
	   r'':{
	      "stream":"https://simplecast.com/podcasts/1034/rss",
	      "image":"",
	      "name":"Design Details"
	   },
	   r'':{
	      "stream":"http://designobserver.com/show.designmatters2009-10.xml",
	      "image":"",
	      "name":"Design Matters with Debbie Millman: 2009-2016"
	   },
	   r'':{
	      "stream":"http://podcasts.universalstudioshomeentertainment.com/despicableme/despicablememetadata.xml",
	      "image":"",
	      "name":"Despicable Me"
	   },
	   r'':{
	      "stream":"http://podcasts.universalstudioshomeentertainment.com/DespicableMe2/dm2_podcast3.xml",
	      "image":"",
	      "name":"Despicable Me 2"
	   },
	   r'':{
	      "stream":"http://DestinyCommunityPodcast.podbean.com/feed/",
	      "image":"",
	      "name":"Destiny Community Podcast"
	   },
	   r'':{
	      "stream":"http://detectiveotr.rnn.libsynpro.com/rss",
	      "image":"",
	      "name":"Detective OTR"
	   },
	   r'':{
	      "stream":"http://rss.dw.com/xml/DKpodcast_dwn1_en",
	      "image":"",
	      "name":"Deutsch - warum nicht? Series 1 | Learning German | Deutsche Welle"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/DeveloperTea",
	      "image":"",
	      "name":"Developer Tea"
	   },
	   r'':{
	      "stream":"http://www.dharmaseed.org/feeds/recordings/",
	      "image":"",
	      "name":"Dharmaseed.org: dharma talks and meditation instruction"
	   },
	   r'':{
	      "stream":"http://energy.gov/podcasts/direct-current-energygov-podcast?format=itunes",
	      "image":"",
	      "name":"Direct Current - An Energy.gov Podcast"
	   },
	   r'':{
	      "stream":"http://www.bbc.co.uk/programmes/p002w557/episodes/downloads.rss",
	      "image":"",
	      "name":"Discovery"
	   },
	   r'':{
	      "stream":"https://www.cityscoutmag.com/feed/dissect",
	      "image":"",
	      "name":"Dissect - A Serialized Music Podcast"
	   },
	   r'':{
	      "stream":"http://radiofrance-podcast.net/podcast09/rss_14928.xml",
	      "image":"",
	      "name":"Dites le en Marseillais France Bleu Provence"
	   },
	   r'':{
	      "stream":"http://divefilmhd.com/podcasts/podcast.xml",
	      "image":"",
	      "name":"DiveFilm HD Video"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/cdbabydiymusicpodcast",
	      "image":"",
	      "name":"DIY Musician Podcast"
	   },
	   r'':{
	      "stream":"http://djjucrazy.libsyn.com/rss",
	      "image":"",
	      "name":"Dj Ju Crazy"
	   },
	   r'':{
	      "stream":"http://djprivateryan.libsyn.com/rss",
	      "image":"",
	      "name":"DJ Private Ryan's Podcast"
	   },
	   r'':{
	      "stream":"http://djtouchtone.podOmatic.com/rss2.xml",
	      "image":"",
	      "name":"DJ TOUCH TONE MUSIC BLOG"
	   },
	   r'':{
	      "stream":"http://feeds.5by5.tv/dlc",
	      "image":"",
	      "name":"DLC"
	   },
	   r'':{
	      "stream":"https://www.thisisdistorted.com/repository/xml/DonDiabloHexagonRadio1422895802.xml",
	      "image":"",
	      "name":"Don Diablo Presents Hexagon Radio"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/DougLovesMovies",
	      "image":"",
	      "name":"Doug Loves Movies"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/LeadershipUniversityPodcast",
	      "image":"",
	      "name":"Dr. Henry Cloud's Leadership University Podcast"
	   },
	   r'':{
	      "stream":"http://drwaynedyer.hayhouse.libsynpro.com/rss",
	      "image":"",
	      "name":"Dr. Wayne W. Dyer Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/dragonballsuperonline",
	      "image":"",
	      "name":"Dragon Ball Super Online"
	   },
	   r'':{
	      "stream":"http://www.wizards.com/dnd/rsspodcast.xml",
	      "image":"",
	      "name":"Dragon Talk - An Official Dungeons & Dragons Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:182624645/sounds.rss",
	      "image":"",
	      "name":"DragonBallerZ : a Dragonball Z Podcast | an NthCast Production"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=981",
	      "image":"",
	      "name":"Dreadtime Stories with Malcolm McDowell"
	   },
	   r'':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1441?format=MP3_128K",
	      "image":"",
	      "name":"Drink Champs"
	   },
	   r'':{
	      "stream":"http://drinkingbros.libsyn.com/rss",
	      "image":"",
	      "name":"Drinkin' Bros."
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/DnDPodcast",
	      "image":"",
	      "name":"Drunks and Dragons - Dungeons and Dragons 5e Actual Play"
	   },
	   r'':{
	      "stream":"http://funhaus.roosterteeth.com/show/dude-soup/feed/mp3",
	      "image":"",
	      "name":"Dude Soup"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/dumbgaypolitics",
	      "image":"",
	      "name":"Dumb, Gay Politics"
	   },
	   r'':{
	      "stream":"http://www.blogtalkradio.com/duncdon/podcast",
	      "image":"",
	      "name":"Dunc'd On Basketball Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/DuncanTrussell",
	      "image":"",
	      "name":"Duncan Trussell Family Hour"
	   },
	   r'':{
	      "stream":"http://dungeonmasterblock.podbean.com/feed/",
	      "image":"",
	      "name":"Dungeon Master's Block"
	   },
	   r'':{
	      "stream":"http://dungeonsandrandomness.podbean.com/feed/",
	      "image":"",
	      "name":"Dungeons and Randomness: A D&D Podcast"
	   },
	   r'':{
	      "stream":"http://teamrwb.libsyn.com/rss",
	      "image":"",
	      "name":"Eagle Nation Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:59736920/sounds.rss",
	      "image":"",
	      "name":"Ear Biscuits"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/EarnYouHappy",
	      "image":"",
	      "name":"Earn Your Happy Podcast | Motivation | Self-Love | Entrepreneurship | Confidence | Fitness and Life Coaching with Lori Harder"
	   },
	   r'':{
	      "stream":"http://files.libertyfund.org/econtalk/EconTalk.xml",
	      "image":"",
	      "name":"EconTalk"
	   },
	   r'':{
	      "stream":"http://edmylett.libsyn.com/rss",
	      "image":"",
	      "name":"ED MYLETT SHOW"
	   },
	   r'':{
	      "stream":"http://www.baseballprospectus.com/blog/daily_podcast/feed.xml",
	      "image":"",
	      "name":"Effectively Wild: The Daily Baseball Prospectus Podcast"
	   },
	   r'':{
	      "stream":"http://effortlessenglish.libsyn.com/rss",
	      "image":"",
	      "name":"Effortless English Podcast"
	   },
	   r'':{
	      "stream":"http://electioncollege.libsyn.com/rss",
	      "image":"",
	      "name":"Election College | Presidential Election History"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ElevationChurchCharlotte",
	      "image":"",
	      "name":"Elevation Church Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/elevationipod",
	      "image":"",
	      "name":"Elevation Church Podcast"
	   },
	   r'':{
	      "stream":"http://eleventylife.libsyn.com/rss",
	      "image":"",
	      "name":"eleventylife"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:255132557/sounds.rss",
	      "image":"",
	      "name":"ELLISTRONICS"
	   },
	   r'':{
	      "stream":"http://downloads.cdn.sesame.org/podcast/outreach/english_rss.xml",
	      "image":"",
	      "name":"Elmo's Adventures in Spending, Saving, and Sharing"
	   },
	   r'':{
	      "stream":"http://embasic.libsyn.com/rss",
	      "image":"",
	      "name":"EM Basic"
	   },
	   r'':{
	      "stream":"http://emcrit.org/feed/podcast/",
	      "image":"",
	      "name":"EMCrit Podcast - Critical Care and Resuscitation"
	   },
	   r'':{
	      "stream":"https://emergencymedicinecases.com/feed/podcast/",
	      "image":"",
	      "name":"Emergency Medicine Cases"
	   },
	   r'':{
	      "stream":"https://www2c.cdc.gov/podcasts/createrss.asp?t=a&c=49",
	      "image":"",
	      "name":"Emerging Infectious Diseases"
	   },
	   r'':{
	      "stream":"http://www.latrobe.edu.au/marketing/assets/podcasts/rssfeeds/caesar.xml",
	      "image":"",
	      "name":"Emperors of Rome"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/EnglishAsASecondLanguagePodcast",
	      "image":"",
	      "name":"English as a Second Language (ESL) Podcast - Learn English Online"
	   },
	   r'':{
	      "stream":"http://simplerhappierlifepodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Enjoying Life On A Budget Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/enoughaboutmepodcast",
	      "image":"",
	      "name":"Enough About Me with Kirk Minihane"
	   },
	   r'':{
	      "stream":"http://web.stanford.edu/group/edcorner/uploads/podcast/EducatorsCorner.xml",
	      "image":"",
	      "name":"Entrepreneurial Thought Leaders"
	   },
	   r'':{
	      "stream":"http://entrepreneuronfire.libsyn.com/rss",
	      "image":"",
	      "name":"EOFire | Entrepreneur on FIRE | Chats with Tim Ferriss, Gary Vaynerchuk, Tony Robbins and inspiring Entrepreneurs 7-days a week"
	   },
	   r'':{
	      "stream":"http://eprei.libsyn.com/rss",
	      "image":"",
	      "name":"Epic Real Estate Investing"
	   },
	   r'':{
	      "stream":"http://www.eslpod.com/past.xml",
	      "image":"",
	      "name":"ESL Podcast - Previous Episodes"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/feeds/rss/podcast.xml?id=10672984",
	      "image":"",
	      "name":"ESPN FC"
	   },
	   r'':{
	      "stream":"http://www.rand.org/multimedia/podcasts/xml/events-at-rand.xml",
	      "image":"",
	      "name":"Events @ RAND"
	   },
	   r'':{
	      "stream":"http://shoutengine.com/EverydayDriverCarDebate.xml",
	      "image":"",
	      "name":"Everyday Driver Car Debate"
	   },
	   r'':{
	      "stream":"http://www.goldmansachs.com/exchanges-podcast/feed.rss",
	      "image":"",
	      "name":"Exchanges at Goldman Sachs"
	   },
	   r'':{
	      "stream":"http://explainthingstome.libsyn.com/rss",
	      "image":"",
	      "name":"Explain Things To Me"
	   },
	   r'':{
	      "stream":"http://exponent.fm/feed/",
	      "image":"",
	      "name":"Exponent"
	   },
	   r'':{
	      "stream":"http://facebookyoursmallbusiness.podomatic.com/rss2.xml",
	      "image":"",
	      "name":"Facebook Your Small Business' Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/vZEXwaruRy29",
	      "image":"",
	      "name":"FanBrosShow"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=2942325",
	      "image":"",
	      "name":"Fantasy Focus Football"
	   },
	   r'':{
	      "stream":"http://podcasts.cstv.com/feeds/fantasyfootball.xml",
	      "image":"",
	      "name":"Fantasy Football Today Podcast"
	   },
	   r'':{
	      "stream":"http://kfan.iheart.com/podcast/itunes/FantasyFBWeekly_itunes.xml",
	      "image":"",
	      "name":"Fantasy Football Weekly"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:243341313/sounds.rss",
	      "image":"",
	      "name":"FantasyPros - Fantasy Football Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/FatManOnBatman",
	      "image":"",
	      "name":"Fat Man on Batman"
	   },
	   r'':{
	      "stream":"https://www.fbi.gov/feeds/fbi-this-week-podcast/itunes.xml",
	      "image":"",
	      "name":"FBI, This Week Podcast"
	   },
	   r'':{
	      "stream":"http://www.fdnypro.org/feed/podcast",
	      "image":"",
	      "name":"FDNY Pro"
	   },
	   r'':{
	      "stream":"http://fedsoc.server326.com/audio/MP3s/fsaudio.xml",
	      "image":"",
	      "name":"Federalist Society Event Audio"
	   },
	   r'':{
	      "stream":"http://fedsoc.server326.com/audio/SCOTUScast/SCOTUScast.xml",
	      "image":"",
	      "name":"Federalist Society SCOTUScast"
	   },
	   r'':{
	      "stream":"http://feeds.frogpants.com/filmsack_feed.xml",
	      "image":"",
	      "name":"Film Sack"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/cinecast",
	      "image":"",
	      "name":"Filmspotting"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/MadFientistPodcast",
	      "image":"",
	      "name":"Financial Independence Podcast - Early Retirement | Investing | Real Estate | Entrepreneurship"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/FireteamChatIgnsDestinyPodcast",
	      "image":"",
	      "name":"Fireteam Chat: IGN's Destiny Podcast"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=6247496",
	      "image":"",
	      "name":"First Take"
	   },
	   r'':{
	      "stream":"http://feedpress.me/first-things-podcast",
	      "image":"",
	      "name":"First Things Podcast"
	   },
	   r'':{
	      "stream":"http://angriesttrainer.libsyn.com/rss",
	      "image":"",
	      "name":"Fitness Confidential with Vinnie Tortorich"
	   },
	   r'':{
	      "stream":"http://www.flashforwardpod.com/feed/podcast/",
	      "image":"",
	      "name":"Flash Forward"
	   },
	   r'':{
	      "stream":"http://www.blogtalkradio.com/flylady/podcast",
	      "image":"",
	      "name":"FlyLady and Friends"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/FocusOnTheFamilyDailyBroadcast",
	      "image":"",
	      "name":"Focus on the Family Daily Broadcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/focus-on-the-family/focus-on-marriage",
	      "image":"",
	      "name":"Focus on the Family: Focus on Marriage"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/focus-on-the-family/focus-on-parenting",
	      "image":"",
	      "name":"Focus on the Family: Focus on Parenting"
	   },
	   r'':{
	      "stream":"http://foodpsych.libsyn.com/rss",
	      "image":"",
	      "name":"Food Psych - Intuitive Eating, Positive Body Image, & Eating Disorder Recovery"
	   },
	   r'':{
	      "stream":"https://www.theguardian.com/football/series/footballweekly/podcast.xml",
	      "image":"",
	      "name":"Football Weekly - The Guardian"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/forazeroth",
	      "image":"",
	      "name":"For Azeroth!: A World of Warcraft Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheParentExperiment",
	      "image":"",
	      "name":"For Crying Out Loud"
	   },
	   r'':{
	      "stream":"http://podcast.foundmyfitness.com/rss.xml",
	      "image":"",
	      "name":"FoundMyFitness"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:87356670/sounds.rss",
	      "image":"",
	      "name":"FR1 and EMS1 Podcasts"
	   },
	   r'':{
	      "stream":"http://www.shilohworshipmusic.com/ShilohWorshipMusic/Free_Bluegrass_Gospel_Hymns_Songs/rss.xml",
	      "image":"",
	      "name":"Free Bluegrass Gospel Hymns and Songs"
	   },
	   r'':{
	      "stream":"http://mafia.hahaascomedyringtones.libsynpro.com/rss",
	      "image":"",
	      "name":"FREE Ringtones, Funny Ringtones by Ringtone Mafia"
	   },
	   r'':{
	      "stream":"http://ffb.libsyn.com/rss",
	      "image":"",
	      "name":"French for Beginners"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/dailyfrenchpod/Gefs",
	      "image":"",
	      "name":"French for Beginners"
	   },
	   r'':{
	      "stream":"http://nsf.libsyn.com/rss",
	      "image":"",
	      "name":"French Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/FreshLifeChurch",
	      "image":"",
	      "name":"Fresh Life Church"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510026",
	      "image":"",
	      "name":"From the Top"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/FrontlineAudiocastPbs",
	      "image":"",
	      "name":"FRONTLINE: Audiocast | PBS"
	   },
	   r'':{
	      "stream":"http://www.thamike.com/fullofsith/fosxml.xml",
	      "image":"",
	      "name":"Full Of Sith: Star Wars News, Discussions and Interviews"
	   },
	   r'':{
	      "stream":"http://baldmove.com/feed/game-of-thrones-podcast/",
	      "image":"",
	      "name":"Game of Thrones The Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.ign.com/ignfeeds/podcasts/gamescoop/",
	      "image":"",
	      "name":"Game Scoop!"
	   },
	   r'':{
	      "stream":"http://choplogic.net/itunes/itunes_feed_gardenfork.xml",
	      "image":"",
	      "name":"GardenFork.TV DIY, Food, & Home Improvement Videos"
	   },
	   r'':{
	      "stream":"http://www.galexmusic.com/podcast/gareth.xml",
	      "image":"",
	      "name":"Gareth Emery: Electric For Life"
	   },
	   r'':{
	      "stream":"https://gastropod.com/feed/",
	      "image":"",
	      "name":"Gastropod"
	   },
	   r'':{
	      "stream":"http://gatewaypeople.com/ministries/life/podcast/audio/this",
	      "image":"",
	      "name":"Gateway Church Audio Podcast"
	   },
	   r'':{
	      "stream":"http://www.davidbarrkirtley.com/podcast/geeksguideshow.xml",
	      "image":"",
	      "name":"Geek's Guide to the Galaxy - Science Fiction Interviews, Movie Reviews, Sci-Fi Books and Writing"
	   },
	   r'':{
	      "stream":"http://geniusnetwork.libsyn.com/rss",
	      "image":"",
	      "name":"Genius Network - The World's Best Wisdom - Presented By Joe Polish"
	   },
	   r'':{
	      "stream":"http://www.quickanddirtytips.com/xml/getfitguy.xml",
	      "image":"",
	      "name":"Get-Fit Guy's Quick and Dirty Tips to Slim Down and Shape Up"
	   },
	   r'':{
	      "stream":"http://www.quickanddirtytips.com/xml/getitdone.xml",
	      "image":"",
	      "name":"Get-It-Done Guy's Quick and Dirty Tips to Work Less and Do More"
	   },
	   r'':{
	      "stream":"http://destinyghoststories.podbean.com/feed/",
	      "image":"",
	      "name":"Ghost Stories, a Destiny Podcast"
	   },
	   r'':{
	      "stream":"http://www.giantbomb.com/feeds/podcast/",
	      "image":"",
	      "name":"Giant Bombcast"
	   },
	   r'':{
	      "stream":"http://gohistorypodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Giants of History"
	   },
	   r'':{
	      "stream":"http://feeds.sideshownetwork.tv/GilbertGottfried",
	      "image":"",
	      "name":"Gilbert Gottfried's Amazing Colossal Podcast"
	   },
	   r'':{
	      "stream":"http://www.afterbuzztv.com/aftershows/gilmore-girls-afterbuzz-tv-aftershow/feed/",
	      "image":"",
	      "name":"Gilmore Girls: A Year In The Life After Show"
	   },
	   r'':{
	      "stream":"http://gilmored.libsyn.com/rss",
	      "image":"",
	      "name":"Gilmored: A New Gilmore Girls Podcast"
	   },
	   r'':{
	      "stream":"http://girlonguy.libsyn.com/rss",
	      "image":"",
	      "name":"Girl on Guy with Aisha Tyler"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/girlbossradio",
	      "image":"",
	      "name":"Girlboss Radio with Sophia Amoruso"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:200760230/sounds.rss",
	      "image":"",
	      "name":"Global Recon Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:123887054/sounds.rss",
	      "image":"",
	      "name":"Glorious in the Mundane Podcast with Christy Nockels"
	   },
	   r'':{
	      "stream":"http://wglt.org/podcasts/91/rss.xml",
	      "image":"",
	      "name":"GLT Jazz Next"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4829841.rss",
	      "image":"",
	      "name":"God Awful Movies"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/GodCenteredMomPodcast",
	      "image":"",
	      "name":"God Centered Mom Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:8760975/sounds.rss",
	      "image":"",
	      "name":"Godsfall: Divine & Conquer"
	   },
	   r'':{
	      "stream":"http://goinginraw.libsyn.com/rss",
	      "image":"",
	      "name":"GOING IN RAW PRO WRESTLING PODCAST"
	   },
	   r'':{
	      "stream":"http://goodjobbrain.libsyn.com/rss",
	      "image":"",
	      "name":"Good Job, Brain!"
	   },
	   r'':{
	      "stream":"http://www.goodlifeproject.com/feed/podcast/",
	      "image":"",
	      "name":"Good Life Project"
	   },
	   r'':{
	      "stream":"http://www.gao.gov/podcast/watchdog.xml",
	      "image":"",
	      "name":"Government Accountability Office (GAO) Podcast: Watchdog Report"
	   },
	   r'':{
	      "stream":"http://www.govinfosecurity.com/itunes_rss_podcasts.php",
	      "image":"",
	      "name":"Government Information Security Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:116855785/sounds.rss",
	      "image":"",
	      "name":"GovLove"
	   },
	   r'':{
	      "stream":"http://sfagravy.libsyn.com/rss",
	      "image":"",
	      "name":"Gravy"
	   },
	   r'':{
	      "stream":"http://victorprepvocab.libsyn.com/rss",
	      "image":"",
	      "name":"GRE Vocabulary Podcast by VictorPrep"
	   },
	   r'':{
	      "stream":"http://www.loyalbooks.com/book/fairy-tales-by-the-brothers-grimm/feed",
	      "image":"",
	      "name":"Grimms' Fairy Tales by Jacob & Wilhelm Grimm"
	   },
	   r'':{
	      "stream":"http://grumpyoldgeeks.libsyn.com/rss",
	      "image":"",
	      "name":"Grumpy Old Geeks - Covering tech news, security, movies, tv shows, and books for tech savvy adults"
	   },
	   r'':{
	      "stream":"http://guardianradio.podbean.com/feed",
	      "image":"",
	      "name":"Guardian Radio"
	   },
	   r'':{
	      "stream":"http://recordings.talkshoe.com/rss37557.xml",
	      "image":"",
	      "name":"Guitar Music Theory Lessons - Desi Serna"
	   },
	   r'':{
	      "stream":"http://guntalk.libsyn.com/rss",
	      "image":"",
	      "name":"Gun Talk"
	   },
	   r'':{
	      "stream":"http://www.gunfightercast.com/wordpress/feed/podcast/",
	      "image":"",
	      "name":"Gunfighter Cast"
	   },
	   r'':{
	      "stream":"http://www.halfsizeme.com/feed/podcast/",
	      "image":"",
	      "name":"Half Size Me"
	   },
	   r'':{
	      "stream":"http://rss.earwolf.com/handsome-rambler",
	      "image":"",
	      "name":"Hannibal Buress: Handsome Rambler"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/HappierWithGretchenRubin",
	      "image":"",
	      "name":"Happier with Gretchen Rubin"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/9to5cast/iUSC",
	      "image":"",
	      "name":"Happy Hour"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/HappySadConfused",
	      "image":"",
	      "name":"Happy Sad Confused"
	   },
	   r'':{
	      "stream":"http://podcast.djhardwell.com/podcast.xml",
	      "image":"",
	      "name":"Hardwell On Air Official Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/HarmontownPodcast",
	      "image":"",
	      "name":"Harmontown"
	   },
	   r'':{
	      "stream":"http://pdl.warnerbros.com/wbol/us/dd/podcasts/harry_potter/harry_potter_podcast.xml",
	      "image":"",
	      "name":"Harry Potter Podcast"
	   },
	   r'':{
	      "stream":"http://harvestbible.podbean.com/feed/",
	      "image":"",
	      "name":"Harvest Bible Chapel"
	   },
	   r'':{
	      "stream":"http://feeds.harvest.org/sunday-audio",
	      "image":"",
	      "name":"Harvest: Greg Laurie Audio"
	   },
	   r'':{
	      "stream":"http://hhmeds.hayhouse.libsynpro.com/rss",
	      "image":"",
	      "name":"Hay House Meditations"
	   },
	   r'':{
	      "stream":"http://hhradio.hayhouse.libsynpro.com/rss",
	      "image":"",
	      "name":"Hay House Radio Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.harvardbusiness.org/harvardbusiness/ideacast",
	      "image":"",
	      "name":"HBR IdeaCast"
	   },
	   r'':{
	      "stream":"http://healthybirthshappybabies.libsyn.com/rss",
	      "image":"",
	      "name":"Healthy Births, Happy Babies | Prenatal Care | Natural Birth | Pregnancy | Pediatrics"
	   },
	   r'':{
	      "stream":"http://heartwisdom.libsyn.com/rss",
	      "image":"",
	      "name":"Heart Wisdom with Jack Kornfield"
	   },
	   r'':{
	      "stream":"http://heldeepradio.spinninpodcasts.com/rss",
	      "image":"",
	      "name":"Heldeep Radio"
	   },
	   r'':{
	      "stream":"http://feeds.wqxr.org/wqxr-helga",
	      "image":"",
	      "name":"Helga"
	   },
	   r'':{
	      "stream":"http://feedpress.me/magictavern",
	      "image":"",
	      "name":"Hello from the Magic Tavern"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"Hello Internet,"
	   },
	   r'':{
	      "stream":"http://www.herewearepodcast.com/rss",
	      "image":"",
	      "name":"Here We Are"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/wnycheresthething",
	      "image":"",
	      "name":"Here's The Thing with Alec Baldwin"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:262464075/sounds.rss",
	      "image":"",
	      "name":"Hidden Tracks: Stories from BART"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/hillsdaledialogues",
	      "image":"",
	      "name":"Hillsdale Dialogues Podcast"
	   },
	   r'':{
	      "stream":"http://hiphopdaily.libsyn.com/rss",
	      "image":"",
	      "name":"HIPHOPDAILY | The Latest in Hip Hop & R&B"
	   },
	   r'':{
	      "stream":"https://feeds.publicradio.org/public_feeds/historically-black/itunes/rss",
	      "image":"",
	      "name":"Historically Black"
	   },
	   r'':{
	      "stream":"http://historyofjapan.libsyn.com/rss",
	      "image":"",
	      "name":"History of Japan"
	   },
	   r'':{
	      "stream":"http://hopwag.podbean.com/feed/",
	      "image":"",
	      "name":"History of Philosophy Without Any Gaps"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/xUnmFXZLuavF",
	      "image":"",
	      "name":"History on Fire"
	   },
	   r'':{
	      "stream":"http://historytoday.podomatic.com/rss2.xml",
	      "image":"",
	      "name":"History Today Podcast"
	   },
	   r'':{
	      "stream":"https://cdn-podcasts.video.aetnd.com/vikings-podcast.xml",
	      "image":"",
	      "name":"History Vikings Podcast"
	   },
	   r'':{
	      "stream":"http://hkspolicycast.libsyn.com/rss",
	      "image":"",
	      "name":"HKS PolicyCast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/HollywoodBabbleOnPod",
	      "image":"",
	      "name":"Hollywood Babble-On"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/homemadestories",
	      "image":"",
	      "name":"Homemade Stories"
	   },
	   r'':{
	      "stream":"http://hospitalmedicine.podbean.com/feed/",
	      "image":"",
	      "name":"Hospital and Internal Medicine Podcast"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=12474672",
	      "image":"",
	      "name":"Hot Takedown"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/HoundTall",
	      "image":"",
	      "name":"Hound Tall with Moshe Kasher"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/dXquYRvijwJ1?http://www.global-sets.com/Podcasts/feed.xml",
	      "image":"",
	      "name":"House Trance & Techno Livesets Podcasts"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"How to Be a Girl,"
	   },
	   r'':{
	      "stream":"http://feeds.howtobeamazingshow.com/htbashow",
	      "image":"",
	      "name":"How To Be Amazing with Michael Ian Black"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510303",
	      "image":"",
	      "name":"How To Do Everything"
	   },
	   r'':{
	      "stream":"https://awesound.com/@ycombinator/feed/how-to-start-a-startup",
	      "image":"",
	      "name":"How to Start a Startup"
	   },
	   r'':{
	      "stream":"http://hunttalk.libsyn.com/rss",
	      "image":"",
	      "name":"Hunt Talk Radio, Randy Newberg Unfiltered | Hunting | Conservation | Politics | Tactics"
	   },
	   r'':{
	      "stream":"http://rss.art19.com/i-just-want-to-talk-star-trek",
	      "image":"",
	      "name":"I Just Want To Talk Star Trek"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:188712331/sounds.rss",
	      "image":"",
	      "name":"I Tell My Husband The News"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/IWasThereToo",
	      "image":"",
	      "name":"I Was There Too"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:138976584/sounds.rss",
	      "image":"",
	      "name":"I'll Name This Podcast Later"
	   },
	   r'':{
	      "stream":"http://icetfinallevel.libsyn.com/rss",
	      "image":"",
	      "name":"Ice T: Final Level"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/LocalGovLife",
	      "image":"",
	      "name":"ICMA: Local Gov Life"
	   },
	   r'':{
	      "stream":"http://burndoc.libsyn.com/rss",
	      "image":"",
	      "name":"ICU Rounds"
	   },
	   r'':{
	      "stream":"http://www.idlethumbs.net/feeds/idle-thumbs",
	      "image":"",
	      "name":"Idle Thumbs"
	   },
	   r'':{
	      "stream":"http://ieltsenergy.libsyn.com/rss",
	      "image":"",
	      "name":"IELTS Energy English Podcast | IELTS English Speaking Practice 7+ | IELTS Test Strategy | IELTS English Writing Tips"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ifanboyPOW",
	      "image":"",
	      "name":"iFanboy.com Comic Book Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.ign.com/ignfeeds/podcasts/games/",
	      "image":"",
	      "name":"IGN Games Podcasts"
	   },
	   r'':{
	      "stream":"http://feeds.ign.com/ignfeeds/podcasts/video/gamescoop/",
	      "image":"",
	      "name":"IGN.com - Game Scoop! TV (Video)"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/imaginaryworldspodcast",
	      "image":"",
	      "name":"Imaginary Worlds"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/PhoneDifferentPodcast",
	      "image":"",
	      "name":"iMore show"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:224639879/sounds.rss",
	      "image":"",
	      "name":"Improper Etiquette"
	   },
	   r'':{
	      "stream":"http://www.bbc.co.uk/programmes/b006qykl/episodes/downloads.rss",
	      "image":"",
	      "name":"In Our Time"
	   },
	   r'':{
	      "stream":"http://www.bbc.co.uk/programmes/p01dh5yg/episodes/downloads.rss",
	      "image":"",
	      "name":"In Our Time: History"
	   },
	   r'':{
	      "stream":"https://www.intouch.org/listen/podcast/this-week-on-tv",
	      "image":"",
	      "name":"In Touch TV Broadcast featuring Dr. Charles Stanley - In Touch Ministries"
	   },
	   r'':{
	      "stream":"http://icollective.libsyn.com/rss",
	      "image":"",
	      "name":"Innovation & Leadership"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/inquiring-minds",
	      "image":"",
	      "name":"Inquiring Minds"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:259882856/sounds.rss",
	      "image":"",
	      "name":"Insecuritea: The Insecure Aftershow"
	   },
	   r'':{
	      "stream":"http://wvpublic.org/podcasts/41/rss.xml",
	      "image":"",
	      "name":"Inside Appalachia"
	   },
	   r'':{
	      "stream":"http://feeds.cfr.org/publication/audio",
	      "image":"",
	      "name":"Inside CFR Events (Audio)"
	   },
	   r'':{
	      "stream":"http://feeds.cfr.org/publication/video",
	      "image":"",
	      "name":"Inside CFR Events (Video)"
	   },
	   r'':{
	      "stream":"http://www.nyc.gov/html/nypd/audio/podcast_nycgov.xml",
	      "image":"",
	      "name":"Inside the NYPD"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:132077920/sounds.rss",
	      "image":"",
	      "name":"Inside The Team Room"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/insidevrar",
	      "image":"",
	      "name":"Inside VR & AR"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/InsightForLivingDailyBroadcast",
	      "image":"",
	      "name":"Insight for Living Daily Broadcast"
	   },
	   r'':{
	      "stream":"http://podcast.livinghour.org/feed/",
	      "image":"",
	      "name":"Inspirational Living: Motivation, Self-Help, Spirituality & Positive Thinking"
	   },
	   r'':{
	      "stream":"http://inspirenation.libsyn.com/rss",
	      "image":"",
	      "name":"Inspire Nation | Daily Inspiration - Motivation - Meditation | Law of Attraction | Health | Career | Spirituality | Self-Help"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/inspiredtoaction/GvcC",
	      "image":"",
	      "name":"InspiredToAction.com - Inspiration for Motherhood"
	   },
	   r'':{
	      "stream":"http://brookingsintersections.libsyn.com/rss",
	      "image":"",
	      "name":"Intersections"
	   },
	   r'':{
	      "stream":"http://investlikethebest.libsyn.com/rss",
	      "image":"",
	      "name":"Invest Like the Best"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:142420018/sounds.rss",
	      "image":"",
	      "name":"Invested: The Rule #1 Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/ipad_video_large.xml",
	      "image":"",
	      "name":"iOS Today (Video-HI)"
	   },
	   r'':{
	      "stream":"http://www.ringtonefeeder.com/videopodcast.xml",
	      "image":"",
	      "name":"iPhone Ringtone Videos"
	   },
	   r'':{
	      "stream":"http://bellobard.libsyn.com/rss",
	      "image":"",
	      "name":"Irish and Celtic Music Podcast"
	   },
	   r'':{
	      "stream":"http://realcoleworld.podomatic.com/rss2.xml",
	      "image":"",
	      "name":"It's a Cole World"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/pkmncast",
	      "image":"",
	      "name":"It's Super Effective"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/feeds/rss/podcast.xml?id=9545077",
	      "image":"",
	      "name":"Jalen & Jacoby"
	   },
	   r'':{
	      "stream":"http://jamaclinicalreviews.jamanetwork.libsynpro.com/rss",
	      "image":"",
	      "name":"JAMA Clinical Reviews: Interviews about ideas & innovations in medicine, science & clinical practice. Listen & earn CME credit."
	   },
	   r'':{
	      "stream":"http://jamaeditorsaudiosummary.jamanetwork.libsynpro.com/rss",
	      "image":"",
	      "name":"JAMA Editors' Summary: On research in medicine, science, & clinical practice. For physicians, researchers, & clinicians."
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/JamesBonding",
	      "image":"",
	      "name":"James Bonding"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/walkintheword/wxZf",
	      "image":"",
	      "name":"James MacDonald: Walk in the Word Audio"
	   },
	   r'':{
	      "stream":"https://feeds.feedwrench.com/JavaScriptJabber.rss",
	      "image":"",
	      "name":"JavaScript Jabber"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/JaySilentBobGetOld",
	      "image":"",
	      "name":"Jay & Silent Bob Get Old"
	   },
	   r'':{
	      "stream":"http://aclj.org/radio-shows/RSS",
	      "image":"",
	      "name":"Jay Sekulow Live Radio Show"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:109532020/sounds.rss",
	      "image":"",
	      "name":"Jenna & Julien Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/jentezenfranklin/hGbl",
	      "image":"",
	      "name":"Jentezen Franklin | RSS Feed"
	   },
	   r'':{
	      "stream":"http://jesuscalling.libsyn.com/jclibpodcast",
	      "image":"",
	      "name":"Jesus Calling Podcast"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=950",
	      "image":"",
	      "name":"Jim Beaver's Project Action"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4756470.rss",
	      "image":"",
	      "name":"Jim Cornette Experience"
	   },
	   r'':{
	      "stream":"http://jimharold.com/?feed=jimharoldscampfire",
	      "image":"",
	      "name":"Jim Harold's Campfire - True Ghost Stories | Jim Harold"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:258167968/sounds.rss",
	      "image":"",
	      "name":"Jim Norton & Sam Roberts"
	   },
	   r'':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1476?format=MP3_128K",
	      "image":"",
	      "name":"Jim Rome's Daily Jungle"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:125332894/sounds.rss",
	      "image":"",
	      "name":"Jimquisition"
	   },
	   r'':{
	      "stream":"http://itstreaming.apple.com/podcasts/musician/joe_budden/ww/j_budden.xml",
	      "image":"",
	      "name":"Joe Budden: Meet the Musician"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"Joel Osteen Podcast,"
	   },
	   r'':{
	      "stream":"http://johnmaxwell.podbean.com/feed/",
	      "image":"",
	      "name":"John Maxwell: A Minute With Maxwell"
	   },
	   r'':{
	      "stream":"http://feed.desiringgod.org/messages.rss",
	      "image":"",
	      "name":"John Piper Sermons"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/JosephPrinceAudioPodcast",
	      "image":"",
	      "name":"Joseph Prince Audio Podcast"
	   },
	   r'':{
	      "stream":"http://jmmtvsd.joycemeyer.libsynpro.com/rss",
	      "image":"",
	      "name":"Joyce Meyer Ministries TV Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/joycemeyer/SFiE",
	      "image":"",
	      "name":"Joyce Meyer Radio Podcast"
	   },
	   r'':{
	      "stream":"http://jmtvaudio.joycemeyer.libsynpro.com/rss",
	      "image":"",
	      "name":"Joyce Meyer TV Audio Podcast"
	   },
	   r'':{
	      "stream":"http://rosenbergradio.com/category/juan-epstein/feed/",
	      "image":"",
	      "name":"Juan Epstein"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/todayinthepast",
	      "image":"",
	      "name":"Judge John Hodgman"
	   },
	   r'':{
	      "stream":"http://rss.art19.com/juicy-scoop",
	      "image":"",
	      "name":"Juicy Scoop with Heather McDonald"
	   },
	   r'':{
	      "stream":"http://feeds.kcrw.com/kcrw/gf",
	      "image":"",
	      "name":"KCRW's Good Food"
	   },
	   r'':{
	      "stream":"http://feeds.kcrw.com/kcrw/mb",
	      "image":"",
	      "name":"KCRW's Morning Becomes Eclectic"
	   },
	   r'':{
	      "stream":"http://feeds.kcrw.com/kcrw/tt",
	      "image":"",
	      "name":"KCRW's The Treatment"
	   },
	   r'':{
	      "stream":"http://feeds.kcrw.com/kcrw/tu",
	      "image":"",
	      "name":"KCRW's Today's Top Tune"
	   },
	   r'':{
	      "stream":"http://ketotalk.libsyn.com/rss",
	      "image":"",
	      "name":"Keto Talk With Jimmy Moore & The Doc"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/KevinPollaksChatShow-Audio",
	      "image":"",
	      "name":"Kevin Pollak's Chat Show"
	   },
	   r'':{
	      "stream":"http://feeds.kexp.org/kexp/songoftheday",
	      "image":"",
	      "name":"KEXP Song of the Day"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/barstoolkfcradio",
	      "image":"",
	      "name":"KFC Radio"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/kidsmusicplanetpodcast",
	      "image":"",
	      "name":"Kids Music Planet Podcast"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=970",
	      "image":"",
	      "name":"Killing the Town with Storm and Cyrus"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/DBhVerLhyNUM",
	      "image":"",
	      "name":"Kinda Funny Gamescast"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4256036.rss",
	      "image":"",
	      "name":"King Falls AM"
	   },
	   r'':{
	      "stream":"http://kisstherose.libsyn.com/rss",
	      "image":"",
	      "name":"Kiss Me Quick's Erotica: Sexy Stories with Rose Caraway"
	   },
	   r'':{
	      "stream":"http://knifepointhorror.libsyn.com/rss",
	      "image":"",
	      "name":"Knifepoint Horror"
	   },
	   r'':{
	      "stream":"http://shoutengine.com/KnightsofRen.xml",
	      "image":"",
	      "name":"Knights of Ren"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/kh_video_hd.xml",
	      "image":"",
	      "name":"Know How... (Video-HD)"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/qjDxovCnSaSq",
	      "image":"",
	      "name":"Komando On Demand"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/KotakuSplitscreen",
	      "image":"",
	      "name":"Kotaku Splitscreen"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/kvministries",
	      "image":"",
	      "name":"Kris Vallotton's Podcast"
	   },
	   r'':{
	      "stream":"http://kuow.org/podcasts",
	      "image":"",
	      "name":"KUOW Seattle News and Information"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/ladieswholunch",
	      "image":"",
	      "name":"Ladies Who Lunch"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=836",
	      "image":"",
	      "name":"LadyGang"
	   },
	   r'':{
	      "stream":"http://rss.dw.com/xml/DKpodcast_lgn_de",
	      "image":"",
	      "name":"Langsam gesprochene Nachrichten | Deutsch lernen | Deutsche Welle"
	   },
	   r'':{
	      "stream":"http://nsslatino.libsyn.com/rss",
	      "image":"",
	      "name":"Latin American Spanish"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510016&uid=p1qe4e85742c986fdb81d2d38ffa0d5d53",
	      "image":"",
	      "name":"Latino USA"
	   },
	   r'':{
	      "stream":"http://radiofrance-podcast.net/podcast09/rss_14277.xml",
	      "image":"",
	      "name":"Le son de la night"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/leadsingersyndrome",
	      "image":"",
	      "name":"Lead Singer Syndrome"
	   },
	   r'':{
	      "stream":"http://www.melnyks.com/?feed=podcast",
	      "image":"",
	      "name":"Learn Chinese - Mandarin Chinese Lessons"
	   },
	   r'':{
	      "stream":"http://www.chineseclass101.com/wp-feed-audio-video.php",
	      "image":"",
	      "name":"Learn Chinese | ChineseClass101.com"
	   },
	   r'':{
	      "stream":"http://www.englishclass101.com/wp-feed-audio-video.php",
	      "image":"",
	      "name":"Learn English | EnglishClass101.com"
	   },
	   r'':{
	      "stream":"http://www.frenchpod101.com/wp-feed-audio-video.php",
	      "image":"",
	      "name":"Learn French | FrenchPod101.com"
	   },
	   r'':{
	      "stream":"http://ftew.libsyn.com/rss",
	      "image":"",
	      "name":"Learn French by Podcast"
	   },
	   r'':{
	      "stream":"http://www.dailyfrenchpod.com/wordpress/new-rss.xml",
	      "image":"",
	      "name":"Learn French with daily podcasts"
	   },
	   r'':{
	      "stream":"http://www.germanpod101.com/wp-feed-audio-video.php",
	      "image":"",
	      "name":"Learn German | GermanPod101.com"
	   },
	   r'':{
	      "stream":"http://lgbp.podbean.com/feed/",
	      "image":"",
	      "name":"Learn German by Podcast"
	   },
	   r'':{
	      "stream":"http://www.hindipod101.com/wp/wp-feed-audio-video.php",
	      "image":"",
	      "name":"Learn Hindi | HindiPod101.com"
	   },
	   r'':{
	      "stream":"http://www.italianpod101.com/wp/wp-feed-audio-video.php",
	      "image":"",
	      "name":"Learn Italian | ItalianPod101.com"
	   },
	   r'':{
	      "stream":"http://www.learnitalianpod.com/feed/",
	      "image":"",
	      "name":"Learn Italian with Podcasts at LearnItalianPod.com"
	   },
	   r'':{
	      "stream":"http://www.japanesepod101.com/wp/wp-feed-audio.php",
	      "image":"",
	      "name":"Learn Japanese | JapanesePod101.com (Audio)"
	   },
	   r'':{
	      "stream":"http://www.koreanclass101.com/wp/wp-feed-audio-video.php",
	      "image":"",
	      "name":"Learn Korean | KoreanClass101.com"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/BrazilianPodClass",
	      "image":"",
	      "name":"Learn Portuguese - BrazilianPodClass"
	   },
	   r'':{
	      "stream":"http://www.russianpod101.com/wp-feed-audio-video.php",
	      "image":"",
	      "name":"Learn Russian | RussianPod101.com"
	   },
	   r'':{
	      "stream":"http://survivalspanish.libsyn.com/rss",
	      "image":"",
	      "name":"Learn Spanish - Survival Guide"
	   },
	   r'':{
	      "stream":"http://www.spanishpod101.com/wp-feed-audio-video.php",
	      "image":"",
	      "name":"Learn Spanish | SpanishPod101.com"
	   },
	   r'':{
	      "stream":"http://learnrealspanish.libsyn.com/rss",
	      "image":"",
	      "name":"Learn Spanish: Notes in Spanish Inspired Beginners"
	   },
	   r'':{
	      "stream":"http://learntocodewithme.libsyn.com/rss",
	      "image":"",
	      "name":"Learn to Code With Me"
	   },
	   r'':{
	      "stream":"http://learntruehealth.libsyn.com/rss",
	      "image":"",
	      "name":"Learn True Health with Ashley James"
	   },
	   r'':{
	      "stream":"http://learningenglish.voanews.com/podcast/?count=20&zoneId=1689",
	      "image":"",
	      "name":"Learning English Broadcast - Voice of America"
	   },
	   r'':{
	      "stream":"http://learningmachines101.libsyn.com/rss",
	      "image":"",
	      "name":"Learning Machines 101"
	   },
	   r'':{
	      "stream":"http://www.afterbuzztv.com/aftershows/legends-of-tomorrow-afterbuzz-tv-aftershow/feed/",
	      "image":"",
	      "name":"Legends Of Tomorrow AfterBuzz TV AfterShow"
	   },
	   r'':{
	      "stream":"http://www.oneplace.com/ministries/let-my-people-think/subscribe/podcast.xml",
	      "image":"",
	      "name":"Let My People Think on OnePlace.com"
	   },
	   r'':{
	      "stream":"http://letsspeakitalian.libsyn.com/rss",
	      "image":"",
	      "name":"Let's Speak Italian!"
	   },
	   r'':{
	      "stream":"https://librivox.org/podcast.xml",
	      "image":"",
	      "name":"LibriVox Audiobooks"
	   },
	   r'':{
	      "stream":"http://feedpress.me/lifechurchaudio",
	      "image":"",
	      "name":"Life.Church: Craig Groeschel Audio"
	   },
	   r'':{
	      "stream":"http://revision3.com/lifehacker/itunes/mp4-hd30",
	      "image":"",
	      "name":"Lifehacker"
	   },
	   r'':{
	      "stream":"http://www.afterbuzztv.com/aftershows/making-their-way-to-the-ring-afterbuzz-tv/feed/",
	      "image":"",
	      "name":"Lilian Garcia: Making Their Way To The Ring"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:125221818/sounds.rss",
	      "image":"",
	      "name":"Limetown"
	   },
	   r'':{
	      "stream":"http://limitedresources.libsyn.com/rss",
	      "image":"",
	      "name":"Limited Resources"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/udacity-linear-digressions?format=xml",
	      "image":"",
	      "name":"Linear Digressions"
	   },
	   r'':{
	      "stream":"http://www.listenmoneymatters.com/feed/podcast/",
	      "image":"",
	      "name":"Listen Money Matters! A Personal Finance Show on How to Invest Simply, Crush Debt, Budget Like a Pro, Build Better Money Habits"
	   },
	   r'':{
	      "stream":"http://www.lisztonian.com/titles/feed.php",
	      "image":"",
	      "name":"Lisztonian: Classical Piano Music"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/littlegoldmenpodcast",
	      "image":"",
	      "name":"Little Gold Men"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510253",
	      "image":"",
	      "name":"Live In Concert from NPR's All Songs Considered"
	   },
	   r'':{
	      "stream":"http://www.livewireradio.org/podcast_feed",
	      "image":"",
	      "name":"Live Wire Radio"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/lote-daily",
	      "image":"",
	      "name":"Living on the Edge with Chip Ingram Daily Podcast"
	   },
	   r'':{
	      "stream":"http://www.lse.ac.uk/assets/richmedia/webFeeds/publicLecturesAndEvents_iTunesStore.xml",
	      "image":"",
	      "name":"London School of Economics: Public lectures and events"
	   },
	   r'':{
	      "stream":"http://www.blubrry.com/feeds/louisvillelectures.xml",
	      "image":"",
	      "name":"Louisville Lectures Internal Medicine Lecture Series Podcast"
	   },
	   r'':{
	      "stream":"https://www.loveandlogic.com/feeds/loveandlogic.rss",
	      "image":"",
	      "name":"Love and Logic - Solutions for parents and teachers"
	   },
	   r'':{
	      "stream":"http://lovelife.libsyn.com/rss",
	      "image":"",
	      "name":"Love Life with Matthew Hussey"
	   },
	   r'':{
	      "stream":"http://www.cbc.ca/podcasting/includes/loveme.xml",
	      "image":"",
	      "name":"Love Me"
	   },
	   r'':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1485?format=MP3_128K",
	      "image":"",
	      "name":"Loveline with Amber Rose"
	   },
	   r'':{
	      "stream":"http://macosken.libsyn.com/rss",
	      "image":"",
	      "name":"Mac OS Ken"
	   },
	   r'':{
	      "stream":"https://www.relay.fm/mpu/feed",
	      "image":"",
	      "name":"Mac Power Users"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/mbw.xml",
	      "image":"",
	      "name":"MacBreak Weekly (MP3)"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/mbw_video_hd.xml",
	      "image":"",
	      "name":"MacBreak Weekly (Video-HD)"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:58576458/sounds.rss",
	      "image":"",
	      "name":"Macworld"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/madmovies",
	      "image":"",
	      "name":"Mad About Movies"
	   },
	   r'':{
	      "stream":"http://podcast.cnbc.com/mmpodcast/lightninground.xml",
	      "image":"",
	      "name":"MAD MONEY W/ JIM CRAMER - Full Episode"
	   },
	   r'':{
	      "stream":"http://magiclessons.libsyn.com/rss",
	      "image":"",
	      "name":"Magic Lessons with Elizabeth Gilbert"
	   },
	   r'':{
	      "stream":"http://mariabartholdi.com/podcastgen/feed.xml",
	      "image":"",
	      "name":"Magic the Amateuring"
	   },
	   r'':{
	      "stream":"http://www.wizards.com/drivetoworkpodcast.xml",
	      "image":"",
	      "name":"Magic: The Gathering Drive to Work Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/mnitunes",
	      "image":"",
	      "name":"Major Nelson Radio"
	   },
	   r'':{
	      "stream":"https://feeds.publicradio.org/public_feeds/make-me-smart-with-kai-and-molly/itunes/rss",
	      "image":"",
	      "name":"Make Me Smart with Kai and Molly"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/MakeMeSmarterFootballPodcast",
	      "image":"",
	      "name":"Make Me Smarter Football Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/jjhM1Pd5OUeO",
	      "image":"",
	      "name":"Making It With Jimmy Diresta, Bob Clagett and David Picciuto"
	   },
	   r'':{
	      "stream":"http://podcasts.apple.com/eaas/us/special_event/gladwell/gladwell.xml",
	      "image":"",
	      "name":"Malcolm Gladwell, Revisionist History: Special Event"
	   },
	   r'':{
	      "stream":"https://files.manager-tools.com/files/public/feeds/manager-tools-podcasts.xml",
	      "image":"",
	      "name":"Manager Tools"
	   },
	   r'':{
	      "stream":"http://manilaclubbing.podomatic.com/rss2.xml",
	      "image":"",
	      "name":"Manila Club Radio - DJ Mixes"
	   },
	   r'':{
	      "stream":"http://marathontrainingacademy.com/feed/podcast",
	      "image":"",
	      "name":"Marathon Training Academy"
	   },
	   r'':{
	      "stream":"http://thestashed.com/podcasts/2015/vol1/stashed-media-network_marisa-explains-it-all.xml",
	      "image":"",
	      "name":"Marisa Explains It All With Tunisia And Jamal"
	   },
	   r'':{
	      "stream":"http://shoutengine.com/MarkBellsPowerCast.xml",
	      "image":"",
	      "name":"Mark Bell's PowerCast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/Marketfoolery",
	      "image":"",
	      "name":"MarketFoolery"
	   },
	   r'':{
	      "stream":"http://mschool.growtheverywhere.libsynpro.com/rss",
	      "image":"",
	      "name":"Marketing School | Digital Marketing | Online Marketing"
	   },
	   r'':{
	      "stream":"http://feeds.americanpublicmedia.org/MarketplacePodcast",
	      "image":"",
	      "name":"Marketplace"
	   },
	   r'':{
	      "stream":"https://feeds.publicradio.org/public_feeds/apm-marketplace-tech/itunes/rss",
	      "image":"",
	      "name":"Marketplace Tech"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/MarkusSchulzGlobalDJBroadcast",
	      "image":"",
	      "name":"Markus Schulz Presents Global DJ Broadcast"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"Marriage Is Funny,"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:113872557/sounds.rss",
	      "image":"",
	      "name":"Marriage More Podcast - Making Your Marriage More - Relationships | Couples | Intimacy | Christian |"
	   },
	   r'':{
	      "stream":"http://martinisandyourmoney.libsyn.com/rss",
	      "image":"",
	      "name":"Martinis and Your Money Podcast"
	   },
	   r'':{
	      "stream":"http://masterofmemory.com/feed/podcast/",
	      "image":"",
	      "name":"Master of Memory: Accelerated learning, education, memorization"
	   },
	   r'':{
	      "stream":"https://simplecast.com/podcasts/1528/rss",
	      "image":"",
	      "name":"MASTERPIECE Studio"
	   },
	   r'':{
	      "stream":"http://www.bloomberg.com/feeds/podcasts/masters_in_business.xml",
	      "image":"",
	      "name":"Masters in Business"
	   },
	   r'':{
	      "stream":"https://rss.art19.com/matt-and-dorees-eggcellent-adventure",
	      "image":"",
	      "name":"Matt and Doree's Eggcellent Adventure"
	   },
	   r'':{
	      "stream":"http://maxlucado.com/feed/custom",
	      "image":"",
	      "name":"Max LucadoMax Lucado"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:68947374/sounds.rss",
	      "image":"",
	      "name":"Me & Paranormal You"
	   },
	   r'':{
	      "stream":"http://www.themeateater.com/podcasts/feed/podcast/",
	      "image":"",
	      "name":"MeatEater Podcast"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4581642.rss",
	      "image":"",
	      "name":"Meditation Minis Podcast"
	   },
	   r'':{
	      "stream":"http://meditationoasis.libsyn.com/rss",
	      "image":"",
	      "name":"Meditation Oasis"
	   },
	   r'':{
	      "stream":"https://www.nrsng.com/feed/motd/",
	      "image":"",
	      "name":"MedMaster Show (Nursing Podcast: Pharmacology and Medications for Nurses and Nursing Students by NRSNG)"
	   },
	   r'':{
	      "stream":"http://feeds.wnyc.org/wqxr-meetthecomposer",
	      "image":"",
	      "name":"Meet the Composer"
	   },
	   r'':{
	      "stream":"http://podcasts.apple.com/eaas/mtf.xml",
	      "image":"",
	      "name":"Meet the Filmmaker"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/MenInBlazers",
	      "image":"",
	      "name":"Men In Blazers"
	   },
	   r'':{
	      "stream":"http://mentalpod.libsyn.com/rss",
	      "image":"",
	      "name":"Mental Illness Happy Hour"
	   },
	   r'':{
	      "stream":"http://www.screencast.com/users/nerfherder/folders/Mental%20Math%20Secrets%20-%20Your%20Secret%20Weapon%20for%20Success/itunes",
	      "image":"",
	      "name":"Mental Math Secrets - Your Secret Weapon for Success"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:193038850/sounds.rss",
	      "image":"",
	      "name":"Mentors for Military Podcast"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"Merriam-Webster's Word of the Day,"
	   },
	   r'':{
	      "stream":"http://mettahour.libsyn.com/rss",
	      "image":"",
	      "name":"Metta Hour with Sharon Salzberg"
	   },
	   r'':{
	      "stream":"http://mghpsychiatry.mgh.libsynpro.com/rss",
	      "image":"",
	      "name":"MGH Psychiatry Academy Podcasts"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=2445552",
	      "image":"",
	      "name":"Mike & Mike"
	   },
	   r'':{
	      "stream":"http://www.dvidshub.net/rss/podcast/34",
	      "image":"",
	      "name":"Military HD"
	   },
	   r'':{
	      "stream":"http://artizen.audello.com/podcast/1/",
	      "image":"",
	      "name":"Mind Pump: Raw Fitness Truth"
	   },
	   r'':{
	      "stream":"http://mindfullivingspiritualawakening.libsyn.com/rss",
	      "image":"",
	      "name":"Mindful Living Spiritual Awakening"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/minecraftvideo",
	      "image":"",
	      "name":"Minecraft Me - SD Video"
	   },
	   r'':{
	      "stream":"http://minutephysics.libsyn.com/rss",
	      "image":"",
	      "name":"MinutePhysics"
	   },
	   r'':{
	      "stream":"http://devonhyland.ca/mm/rss_feed.xml",
	      "image":"",
	      "name":"Mischief Managed Podcast - Your Recommended Dose of Harry Potter Nonsense"
	   },
	   r'':{
	      "stream":"http://www.cbc.ca/podcasting/includes/missing.xml",
	      "image":"",
	      "name":"Missing & Murdered: Who Killed Alberta Williams?"
	   },
	   r'':{
	      "stream":"https://mixergy.com/?feed=mixergy_feed&rss_source=itunes&",
	      "image":"",
	      "name":"Mixergy - Startup Stories with 1000+ entrepreneurs including founders of Wikipedia, Y Combinator, Pixar and more."
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:95405521/sounds.rss",
	      "image":"",
	      "name":"Money For the Rest of Us"
	   },
	   r'':{
	      "stream":"http://www.quickanddirtytips.com/money.xml",
	      "image":"",
	      "name":"Money Girl's Quick and Dirty Tips for a Richer Life"
	   },
	   r'':{
	      "stream":"https://www.monstercat.com/podcast/feed.xml",
	      "image":"",
	      "name":"Monstercat Podcast"
	   },
	   r'':{
	      "stream":"http://skeptic.libsyn.com/rss",
	      "image":"",
	      "name":"MonsterTalk"
	   },
	   r'':{
	      "stream":"http://feed.theplatform.com/f/IfSiAC/mqWRck66SwGc",
	      "image":"",
	      "name":"MOSAIC - Erwin Raphael McManus  (Audio)"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/mothermayisleepwithpodcast",
	      "image":"",
	      "name":"Mother, May I Sleep With Podcast?"
	   },
	   r'':{
	      "stream":"http://feeds2.feedburner.com/MotleyFoolMoney",
	      "image":"",
	      "name":"Motley Fool Money"
	   },
	   r'':{
	      "stream":"http://movethesticks.libsyn.com/rss",
	      "image":"",
	      "name":"Move the Sticks with Daniel Jeremiah & Bucky Brooks"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"MPIR Old Time Radio,"
	   },
	   r'':{
	      "stream":"https://www.mtggoldfish.com/podcasts/feed.rss",
	      "image":"",
	      "name":"MTGGoldfish Podcast"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4855957.rss",
	      "image":"",
	      "name":"MuggleCast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:87377017/sounds.rss",
	      "image":"",
	      "name":"Muscle for Life"
	   },
	   r'':{
	      "stream":"http://mwfmotivation.libsyn.com/rss",
	      "image":"",
	      "name":"MWF Motivation Podcast"
	   },
	   r'':{
	      "stream":"http://mbmbam.libsyn.com/rss",
	      "image":"",
	      "name":"My Brother, My Brother And Me"
	   },
	   r'':{
	      "stream":"http://mysevenchakras7.libsyn.com/rss",
	      "image":"",
	      "name":"My Seven Chakras with Aditya"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"Myleik Teele's Podcast,"
	   },
	   r'':{
	      "stream":"http://recordings.talkshoe.com/rss21864.xml",
	      "image":"",
	      "name":"Mysteries Abound"
	   },
	   r'':{
	      "stream":"http://mysteriousuniverse.org/feed/podcast/",
	      "image":"",
	      "name":"Mysterious Universe"
	   },
	   r'':{
	      "stream":"http://feeds.gimletmedia.com/mysteryshow",
	      "image":"",
	      "name":"Mystery Show"
	   },
	   r'':{
	      "stream":"http://mysterytheatre.rnn.beta.libsynpro.com/rss",
	      "image":"",
	      "name":"Mystery Theatre"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/naked_astronomy_podcast",
	      "image":"",
	      "name":"Naked Astronomy, from the Naked Scientists"
	   },
	   r'':{
	      "stream":"http://www.nasa.gov/rss/dyn/NASAcast_vodcast.rss",
	      "image":"",
	      "name":"NASACast Video"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/npspodcasts",
	      "image":"",
	      "name":"National Park Service"
	   },
	   r'':{
	      "stream":"http://feeds.pbs.org/pbs/wnet/nature-video",
	      "image":"",
	      "name":"NATURE | PBS"
	   },
	   r'':{
	      "stream":"http://wrvo.org/podcasts/15101/rss.xml",
	      "image":"",
	      "name":"Nature of Things"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/nature",
	      "image":"",
	      "name":"Nature Podcast"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=3634017",
	      "image":"",
	      "name":"NBA Lockdown"
	   },
	   r'':{
	      "stream":"http://www.washingtoninstitute.org/podcast/",
	      "image":"",
	      "name":"Near East Policycast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/nejm-this-week-audio-summaries",
	      "image":"",
	      "name":"NEJM This Week - Audio Summaries"
	   },
	   r'':{
	      "stream":"http://podcast.nejm.org/nejm_audio_interview.xml",
	      "image":"",
	      "name":"New England Journal of Medicine Interviews"
	   },
	   r'':{
	      "stream":"http://www.newmusicmonday.com/podcast/newmusicmonday.xml",
	      "image":"",
	      "name":"New Music Monday - Free music podcast by two seconds away"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/NewYorkMagazinesSexLives",
	      "image":"",
	      "name":"New York Magazine's Sex Lives"
	   },
	   r'':{
	      "stream":"http://www.newyorker.com/feed/podcast/out-loud",
	      "image":"",
	      "name":"New Yorker: Out Loud"
	   },
	   r'':{
	      "stream":"http://www.newyorker.com/feed/podcast/movie-of-the-week",
	      "image":"",
	      "name":"New Yorker: The Front Row"
	   },
	   r'':{
	      "stream":"http://nflfantasy.libsyn.com/rss",
	      "image":"",
	      "name":"NFL Fantasy Live"
	   },
	   r'':{
	      "stream":"http://dameshek.libsyn.com/rss",
	      "image":"",
	      "name":"NFL: The Dave Dameshek Football Program"
	   },
	   r'':{
	      "stream":"http://thechainsmokers.libsyn.com/rss",
	      "image":"",
	      "name":"Nice Hair with The Chainsmokers"
	   },
	   r'':{
	      "stream":"http://www.nick.com/sbcom/data/scenic/itunes_podcast.jhtml?podcast=nickjr",
	      "image":"",
	      "name":"Nick Jr."
	   },
	   r'':{
	      "stream":"http://asmassets.mtvnservices.com/alias/podcasts/nickelodeon/nickelodeon_animation_podcast/Nickelodeon_iTunesPodcast_Podcasts.xml",
	      "image":"",
	      "name":"Nickelodeon Animation Podcast"
	   },
	   r'':{
	      "stream":"http://nightowl.podtree.com/feed/podcast/",
	      "image":"",
	      "name":"Night Owl Radio"
	   },
	   r'':{
	      "stream":"http://feeds.ign.com/ignfeeds/podcasts/wii/",
	      "image":"",
	      "name":"Nintendo Voice Chat"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:162332893/sounds.rss",
	      "image":"",
	      "name":"No Guitar Is Safe"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:154009125/sounds.rss",
	      "image":"",
	      "name":"No Jumper"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/NLUpodcasts",
	      "image":"",
	      "name":"No Laying Up - Golf Podcast"
	   },
	   r'':{
	      "stream":"http://nomeatathleteradio.libsyn.com/rss",
	      "image":"",
	      "name":"No Meat Athlete Radio"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/2399216.rss",
	      "image":"",
	      "name":"No Such Thing As A Fish"
	   },
	   r'':{
	      "stream":"http://www.joangarry.com/feed/podcast",
	      "image":"",
	      "name":"Nonprofits Are Messy: Lessons in Leadership | Fundraising | Board Development | Communications"
	   },
	   r'':{
	      "stream":"http://norm.videopodcastnetwork.libsynpro.com/rss",
	      "image":"",
	      "name":"Norm Macdonald Live"
	   },
	   r'':{
	      "stream":"http://norml.org/rss/normlevents_podcast.xml",
	      "image":"",
	      "name":"NORML Events - PodCast"
	   },
	   r'':{
	      "stream":"http://norml.org/rss/normlnews_podcast.xml",
	      "image":"",
	      "name":"NORML Weekly News Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/NorthMollywood",
	      "image":"",
	      "name":"North Mollywood"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/WeeklyPodcastNorthPoint",
	      "image":"",
	      "name":"North Point Community Church"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:174789515/sounds.rss",
	      "image":"",
	      "name":"Not So Standard Deviations"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/NotTooDeepWithGraceHelbig",
	      "image":"",
	      "name":"Not Too Deep with Grace Helbig"
	   },
	   r'':{
	      "stream":"http://notesinspanish.libsyn.com/rss",
	      "image":"",
	      "name":"Notes in Spanish Advanced"
	   },
	   r'':{
	      "stream":"http://intnotesinspanish.libsyn.com/rss",
	      "image":"",
	      "name":"Notes in Spanish Intermediate"
	   },
	   r'':{
	      "stream":"http://www.muslimcentral.com/audio/nouman-ali-khan/feed/",
	      "image":"",
	      "name":"Nouman Ali Khan"
	   },
	   r'':{
	      "stream":"http://www.pbs.org/wgbh/nova/rss/nova-podcast.xml",
	      "image":"",
	      "name":"NOVA | PBS"
	   },
	   r'':{
	      "stream":"http://feeds.pbs.org/pbs/wgbh/nova/nsn-audio",
	      "image":"",
	      "name":"NOVA scienceNOW"
	   },
	   r'':{
	      "stream":"http://podcast.nowplayingpodcast.com/feed/",
	      "image":"",
	      "name":"Now Playing - The Movie Review Podcast"
	   },
	   r'':{
	      "stream":"http://feedpress.me/mountainstagepodcast",
	      "image":"",
	      "name":"NPR's Mountain Stage"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"NutritionFacts.org,"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/OffCameraWithSamJones",
	      "image":"",
	      "name":"Off Camera with Sam Jones"
	   },
	   r'':{
	      "stream":"http://achievementhunter.roosterteeth.com/show/off-topic-the-achievement-hunter-podcast/feed/mp3",
	      "image":"",
	      "name":"Off Topic"
	   },
	   r'':{
	      "stream":"http://playstation.libsyn.com/rss",
	      "image":"",
	      "name":"Official PlayStation Blogcast"
	   },
	   r'':{
	      "stream":"http://feeds.civilbeat.org/civilbeatoffshore",
	      "image":"",
	      "name":"OFFSHORE"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/OhNoPodcast",
	      "image":"",
	      "name":"Oh No Ross and Carrie"
	   },
	   r'':{
	      "stream":"http://www.mysteryshows.com/Podcasts/Mystery-Shows-Feed.xml",
	      "image":"",
	      "name":"Old Time Radio Mystery Theater"
	   },
	   r'':{
	      "stream":"http://feed.cnet.com/feed/podcast/cnet-on-cars/hd.xml",
	      "image":"",
	      "name":"On Cars (HD)"
	   },
	   r'':{
	      "stream":"http://feeds.wnyc.org/onthemedia",
	      "image":"",
	      "name":"On the Media"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/OnViolentExtremism",
	      "image":"",
	      "name":"On Violent Extremism"
	   },
	   r'':{
	      "stream":"http://onechurchla.org/feed/podcast/",
	      "image":"",
	      "name":"One Church LA"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"ONE Extraordinary Marriage Show | Sex. Love. Commitment.,"
	   },
	   r'':{
	      "stream":"http://oneshotpodcast.com/category/one-shot/one-shot-podcast/feed/",
	      "image":"",
	      "name":"One Shot"
	   },
	   r'':{
	      "stream":"http://www.amyporterfield.com/feed/podcast/?wpmfeedkey=42",
	      "image":"",
	      "name":"Online Marketing Made Easy with Amy Porterfield"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510052",
	      "image":"",
	      "name":"Only A Game"
	   },
	   r'':{
	      "stream":"http://feeds.wnyc.org/only-human",
	      "image":"",
	      "name":"Only Human"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4828446.rss",
	      "image":"",
	      "name":"Only Stupid Answers"
	   },
	   r'':{
	      "stream":"http://www.blogtalkradio.com/ufo_radio/podcast",
	      "image":"",
	      "name":"Open Minds UFO Radio"
	   },
	   r'':{
	      "stream":"http://radioopensource.org/feed/",
	      "image":"",
	      "name":"Open Source with Christopher Lydon"
	   },
	   r'':{
	      "stream":"http://www.operationselfreset.com/feed/podcast/",
	      "image":"",
	      "name":"Operation Self Reset | Self Help 101 | Confidence | Self Esteem | Motivation | Inspiration | Goal Setting| Success Factors|"
	   },
	   r'':{
	      "stream":"http://optimalfinancedaily.libsyn.com/rss",
	      "image":"",
	      "name":"Optimal Finance Daily: The Best Of Personal Finance | Minimalism | Investing"
	   },
	   r'':{
	      "stream":"http://optimallivingdaily.libsyn.com/rss",
	      "image":"",
	      "name":"Optimal Living Daily: Personal Development | Productivity | Minimalism | Growth"
	   },
	   r'':{
	      "stream":"http://feeds.prx.org/orbitalpath",
	      "image":"",
	      "name":"Orbital Path"
	   },
	   r'':{
	      "stream":"http://orderofman.libsyn.com/rss",
	      "image":"",
	      "name":"Order of Man: Finance | Fitness | Leadership | Manly Skills | Relationships | Self-Mastery | Style"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/outwestpodcast",
	      "image":"",
	      "name":"Out West: Westworld Fan Theories, Dissected"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/Outkick",
	      "image":"",
	      "name":"Outkick The Show with Clay Travis"
	   },
	   r'':{
	      "stream":"http://podcast.outsideonline.com/OutsidePodcast",
	      "image":"",
	      "name":"Outside Podcast"
	   },
	   r'':{
	      "stream":"http://overitandonwithit.libsyn.com/rss",
	      "image":"",
	      "name":"Over It And On With It"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/overwatchers",
	      "image":"",
	      "name":"Overwatchers: The Overwatch Podcast"
	   },
	   r'':{
	      "stream":"http://paleomg.com/feed/podcast/",
	      "image":"",
	      "name":"PaleOMG Uncensored"
	   },
	   r'':{
	      "stream":"http://jimharold.com/?feed=podcast",
	      "image":"",
	      "name":"PARANORMAL PODCAST | Jim Harold"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/parentcast",
	      "image":"",
	      "name":"ParentCast: New Parents | New Babies | New Adventures | A New Kind Of Crazy"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:209924999/sounds.rss",
	      "image":"",
	      "name":"Parenting Beyond Discipline"
	   },
	   r'':{
	      "stream":"http://megmeeker.megmeekerpodcast.libsynpro.com/rss",
	      "image":"",
	      "name":"Parenting Great Kids with Dr. Meg Meeker"
	   },
	   r'':{
	      "stream":"http://parentingonpurpose.org/podcast.ashx",
	      "image":"",
	      "name":"Parenting On Purpose (Parenting On Purpose)"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/PartiallyDerivative",
	      "image":"",
	      "name":"Partially Derivative"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/PassionCityChurchPodcast",
	      "image":"",
	      "name":"Passion City Church Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/DailyHopeWithRickWarrenPodcast",
	      "image":"",
	      "name":"Pastor Rick's Daily Hope"
	   },
	   r'':{
	      "stream":"http://www.pcgamer.com/spark_podcast/2/",
	      "image":"",
	      "name":"PC Gamer"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/peainthepodcast",
	      "image":"",
	      "name":"Pea In The Podcast"
	   },
	   r'':{
	      "stream":"http://pedscases.libsyn.com/rss",
	      "image":"",
	      "name":"Pedscases.com: Pediatrics for Medical Students"
	   },
	   r'':{
	      "stream":"http://xsfm.co.kr/xml/p25.xml",
	      "image":"",
	      "name":"Perfect25 English Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/PermacultureVoicesPodcast",
	      "image":"",
	      "name":"Permaculture Voices: Profitable and Practical Permaculture - Focusing on Farming, Business, Design"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/PersonalGrowthPodcast",
	      "image":"",
	      "name":"Personal Growth Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/PersonalityHackerPodcast",
	      "image":"",
	      "name":"Personality Hacker Podcast"
	   },
	   r'':{
	      "stream":"http://www.peta.org/scripts/podcast.xml",
	      "image":"",
	      "name":"PETA's Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/the-mmqb-king",
	      "image":"",
	      "name":"Peter King, The MMQB Podcast"
	   },
	   r'':{
	      "stream":"http://philosophizethis.libsyn.com/rss",
	      "image":"",
	      "name":"Philosophize This!"
	   },
	   r'':{
	      "stream":"http://philosophybites.libsyn.com/rss",
	      "image":"",
	      "name":"Philosophy Bites"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:271543223/sounds.rss",
	      "image":"",
	      "name":"PhishCast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/blogspot/VIQv",
	      "image":"",
	      "name":"PHOTOGRAPHY 101"
	   },
	   r'':{
	      "stream":"http://physicianassistantboards.libsyn.com/rss",
	      "image":"",
	      "name":"Physician Assistant Boards Podcast: Exam Review | Medicine | PANCE Preparation |"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/physicianassistantexamreviewpodcasts",
	      "image":"",
	      "name":"Physician Assistant Exam Review"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510056",
	      "image":"",
	      "name":"Piano Jazz Shorts"
	   },
	   r'':{
	      "stream":"http://pintswithaquinas.libsyn.com/rss",
	      "image":"",
	      "name":"Pints With Aquinas"
	   },
	   r'':{
	      "stream":"http://www.planetary.org/multimedia/podcasts/planetary-radio-podcast-rss.xml",
	      "image":"",
	      "name":"Planetary Radio: Space Exploration, Astronomy and Science"
	   },
	   r'':{
	      "stream":"http://www.pleasefinishyourbook.com/feed/podcast",
	      "image":"",
	      "name":"Please, Finish Your Book!"
	   },
	   r'':{
	      "stream":"http://feeds.ign.com/ignfeeds/podcasts/beyond/",
	      "image":"",
	      "name":"Podcast Beyond"
	   },
	   r'':{
	      "stream":"http://feeds.ign.com/ignfeeds/podcasts/xbox360/",
	      "image":"",
	      "name":"Podcast Unlocked"
	   },
	   r'':{
	      "stream":"http://pointofinquiry.libsyn.com/rss",
	      "image":"",
	      "name":"Point of Inquiry"
	   },
	   r'':{
	      "stream":"http://feeds2.feedburner.com/POLICE-Podcasts?format=xml",
	      "image":"",
	      "name":"POLICE Magazine - Podcasts"
	   },
	   r'':{
	      "stream":"http://americaoutloud.com/feed/police-radio/",
	      "image":"",
	      "name":"POLICE RADIO"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:174823287/sounds.rss",
	      "image":"",
	      "name":"Policing Matters"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/squarespace/WtCx",
	      "image":"",
	      "name":"Politics Politics Politics"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/polygonqualitycontrol",
	      "image":"",
	      "name":"Polygon's Quality Control"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510282",
	      "image":"",
	      "name":"Pop Culture Happy Hour"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"Pop Culture Leftovers,"
	   },
	   r'':{
	      "stream":"https://feeds.podtrac.com/_-sJYvsFQrn_",
	      "image":"",
	      "name":"Popcast"
	   },
	   r'':{
	      "stream":"http://pottercast.libsyn.com/rss",
	      "image":"",
	      "name":"PotterCast - The Harry Potter Podcast"
	   },
	   r'':{
	      "stream":"http://powerandpurpose.libsyn.com/rss",
	      "image":"",
	      "name":"Power & Purpose With Mastin Kipp"
	   },
	   r'':{
	      "stream":"http://powerofmoms.libsyn.com/rss",
	      "image":"",
	      "name":"Power of Moms Radio"
	   },
	   r'':{
	      "stream":"http://powertradingradio.libsyn.com/rss",
	      "image":"",
	      "name":"Power Trading Radio - A Trader's Perspective on Investing in Stocks, Futures, Forex, Options Podcast"
	   },
	   r'':{
	      "stream":"http://prageru.dreamhosters.com/podcastgen/feed.xml",
	      "image":"",
	      "name":"PragerU"
	   },
	   r'':{
	      "stream":"http://www.pray-as-you-go.org/podcast_en.xml",
	      "image":"",
	      "name":"pray-as-you-go"
	   },
	   r'':{
	      "stream":"https://www.preciouslittlesleep.com/feed/podcast/",
	      "image":"",
	      "name":"Precious Little Sleep Parenting Podcast"
	   },
	   r'':{
	      "stream":"http://pregame.libsyn.com/rss",
	      "image":"",
	      "name":"Pregame.com's FIRST PREVIEW (ESPN Las Vegas)"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/PregnancyConfidential",
	      "image":"",
	      "name":"Pregnancy Confidential"
	   },
	   r'':{
	      "stream":"http://thepregnancypodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Pregnancy Podcast"
	   },
	   r'':{
	      "stream":"http://audiblepapt.libsyn.com/rss",
	      "image":"",
	      "name":"Presidents Are People Too!"
	   },
	   r'':{
	      "stream":"http://primalblueprint.libsyn.com/rss",
	      "image":"",
	      "name":"Primal Blueprint Podcast"
	   },
	   r'':{
	      "stream":"http://probablyscience.libsyn.com/rss",
	      "image":"",
	      "name":"Probably Science"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ProgrammingThrowdown",
	      "image":"",
	      "name":"Programming Throwdown"
	   },
	   r'':{
	      "stream":"http://podcasts.protocol-radio.com/PRRADIO.xml",
	      "image":"",
	      "name":"Protocol Radio"
	   },
	   r'':{
	      "stream":"http://proverbs31.org/feed/podcast/",
	      "image":"",
	      "name":"Proverbs 31 Ministries"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/nOTae4fRptyc",
	      "image":"",
	      "name":"PS I Love You XOXO"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/psychobabble",
	      "image":"",
	      "name":"Psychobabble with Tyler Oakley & Korey Kuhl"
	   },
	   r'':{
	      "stream":"http://psychsessions.com/feed/podcast/",
	      "image":"",
	      "name":"Psychology Illustrated: Psych Sessions Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/thepsychfiles",
	      "image":"",
	      "name":"Psychology in Everyday Life: The Psych Files"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=2406595",
	      "image":"",
	      "name":"PTI"
	   },
	   r'':{
	      "stream":"http://www.kaltura.com/api_v3/getFeed.php?partnerId=32325&feedId=1_2ykb44sa",
	      "image":"",
	      "name":"Public-Private Partnerships - MOOC (audio)"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"Pumped Podcast,"
	   },
	   r'':{
	      "stream":"http://www.purenonfiction.net/feed/podcast/",
	      "image":"",
	      "name":"Pure Nonfiction: Inside Documentary Film"
	   },
	   r'':{
	      "stream":"http://www.quantamagazine.org/feed/podcast/",
	      "image":"",
	      "name":"Quanta Science Podcast"
	   },
	   r'':{
	      "stream":"http://www.cbc.ca/podcasting/includes/quirksaio.xml",
	      "image":"",
	      "name":"Quirks and Quarks Complete Show from CBC Radio"
	   },
	   r'':{
	      "stream":"https://www.residentadvisor.net/xml/podcast.xml",
	      "image":"",
	      "name":"RA Podcast"
	   },
	   r'':{
	      "stream":"http://radicalpersonalfinance.libsyn.com/rss",
	      "image":"",
	      "name":"Radical Personal Finance: Financial Independence, Early Retirement, Investing, Insurance, Financial Planning"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510315",
	      "image":"",
	      "name":"Radio Ambulante"
	   },
	   r'':{
	      "stream":"http://www.unmultimedia.org/radio/spanish/feed/itunes/index.xml",
	      "image":"",
	      "name":"Radio de las Naciones Unidas"
	   },
	   r'':{
	      "stream":"http://detective.libsyn.com/rss",
	      "image":"",
	      "name":"Radio Detective Story Hour"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:77542725/sounds.rss",
	      "image":"",
	      "name":"Radio Headspace"
	   },
	   r'':{
	      "stream":"http://radiowest.kuer.org/podcasts/220/rss.xml",
	      "image":"",
	      "name":"RadioWest Podcasts"
	   },
	   r'':{
	      "stream":"http://ramdasshereandnow.libsyn.com/rss",
	      "image":"",
	      "name":"Ram Dass Here And Now"
	   },
	   r'':{
	      "stream":"http://www.rand.org/multimedia/podcasts/xml/congressional_briefing_series.xml",
	      "image":"",
	      "name":"RAND Congressional Briefing Series Podcast"
	   },
	   r'':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1327?format=MP3_128K",
	      "image":"",
	      "name":"Rap Radar Podcast"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"Rationally Speaking,"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:158340237/sounds.rss",
	      "image":"",
	      "name":"Read Scripture Podcast Series"
	   },
	   r'':{
	      "stream":"https://amongstlovelythings.com/feed/podcast/",
	      "image":"",
	      "name":"Read-Aloud Revival"
	   },
	   r'':{
	      "stream":"http://rss.art19.com/real-crime-profile",
	      "image":"",
	      "name":"Real Crime Profile"
	   },
	   r'':{
	      "stream":"http://www.iradeo.com/113248/feed/143029.xml",
	      "image":"",
	      "name":"REAL DEAL MUSIC RADIO"
	   },
	   r'':{
	      "stream":"http://realestatenews.libsyn.com/rss",
	      "image":"",
	      "name":"Real Estate News | Real Estate Investing | Stock Market Investing | Passive Income | Flipping | 1031 Exchange | Private Lending"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4567086.rss",
	      "image":"",
	      "name":"REAL GHOST STORIES ONLINE | Paranormal | Supernatural | Unexplained | Haunted"
	   },
	   r'':{
	      "stream":"http://realitybytespod.videopodcastnetwork.libsynpro.com/rss",
	      "image":"",
	      "name":"REALITY BYTES with Stephanie Beatriz & Courtney Kocak"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/CarollaReasonableDoubt",
	      "image":"",
	      "name":"Reasonable Doubt"
	   },
	   r'':{
	      "stream":"http://rebelfm.libsyn.com/rss",
	      "image":"",
	      "name":"Rebel FM"
	   },
	   r'':{
	      "stream":"http://rebelforceradio.libsyn.com/rss",
	      "image":"",
	      "name":"Rebel Force Radio: Star Wars Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:184343600/sounds.rss",
	      "image":"",
	      "name":"Reclaimed Audio Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/Recode-Decode",
	      "image":"",
	      "name":"Recode Decode, hosted by Kara Swisher"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/Recode-Media",
	      "image":"",
	      "name":"Recode Media with Peter Kafka"
	   },
	   r'':{
	      "stream":"http://idopodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Relationships, Sex, Dating and Marriage Advice - I Do Podcast"
	   },
	   r'':{
	      "stream":"http://www.relevantmagazine.com/taxonomy/term/79/feed",
	      "image":"",
	      "name":"RELEVANT Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.ligonier.org/RenewingYourMind",
	      "image":"",
	      "name":"Renewing Your Mind with R.C. Sproul"
	   },
	   r'':{
	      "stream":"http://residualincomepodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Residual Income Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:91056977/sounds.rss",
	      "image":"",
	      "name":"Respectful Parenting: Janet Lansbury Unruffled"
	   },
	   r'':{
	      "stream":"http://retronauts.libsyn.com/rss",
	      "image":"",
	      "name":"Retronauts"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ReverberationRadio",
	      "image":"",
	      "name":"Reverberation Radio"
	   },
	   r'':{
	      "stream":"http://www.reviveourhearts.com/podcasts/revive-our-hearts.rss",
	      "image":"",
	      "name":"Revive Our Hearts with Nancy DeMoss Wolgemuth"
	   },
	   r'':{
	      "stream":"http://chriskresser.com/feed/podcast",
	      "image":"",
	      "name":"Revolution Health Radio"
	   },
	   r'':{
	      "stream":"http://revolutionspodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Revolutions"
	   },
	   r'':{
	      "stream":"http://rewildyourself.libsyn.com/rss",
	      "image":"",
	      "name":"ReWild Yourself"
	   },
	   r'':{
	      "stream":"http://richdadradio.libsyn.com/rss",
	      "image":"",
	      "name":"Rich Dad Radio Show: In-Your-Face Advice on Investing, Personal Finance, & Starting a Business"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/RickWarrensMinistryPodcastShow",
	      "image":"",
	      "name":"Rick Warren's Ministry Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/RingerUniversity",
	      "image":"",
	      "name":"Ringer University"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"RINGTONE,"
	   },
	   r'':{
	      "stream":"http://risk.libsyn.com/rss",
	      "image":"",
	      "name":"RISK!"
	   },
	   r'':{
	      "stream":"http://risky.biz/feeds/risky-business",
	      "image":"",
	      "name":"Risky Business"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/RobCesternino",
	      "image":"",
	      "name":"Rob Has a Podcast | Survivor / Big Brother / Amazing Race - RHAP"
	   },
	   r'':{
	      "stream":"http://robbwolf.libsyn.com/rss",
	      "image":"",
	      "name":"Robb Wolf - The Paleo Solution Podcast - Paleo diet, nutrition, fitness, and health"
	   },
	   r'':{
	      "stream":"http://feeds.megaphone.fm/rollingstonemusicnow",
	      "image":"",
	      "name":"Rolling Stone Music Now"
	   },
	   r'':{
	      "stream":"http://roncarpenter.libsyn.com/rss",
	      "image":"",
	      "name":"Ron Carpenter TV"
	   },
	   r'':{
	      "stream":"http://roosterteeth.com/show/rt-podcast/feed/mp3",
	      "image":"",
	      "name":"Rooster Teeth Podcast"
	   },
	   r'':{
	      "stream":"http://rosebuddies.libsyn.com/rss",
	      "image":"",
	      "name":"Rose Buddies"
	   },
	   r'':{
	      "stream":"https://rotogrinders.com/podcasts.rss",
	      "image":"",
	      "name":"RotoGrinders Daily Fantasy Fix"
	   },
	   r'':{
	      "stream":"http://rulebreakerinvesting.libsyn.com/rss",
	      "image":"",
	      "name":"Rule Breaker Investing"
	   },
	   r'':{
	      "stream":"http://rupaul.libsyn.com/rupaul.rss",
	      "image":"",
	      "name":"RuPaul: What's The Tee? with Michelle Visage"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=3028618",
	      "image":"",
	      "name":"Russillo & Kanell"
	   },
	   r'':{
	      "stream":"http://rzim.org/just-thinking-broadcasts/feed/",
	      "image":"",
	      "name":"RZIM: Just Thinking Broadcasts"
	   },
	   r'':{
	      "stream":"http://rzim.org/let-my-people-think-broadcasts/feed/",
	      "image":"",
	      "name":"RZIM: Let My People Think Broadcasts"
	   },
	   r'':{
	      "stream":"http://mediacenter.saddleback.com/mc/podcaststream.aspx?p=1&iid=-1&site=1",
	      "image":"",
	      "name":"Saddleback Church Weekend Messages"
	   },
	   r'':{
	      "stream":"http://samrobertswrestling.libsyn.com/rss",
	      "image":"",
	      "name":"Sam Roberts Wrestling Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.gimletmedia.com/samplershow",
	      "image":"",
	      "name":"Sampler"
	   },
	   r'':{
	      "stream":"http://www.blogtalkradio.com/bigfoothotspot/podcast",
	      "image":"",
	      "name":"Sasquatch Chronicles"
	   },
	   r'':{
	      "stream":"http://podcast.sasquatchsyndicate.com/rss",
	      "image":"",
	      "name":"Sasquatch Syndicate"
	   },
	   r'':{
	      "stream":"http://savagelove.libsyn.com/rss",
	      "image":"",
	      "name":"Savage Lovecast"
	   },
	   r'':{
	      "stream":"http://sawbones.libsyn.com/rss",
	      "image":"",
	      "name":"Sawbones: A Marital Tour of Misguided Medicine"
	   },
	   r'':{
	      "stream":"http://nojargon.libsyn.com/rss",
	      "image":"",
	      "name":"Scholars Strategy Network's No Jargon"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"School Sucks,"
	   },
	   r'':{
	      "stream":"http://www.sciencefriday.com/feed/podcast/podcast-video",
	      "image":"",
	      "name":"Science Friday Videos"
	   },
	   r'':{
	      "stream":"http://www.bbc.co.uk/programmes/p002vsnb/episodes/downloads.rss",
	      "image":"",
	      "name":"Science in Action"
	   },
	   r'':{
	      "stream":"http://www.sciencemag.org/rss/podcast.xml",
	      "image":"",
	      "name":"Science Magazine Podcast"
	   },
	   r'':{
	      "stream":"https://www.scientificamerican.com/sciam/xml/iTunes.cfm?id=science-talk",
	      "image":"",
	      "name":"Science Talk"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:154052752/sounds.rss",
	      "image":"",
	      "name":"Science Vs - Season 1"
	   },
	   r'':{
	      "stream":"http://sciencesortof.libsyn.com/rss",
	      "image":"",
	      "name":"Science... sort of"
	   },
	   r'':{
	      "stream":"http://api.breakmedia.com/content/contentfeed/get?apiRequestJson=%7bid:1179,pageNumber:1,pageSize:52,responseType:%22itunespodcastrss%22%7d",
	      "image":"",
	      "name":"ScreenJunkies Movie Fights"
	   },
	   r'':{
	      "stream":"http://scriptnotes.net/rss",
	      "image":"",
	      "name":"Scriptnotes Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:196546667/sounds.rss",
	      "image":"",
	      "name":"Secular Buddhism"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/sn.xml",
	      "image":"",
	      "name":"Security Now (MP3)"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/seesomethingsaysomething",
	      "image":"",
	      "name":"See Something Say Something"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/Selected-Shorts",
	      "image":"",
	      "name":"Selected Shorts"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TooHotForRadio",
	      "image":"",
	      "name":"Selected Shorts: Too Hot For Radio"
	   },
	   r'':{
	      "stream":"http://selfmademan.libsyn.com/rss",
	      "image":"",
	      "name":"Self Made Man"
	   },
	   r'':{
	      "stream":"http://www.theselfsufficientlife.com/feed/podcast/",
	      "image":"",
	      "name":"Self-Sufficient Life: Homesteading | Preparedness | Prepping | Simple Living"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/libsyn/vbTa",
	      "image":"",
	      "name":"Serendipity"
	   },
	   r'':{
	      "stream":"http://feed.desiringgod.org/sermon-of-the-day.rss",
	      "image":"",
	      "name":"Sermon of the Day"
	   },
	   r'':{
	      "stream":"http://downloads.cdn.sesame.org/podcast/rss/rss.xml",
	      "image":"",
	      "name":"Sesame Street Podcast"
	   },
	   r'':{
	      "stream":"http://rss.earwolf.com/startup-school",
	      "image":"",
	      "name":"Seth Godin's Startup School"
	   },
	   r'':{
	      "stream":"http://sexgetsreal.libsyn.com/rss",
	      "image":"",
	      "name":"Sex Gets Real: Talking Sex, Relationships, and Kink with Dawn Serra"
	   },
	   r'':{
	      "stream":"http://rss.art19.com/sex-nerd-sandra.xml",
	      "image":"",
	      "name":"Sex Nerd Sandra"
	   },
	   r'':{
	      "stream":"http://emilymorse.libsyn.com/rss",
	      "image":"",
	      "name":"Sex With Emily"
	   },
	   r'':{
	      "stream":"http://sherlock.libsyn.com/rss",
	      "image":"",
	      "name":"Sherlock Holmes Adventures"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ShrinkRapRadio-APsychologyTalkAndInterviewShow",
	      "image":"",
	      "name":"Shrink Rap Radio Psychology Interviews: Exploring brain, body, mind, spirit, intuition, leadership, research, psychotherapy and"
	   },
	   r'':{
	      "stream":"http://sidehustlepro.libsyn.com/rss",
	      "image":"",
	      "name":"Side Hustle Pro: Female Entrepreneurs | Black Women Business Owners | Sidepreneurs"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/Q2-QW4_lLftD",
	      "image":"",
	      "name":"Sidedoor"
	   },
	   r'':{
	      "stream":"http://silentsalesmachine.libsyn.com/rss",
	      "image":"",
	      "name":"Silent Sales Machine Radio"
	   },
	   r'':{
	      "stream":"http://cinemasins.libsyn.com/rss",
	      "image":"",
	      "name":"SinCast - Presented by CinemaSins"
	   },
	   r'':{
	      "stream":"http://skeptoid.com/podcast.xml",
	      "image":"",
	      "name":"Skeptoid"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SkipandShannonUndisputed",
	      "image":"",
	      "name":"Skip and Shannon: Undisputed"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SlateMoney",
	      "image":"",
	      "name":"Slate Money"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SlateLexiconValley",
	      "image":"",
	      "name":"Slate Presents Lexicon Valley"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SlateAudioBookClub",
	      "image":"",
	      "name":"Slate's Audio Book Club"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SlateCultureGabfest",
	      "image":"",
	      "name":"Slate's Culture Gabfest"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SlateMomAndDadAreFighting",
	      "image":"",
	      "name":"Slate's Mom and Dad Are Fighting"
	   },
	   r'':{
	      "stream":"http://sleepwithmepodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Sleep With Me | Helps You Fall Asleep Via Silly Boring Bedtime Stories"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/silknature",
	      "image":"",
	      "name":"Sleep with Silk: Nature Sounds (to help insomnia, anxiety, stress, relax, focus, meditate, ASMR)"
	   },
	   r'':{
	      "stream":"http://feeds.schlaflosinmuenchen.com/slowsim.xml",
	      "image":"",
	      "name":"Slow German"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SlumberPartyWithAlieAndGeorgia",
	      "image":"",
	      "name":"Slumber Party With Alie and Georgia"
	   },
	   r'':{
	      "stream":"http://smalltownhorror.libsyn.com/rss",
	      "image":"",
	      "name":"Small Town Horror"
	   },
	   r'':{
	      "stream":"http://feeds.smartdrugsmarts.com/podcast/sds.xml",
	      "image":"",
	      "name":"Smart Drug Smarts: Brain Optimization | Nootropics | Neuroscience"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SModcasts",
	      "image":"",
	      "name":"SModcast"
	   },
	   r'':{
	      "stream":"http://sneakattack.libsyn.com/rss",
	      "image":"",
	      "name":"Sneak Attack!: A Dungeons and Dragons Adventure"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:213836126/sounds.rss",
	      "image":"",
	      "name":"Snoop Dogg's GGN Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.megaphone.fm/somoney",
	      "image":"",
	      "name":"So Money with Farnoosh Torabi"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SocialMediaMarketingFeed",
	      "image":"",
	      "name":"Social Media Marketing Podcast helps your business thrive with social media"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:118369573/sounds.rss",
	      "image":"",
	      "name":"SOFREP Radio"
	   },
	   r'':{
	      "stream":"http://softwareengineeringdaily.com/feed/podcast/",
	      "image":"",
	      "name":"Software Engineering Daily"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/se-radio",
	      "image":"",
	      "name":"Software Engineering Radio - The Podcast for Professional Software Developers"
	   },
	   r'':{
	      "stream":"http://solomonster.podbean.com/feed/",
	      "image":"",
	      "name":"Solomonster Sounds Off"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4792166.rss",
	      "image":"",
	      "name":"Something to Wrestle with Bruce Prichard"
	   },
	   r'':{
	      "stream":"http://songexploder.libsyn.com/rss",
	      "image":"",
	      "name":"Song Exploder"
	   },
	   r'':{
	      "stream":"https://feeds.publicradio.org/public_feeds/song-of-the-day/itunes/rss",
	      "image":"",
	      "name":"Song of the Day"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/Songarab",
	      "image":"",
	      "name":"songarab"
	   },
	   r'':{
	      "stream":"http://feeds.wnyc.org/sooomanywhiteguys",
	      "image":"",
	      "name":"Sooo Many White Guys"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheSoundOpinionsPodcast",
	      "image":"",
	      "name":"Sound Opinions"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/thisweekinsoundcloud",
	      "image":"",
	      "name":"SoundCloud Community"
	   },
	   r'':{
	      "stream":"http://www.soundsofthetrail.com/?feed=podcast",
	      "image":"",
	      "name":"Sounds of the Trail"
	   },
	   r'':{
	      "stream":"http://www.soundstrue.com/podcast/feed/podcast/",
	      "image":"",
	      "name":"Sounds True: Insights at the Edge"
	   },
	   r'':{
	      "stream":"http://www.edufone.com/rss.xml",
	      "image":"",
	      "name":"Spanish A+ - Finally Learn Spanish with Bilingual Podcasts"
	   },
	   r'':{
	      "stream":"http://newsinslowspanish.libsyn.com/rss",
	      "image":"",
	      "name":"Spanish Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/stritunes",
	      "image":"",
	      "name":"Spare the Rock, Spoil the Child Playlists"
	   },
	   r'':{
	      "stream":"http://sparklestories.libsyn.com/rss",
	      "image":"",
	      "name":"Sparkle Stories Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SpawnedWithKristenAndLizOfCoolmompicks",
	      "image":"",
	      "name":"Spawned with Kristen and Liz of CoolMomPicks"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/speak-for-yourself",
	      "image":"",
	      "name":"Speak For Yourself with Cowherd & Whitlock"
	   },
	   r'':{
	      "stream":"http://speakspanish.libsyn.com/rss",
	      "image":"",
	      "name":"Speak Spanish with Maria Fernandez. Easy Spanish lessons & drills to help you become fluent in no time!"
	   },
	   r'':{
	      "stream":"http://kuow.org/podcasts/721/rss.xml",
	      "image":"",
	      "name":"Speakers Forum"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SpeakingOfPsychology",
	      "image":"",
	      "name":"Speaking of Psychology"
	   },
	   r'':{
	      "stream":"http://seriouseats.libsyn.com/rss",
	      "image":"",
	      "name":"Special Sauce with Ed Levine"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SpeedDial",
	      "image":"",
	      "name":"Speed Dial"
	   },
	   r'':{
	      "stream":"http://spinninsessions.spinninpodcasts.com/rss",
	      "image":"",
	      "name":"Spinnin' Sessions"
	   },
	   r'':{
	      "stream":"http://spiritspodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Spirits: A Drunken Dive into Myths and Legends"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SpittinChiclets",
	      "image":"",
	      "name":"Spittin' Chiclets"
	   },
	   r'':{
	      "stream":"http://rss.earwolf.com/spontaneanation-with-paul-f-tompkins",
	      "image":"",
	      "name":"SPONTANEANATION with Paul F. Tompkins"
	   },
	   r'':{
	      "stream":"http://www.spreaker.com/user/8206201/episodes/feed",
	      "image":"",
	      "name":"Sports Gambling Radio - By BangTheBook"
	   },
	   r'':{
	      "stream":"http://stackingbenjamins.libsyn.com/rss",
	      "image":"",
	      "name":"Stacking Benjamins: Earn, Save, and Spend Money With a Plan"
	   },
	   r'':{
	      "stream":"http://ecorner.stanford.edu/StanfordInnovationLab.xml",
	      "image":"",
	      "name":"Stanford Innovation Lab with Tina Seelig"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/StarWarsMinute",
	      "image":"",
	      "name":"Star Wars Minute"
	   },
	   r'':{
	      "stream":"http://feeds.hearstartup.com/hearstartup",
	      "image":"",
	      "name":"StartUp Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:150759713/sounds.rss",
	      "image":"",
	      "name":"Startup School Radio"
	   },
	   r'':{
	      "stream":"https://www.ihmc.us/stemtalk/feed/podcast/",
	      "image":"",
	      "name":"STEM-Talk"
	   },
	   r'':{
	      "stream":"http://6ftmama.com/feed/podcast/",
	      "image":"",
	      "name":"Still Growing...A Weekly Gardening Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/LhS5ax2CPGou",
	      "image":"",
	      "name":"Still Processing"
	   },
	   r'':{
	      "stream":"http://www.tested.com/podcast-xml/still-untitled-the-adam-savage-project/",
	      "image":"",
	      "name":"Still Untitled: The Adam Savage Project"
	   },
	   r'':{
	      "stream":"http://rss.art19.com/stories-podcast",
	      "image":"",
	      "name":"Stories Podcast - A Free Children's Story Podcast for Bedtime, Car Rides, and Kids of All Ages!"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/StoryAndStarWars",
	      "image":"",
	      "name":"Story and Star Wars"
	   },
	   r'':{
	      "stream":"http://storypirates.libsyn.com/rss",
	      "image":"",
	      "name":"Story Pirates Podcast"
	   },
	   r'':{
	      "stream":"http://bedtime.fm/storytime/feed",
	      "image":"",
	      "name":"Story Time - Free children's bedtime stories for your kids"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510200",
	      "image":"",
	      "name":"StoryCorps"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/Storynory",
	      "image":"",
	      "name":"Storynory - Stories for Kids"
	   },
	   r'':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1243?format=MP3_128K",
	      "image":"",
	      "name":"Straight Up with Stassi"
	   },
	   r'':{
	      "stream":"http://feeds.strangersnomore.org/StrangersNoMore",
	      "image":"",
	      "name":"Strangers"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/AnatomyOfMarriage",
	      "image":"",
	      "name":"Stronger Marriages: Anatomy of Marriage"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/StudentOfTheGunRadio",
	      "image":"",
	      "name":"Student of the Gun Radio"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/studio360/podcast",
	      "image":"",
	      "name":"Studio 360 with Kurt Andersen"
	   },
	   r'':{
	      "stream":"http://www.howstuffworks.com/podcasts/stuff-mom-never-told-you.rss",
	      "image":"",
	      "name":"Stuff Mom Never Told You"
	   },
	   r'':{
	      "stream":"http://www.howstuffworks.com/podcasts/stuff-they-dont-want-you-to-know.rss",
	      "image":"",
	      "name":"Stuff They Don't Want You To Know"
	   },
	   r'':{
	      "stream":"http://www.howstuffworks.com/podcasts/stuff-they-dont-want-you-to-know-audio.rss",
	      "image":"",
	      "name":"Stuff They Don't Want You To Know Audio"
	   },
	   r'':{
	      "stream":"http://www.howstuffworks.com/podcasts/stuff-to-blow-your-mind.rss",
	      "image":"",
	      "name":"Stuff To Blow Your Mind"
	   },
	   r'':{
	      "stream":"http://successtalks.libsyn.com/rss",
	      "image":"",
	      "name":"SUCCESS Talks"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/sundaysupplement",
	      "image":"",
	      "name":"Sunday Supplement - Sky Sports"
	   },
	   r'':{
	      "stream":"http://superbestfriendcast.libsyn.com/rss",
	      "image":"",
	      "name":"Super Best Friendcast!"
	   },
	   r'':{
	      "stream":"http://surgery101.libsyn.com/rss",
	      "image":"",
	      "name":"Surgery 101"
	   },
	   r'':{
	      "stream":"http://feeds.gimletmedia.com/surprisinglyawesome",
	      "image":"",
	      "name":"Surprisingly Awesome"
	   },
	   r'':{
	      "stream":"http://survivalmomradio.libsyn.com/rss",
	      "image":"",
	      "name":"Survival Mom Podcast"
	   },
	   r'':{
	      "stream":"http://drumguru.hipcast.com/rss/everyday_survival.xml",
	      "image":"",
	      "name":"Survivalist.com: Survival | Preparedness | Prepper"
	   },
	   r'':{
	      "stream":"http://joannandstacy.libsyn.com/rss",
	      "image":"",
	      "name":"Survivor Fans Podcast"
	   },
	   r'':{
	      "stream":"http://pdcastsusworldradio.libsyn.com/rss",
	      "image":"",
	      "name":"Sustainable World Radio- Ecology and Permaculture Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/SwitchedOnPopPodcast",
	      "image":"",
	      "name":"Switched On Pop"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4854348.rss",
	      "image":"",
	      "name":"Tactical Talk with Allison Barrie"
	   },
	   r'':{
	      "stream":"http://thetailopezshow.libsyn.com/rss",
	      "image":"",
	      "name":"Tai Lopez Book Of The Day Show"
	   },
	   r'':{
	      "stream":"http://horrortales.libsyn.com/rss",
	      "image":"",
	      "name":"Tales of Horror Podcast"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"TALK NERDY"
	   },
	   r'':{
	      "stream":"https://talkpython.fm/episodes/rss",
	      "image":"",
	      "name":"Talk Python To Me - Python conversations for passionate developers"
	   },
	   r'':{
	      "stream":"http://talktomeinkorean.libsyn.com/rss",
	      "image":"",
	      "name":"Talk To Me In Korean"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"Talking Machines,"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/LaserTimeTalkingSimpsons",
	      "image":"",
	      "name":"Talking Simpsons"
	   },
	   r'':{
	      "stream":"http://tangent.libsyn.com/rss",
	      "image":"",
	      "name":"Tangentially Speaking with Dr. Christopher Ryan"
	   },
	   r'':{
	      "stream":"http://tanis.libsyn.com/rss",
	      "image":"",
	      "name":"TANIS"
	   },
	   r'':{
	      "stream":"http://tarabrach.libsyn.com/rss",
	      "image":"",
	      "name":"Tara Brach"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:143461576/sounds.rss",
	      "image":"",
	      "name":"Tax Season"
	   },
	   r'':{
	      "stream":"http://taylortalk.libsyn.com/rss",
	      "image":"",
	      "name":"Taylor Talk: The Taylor Swift Podcast | 1989 | Shake It Off | Blank Space | Red | Speak Now | Fearless | Taylor Swift"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TdJakesPodcast",
	      "image":"",
	      "name":"TD Jakes Podcast"
	   },
	   r'':{
	      "stream":"http://www.blogtalkradio.com/laura-mize/podcast",
	      "image":"",
	      "name":"Teach Me To Talk with Laura and Friends"
	   },
	   r'':{
	      "stream":"http://images.beachbody.com/podcasts/beachbodycoach.xml",
	      "image":"",
	      "name":"Team Beachbody Coach Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/EJbKUnHP5ywQ",
	      "image":"",
	      "name":"Tech News This Week"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/tnt.xml",
	      "image":"",
	      "name":"Tech News Today (MP3)"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TechnoLiveSets",
	      "image":"",
	      "name":"Techno Live Sets TLS Podcast"
	   },
	   r'':{
	      "stream":"http://www.howstuffworks.com/podcasts/techstuff.rss",
	      "image":"",
	      "name":"TechStuff"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/Ted-edPodcast",
	      "image":"",
	      "name":"TED-Ed: Lessons Worth Sharing"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TedtalksHD",
	      "image":"",
	      "name":"TEDTalks (hd)"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TEDTalks_video",
	      "image":"",
	      "name":"TEDTalks (video)"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/iTunesPodcastTTArts",
	      "image":"",
	      "name":"TEDTalks Art"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/iTunesPodcastTTEducation",
	      "image":"",
	      "name":"TEDTalks Education"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/iTunesPodcastTTHealth",
	      "image":"",
	      "name":"TEDTalks Health"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/iTunesPodcastTTKidsFamily",
	      "image":"",
	      "name":"TEDTalks Kids and Family"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/iTunesPodcastTTMusic",
	      "image":"",
	      "name":"TEDTalks Music"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/iTunesPodcastTTScienceMedicine",
	      "image":"",
	      "name":"TEDTalks Science and Medicine"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/iTunesPodcastTTSocietyCulture",
	      "image":"",
	      "name":"TEDTalks Society and Culture"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/iTunesPodcastTTTechnology",
	      "image":"",
	      "name":"TEDTalks Technology"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TellEmSteveDave",
	      "image":"",
	      "name":"Tell 'Em Steve-Dave"
	   },
	   r'':{
	      "stream":"https://rss.art19.com/terms",
	      "image":"",
	      "name":"Terms"
	   },
	   r'':{
	      "stream":"https://feeds.publicradio.org/public_feeds/terrible-thanks-for-asking/itunes/rss",
	      "image":"",
	      "name":"Terrible, Thanks For Asking"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:172452163/sounds.rss",
	      "image":"",
	      "name":"That's Not Metal"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/filmcast",
	      "image":"",
	      "name":"The /Filmcast"
	   },
	   r'':{
	      "stream":"http://askgaryvee.garyvee.libsynpro.com/rss",
	      "image":"",
	      "name":"The #AskGaryVee Show"
	   },
	   r'':{
	      "stream":"http://100mba.net/category/show/feed/",
	      "image":"",
	      "name":"The $100 MBA Show"
	   },
	   r'':{
	      "stream":"http://feed.cnet.com/feed/podcast/359-podcast-audio.xml",
	      "image":"",
	      "name":"The 3:59"
	   },
	   r'':{
	      "stream":"http://feedpress.me/jeffsanders",
	      "image":"",
	      "name":"The 5 AM Miracle with Jeff Sanders: Healthy Habits | Personal Development | Rockin' Productivity"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheAdamAndDrewShow",
	      "image":"",
	      "name":"The Adam and Dr. Drew Show"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheAdamCarollaPodcast",
	      "image":"",
	      "name":"The Adam Carolla Show"
	   },
	   r'':{
	      "stream":"http://finncaspian.libsyn.com/rss",
	      "image":"",
	      "name":"The Alien Adventures of Finn Caspian: Science Fiction for Kids"
	   },
	   r'':{
	      "stream":"http://feeds.theallusionist.org/Allusionist",
	      "image":"",
	      "name":"The Allusionist"
	   },
	   r'':{
	      "stream":"http://www.oneplace.com/ministries/the-alternative/subscribe/podcast.xml",
	      "image":"",
	      "name":"The Alternative on OnePlace.com"
	   },
	   r'':{
	      "stream":"http://altonbrown.com/feed/podcast/",
	      "image":"",
	      "name":"The Alton Browncast"
	   },
	   r'':{
	      "stream":"http://theamazingseller.com/feed/podcast/",
	      "image":"",
	      "name":"The Amazing Seller Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/theangrychicken",
	      "image":"",
	      "name":"The Angry Chicken: A Hearthstone Podcast"
	   },
	   r'':{
	      "stream":"http://static.anjunadeep.com/edition/podcast.xml",
	      "image":"",
	      "name":"The Anjunadeep Edition"
	   },
	   r'':{
	      "stream":"http://www.blogtalkradio.com/hahasforhoohaspodcast/podcast",
	      "image":"",
	      "name":"The Anna and Susannah Show"
	   },
	   r'':{
	      "stream":"http://anxietycoaches.libsyn.com/anxietycoaches",
	      "image":"",
	      "name":"The Anxiety Coaches Podcast - Relief from Anxiety, Panic, and PTSD"
	   },
	   r'':{
	      "stream":"http://s3.amazonaws.com/Public-Broadcast/aop-itunes.xml",
	      "image":"",
	      "name":"The Art of Photography"
	   },
	   r'':{
	      "stream":"http://babysittersclubclub.libsyn.com/rss",
	      "image":"",
	      "name":"The Baby-Sitters Club Club"
	   },
	   r'':{
	      "stream":"http://bcpod.libsyn.com/rss",
	      "image":"",
	      "name":"The BadChristian Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:169150534/sounds.rss",
	      "image":"",
	      "name":"The Basement Yard"
	   },
	   r'':{
	      "stream":"https://simplecast.com/podcasts/1434/rss",
	      "image":"",
	      "name":"The Bible Project"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510314",
	      "image":"",
	      "name":"The Big Listen"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=779",
	      "image":"",
	      "name":"The Big Podcast With Shaq"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheBillSimmonsPodcast",
	      "image":"",
	      "name":"The Bill Simmons Podcast"
	   },
	   r'':{
	      "stream":"http://birthhour.libsyn.com/rss",
	      "image":"",
	      "name":"The Birth Hour"
	   },
	   r'':{
	      "stream":"http://birthful.libsyn.com/rss",
	      "image":"",
	      "name":"The Birthful Podcast | Talking with Pregnancy, Birth, Breastfeeding, Postpartum & Parenting Pros to Inform Your Intuition"
	   },
	   r'':{
	      "stream":"http://theblacktapes.libsyn.com/rss",
	      "image":"",
	      "name":"The Black Tapes"
	   },
	   r'':{
	      "stream":"https://feeds.podtrac.com/hyqg9sb75nOH",
	      "image":"",
	      "name":"The Book Review"
	   },
	   r'':{
	      "stream":"http://bornyesterday.libsyn.com/rss",
	      "image":"",
	      "name":"The Born Yesterday Podcast"
	   },
	   r'':{
	      "stream":"http://boweryboys.libsyn.com/rss",
	      "image":"",
	      "name":"The Bowery Boys: New York City History"
	   },
	   r'':{
	      "stream":"http://amenclinics.libsyn.com/rss",
	      "image":"",
	      "name":"The Brain Warrior's Way Podcast"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"The Brewing Network Presents - The Sunday Session,"
	   },
	   r'':{
	      "stream":"http://thebrightsessions.libsyn.com/rss",
	      "image":"",
	      "name":"The Bright Sessions"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud%3Ausers%3A88794716/sounds.rss",
	      "image":"",
	      "name":"The Brilliant Idiots"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheBritishHistoryPodcast",
	      "image":"",
	      "name":"The British History Podcast"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/thebroadexperience",
	      "image":"",
	      "name":"The Broad Experience"
	   },
	   r'':{
	      "stream":"http://brookingscafeteriapodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Brookings Cafeteria"
	   },
	   r'':{
	      "stream":"http://briangburns.podhoster.com/rss/2402/",
	      "image":"",
	      "name":"The Brutal Truth About Sales & Selling - B2B Social LinkedIn SaaS Startup Cold Calling Email Advanced Skills"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheCanonPodcast",
	      "image":"",
	      "name":"The Canon"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/cnlpodcast",
	      "image":"",
	      "name":"The Carey Nieuwhof Leadership Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:259238942/sounds.rss",
	      "image":"",
	      "name":"The Casey Crew"
	   },
	   r'':{
	      "stream":"http://turbochargedlife.libsyn.com/rss",
	      "image":"",
	      "name":"The Chalene Show | Motivation | Leadership | Confidence | Family | Fitness and Life coaching with Chalene Johnson"
	   },
	   r'':{
	      "stream":"https://changelog.com/podcast/feed",
	      "image":"",
	      "name":"The Changelog"
	   },
	   r'':{
	      "stream":"http://brendonburchard.libsyn.com/rss",
	      "image":"",
	      "name":"The Charged Life with Brendon Burchard"
	   },
	   r'':{
	      "stream":"http://chasejarvislive.libsyn.com/itunes",
	      "image":"",
	      "name":"The Chase Jarvis LIVE Show"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:120714189/sounds.rss",
	      "image":"",
	      "name":"The Chief and Shawn Show"
	   },
	   r'':{
	      "stream":"http://www.halleycomm.net/podcast/halleycomm_podcast.xml",
	      "image":"",
	      "name":"The Children's Corner"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ChristmasStockingPodcast",
	      "image":"",
	      "name":"The Christmas Stocking"
	   },
	   r'':{
	      "stream":"http://thechurchofwhatshappeningnow.libsyn.com/rss",
	      "image":"",
	      "name":"The Church of What's Happening Now: With Joey Coco Diaz"
	   },
	   r'':{
	      "stream":"http://cinnamonbear.org.s3.amazonaws.com/podcast.xml",
	      "image":"",
	      "name":"The Cinnamon Bear"
	   },
	   r'':{
	      "stream":"http://thecity.org/feeds/audio",
	      "image":"",
	      "name":"The City Church with Judah Smith (Audio)"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ClarkHowardPodcast",
	      "image":"",
	      "name":"The Clark Howard Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheCleansed",
	      "image":"",
	      "name":"The Cleansed: A Post-Apocalyptic Saga"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:35042463/sounds.rss",
	      "image":"",
	      "name":"The Co-optional Podcast"
	   },
	   r'':{
	      "stream":"https://simplecast.com/podcasts/98/rss",
	      "image":"",
	      "name":"The College Info Geek Podcast: Study Tips & Advice for Students"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheCombatJackShow",
	      "image":"",
	      "name":"The Combat Jack Show"
	   },
	   r'':{
	      "stream":"http://comedybutton.libsyn.com/rss",
	      "image":"",
	      "name":"The Comedy Button"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/rocketjump/commandzone",
	      "image":"",
	      "name":"The Command Zone"
	   },
	   r'':{
	      "stream":"http://rss.earwolf.com/the-cracked-podcast",
	      "image":"",
	      "name":"The Cracked Podcast"
	   },
	   r'':{
	      "stream":"http://www.afterbuzztv.com/aftershows/the-crown-afterbuzz-tv-aftershow/feed/",
	      "image":"",
	      "name":"The Crown After Show"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/csis-podcast",
	      "image":"",
	      "name":"The CSIS Podcast"
	   },
	   r'':{
	      "stream":"http://cultofpedagogy.libsyn.com/rss",
	      "image":"",
	      "name":"The Cult of Pedagogy Podcast"
	   },
	   r'':{
	      "stream":"http://thecultcast.libsyn.com/rss",
	      "image":"",
	      "name":"The CultCast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:179032792/sounds.rss",
	      "image":"",
	      "name":"The Cure"
	   },
	   r'':{
	      "stream":"http://thecyberwire.libsyn.com/rss",
	      "image":"",
	      "name":"The CyberWire - Your cyber security news connection."
	   },
	   r'':{
	      "stream":"http://dailyboost.motivationtomove.com/rss",
	      "image":"",
	      "name":"The Daily Boost: Best Daily Motivation | Life | Career | Goal Setting | Health | Law of Attraction | Network Marketing"
	   },
	   r'':{
	      "stream":"http://dailyfantasyfootballedge.libsyn.com/rss",
	      "image":"",
	      "name":"The Daily Fantasy Football Edge"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=9941853",
	      "image":"",
	      "name":"The Dan Le Batard Show with Stugotz"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=588",
	      "image":"",
	      "name":"The Dan Patrick Show on PodcastOne"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/podcastone/njuD",
	      "image":"",
	      "name":"The Dave Portnoy Show"
	   },
	   r'':{
	      "stream":"http://dcrainmaker.libsyn.com/rss",
	      "image":"",
	      "name":"The DC Rainmaker Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:243532459/sounds.rss",
	      "image":"",
	      "name":"The Deep Vault"
	   },
	   r'':{
	      "stream":"http://dicetower.libsyn.com/rss",
	      "image":"",
	      "name":"The Dice Tower"
	   },
	   r'':{
	      "stream":"http://thedirtbag.libsyn.com/rss",
	      "image":"",
	      "name":"The Dirtbag Diaries"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/tdicasts",
	      "image":"",
	      "name":"The Disciplined Investor"
	   },
	   r'':{
	      "stream":"http://sethdahl.libsyn.com/rss",
	      "image":"",
	      "name":"The Disconnected Dad"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:102930714/sounds.rss",
	      "image":"",
	      "name":"The Division Podcast"
	   },
	   r'':{
	      "stream":"http://www.bbc.co.uk/programmes/p02nq0lx/episodes/downloads.rss",
	      "image":"",
	      "name":"The Documentary"
	   },
	   r'':{
	      "stream":"http://www.quickanddirtytips.com/xml/dogtrainer.xml",
	      "image":"",
	      "name":"The Dog Trainer's Quick and Dirty Tips for Teaching and Caring for Your Pet"
	   },
	   r'':{
	      "stream":"http://stanhope.libsyn.com/rss",
	      "image":"",
	      "name":"The Doug Stanhope Podcast"
	   },
	   r'':{
	      "stream":"http://www.spreaker.com/user/6543245/episodes/feed",
	      "image":"",
	      "name":"The Down & Dirty Radio Show"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheDrDrewPodcast",
	      "image":"",
	      "name":"The Dr. Drew Podcast"
	   },
	   r'':{
	      "stream":"http://www.drlaura.com/podcast",
	      "image":"",
	      "name":"The Dr. Laura Program Highlights"
	   },
	   r'':{
	      "stream":"http://www.spreaker.com/show/2005313/episodes/feed",
	      "image":"",
	      "name":"The Dumbbells"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:197878231/sounds.rss",
	      "image":"",
	      "name":"The Dusty Life Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:214104572/sounds.rss",
	      "image":"",
	      "name":"The Easy Allies Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheEddieTrunkPodcast",
	      "image":"",
	      "name":"The Eddie Trunk Podcast"
	   },
	   r'':{
	      "stream":"https://feeds.ellentv.com/podcast/video",
	      "image":"",
	      "name":"The Ellen Show Podcast (video)"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:13178752/sounds.rss",
	      "image":"",
	      "name":"The Empire Film Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/theenergygang",
	      "image":"",
	      "name":"The Energy Gang"
	   },
	   r'':{
	      "stream":"http://theenergyhealingpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Energy Healing Podcast || Happiness | Life | Inspiration | Success| Health | Motivation"
	   },
	   r'':{
	      "stream":"http://www.bbc.co.uk/programmes/p02pc9zn/episodes/downloads.rss",
	      "image":"",
	      "name":"The English We Speak"
	   },
	   r'':{
	      "stream":"http://enormocast.com/?feed=podcast",
	      "image":"",
	      "name":"The Enormocast: a climbing podcast"
	   },
	   r'':{
	      "stream":"http://theensemblist.podbean.com/feed/",
	      "image":"",
	      "name":"The Ensemblist"
	   },
	   r'':{
	      "stream":"http://entreleadershippodcast.ramsey.libsynpro.com/rss",
	      "image":"",
	      "name":"The EntreLeadership Podcast"
	   },
	   r'':{
	      "stream":"https://rss.art19.com/the-fall-of-rome-podcast",
	      "image":"",
	      "name":"The Fall of Rome Podcast"
	   },
	   r'':{
	      "stream":"http://thefantasyfootballers.libsyn.com/fantasyfootball",
	      "image":"",
	      "name":"The Fantasy Footballers - Fantasy Football Podcast"
	   },
	   r'':{
	      "stream":"http://fatburningman.com/feed/podcast/",
	      "image":"",
	      "name":"The Fat-Burning Man Show by Abel James. Paleo Nutrition, Ancestral Health & Primal Fitness"
	   },
	   r'':{
	      "stream":"http://thefighterandthekid.tfatk.libsynpro.com/rss",
	      "image":"",
	      "name":"The Fighter & The Kid"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheFilmVault",
	      "image":"",
	      "name":"The Film Vault"
	   },
	   r'':{
	      "stream":"http://www.thefirst40miles.com/feed/",
	      "image":"",
	      "name":"The First 40 Miles: Hiking and Backpacking Podcast"
	   },
	   r'':{
	      "stream":"http://theflashpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Flash Podcast"
	   },
	   r'':{
	      "stream":"http://theflophouse.libsyn.com/rss",
	      "image":"",
	      "name":"The Flop House"
	   },
	   r'':{
	      "stream":"http://theforwardpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Forward"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:167300167/sounds.rss",
	      "image":"",
	      "name":"The Friend Zone"
	   },
	   r'':{
	      "stream":"http://wvpublic.org/podcasts/29182/rss.xml",
	      "image":"",
	      "name":"The Front Porch"
	   },
	   r'':{
	      "stream":"https://www.wired.com/feed/podcast/gadget-lab",
	      "image":"",
	      "name":"The Gadget Lab Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/gameinformershow",
	      "image":"",
	      "name":"The Game Informer Show"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/GarbageTimePodcast",
	      "image":"",
	      "name":"The Garbage Time Podcast with Katie Nolan"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/garynevillepodcast",
	      "image":"",
	      "name":"The Gary Neville Podcast - Sky Sports"
	   },
	   r'':{
	      "stream":"http://thegenerationwhypodcast.com/feed/category/podcast",
	      "image":"",
	      "name":"The Generation Why Podcast"
	   },
	   r'':{
	      "stream":"http://www.giantbomb.com/podcast-xml/beastcast/",
	      "image":"",
	      "name":"The Giant Beastcast"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/thegirlswholived",
	      "image":"",
	      "name":"The Girls Who Lived"
	   },
	   r'':{
	      "stream":"http://goaldiggerpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Goal Digger Podcast"
	   },
	   r'':{
	      "stream":"http://gooddadproject.libsyn.com/rss",
	      "image":"",
	      "name":"The Good Dad Project"
	   },
	   r'':{
	      "stream":"https://www.thegospelcoalition.org/media/The_Gospel_Coalition",
	      "image":"",
	      "name":"The Gospel Coalition (TGC)"
	   },
	   r'':{
	      "stream":"https://www.theguardian.com/science/series/science/podcast.xml",
	      "image":"",
	      "name":"The Guardian's Science Weekly"
	   },
	   r'':{
	      "stream":"http://hppodcraft.com/feed/podcast/",
	      "image":"",
	      "name":"The H.P. Lovecraft Literary Podcast"
	   },
	   r'':{
	      "stream":"http://jamieivey.libsyn.com/rss",
	      "image":"",
	      "name":"The Happy Hour with Jamie Ivey"
	   },
	   r'':{
	      "stream":"https://my.wellnessmama.com/podcast/feed/",
	      "image":"",
	      "name":"The Healthy Moms Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.theheartradio.org/TheHeartRadio",
	      "image":"",
	      "name":"The Heart"
	   },
	   r'':{
	      "stream":"http://foxsportsradio.iheart.com/podcast/itunes/The_Herd_Hours_itunes.xml",
	      "image":"",
	      "name":"The Herd with Colin Cowherd"
	   },
	   r'':{
	      "stream":"http://www.blogtalkradio.com/the-hermetic-hour/podcast",
	      "image":"",
	      "name":"The Hermetic Hour"
	   },
	   r'':{
	      "stream":"https://feeds.publicradio.org/public_feeds/the-hilarious-world-of-depression/itunes/rss",
	      "image":"",
	      "name":"The Hilarious World of Depression"
	   },
	   r'':{
	      "stream":"http://hineswardshow.com/feed/podcast/",
	      "image":"",
	      "name":"The Hines Ward Show"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheHistoryChicks",
	      "image":"",
	      "name":"The History Chicks"
	   },
	   r'':{
	      "stream":"https://youngwifesguide.com/feed/podcast/",
	      "image":"",
	      "name":"The Homemaking Foundations Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/idealistpodcasts",
	      "image":"",
	      "name":"The Idealist.org Podcasts"
	   },
	   r'':{
	      "stream":"http://theindoorkids.libsyn.com/rss",
	      "image":"",
	      "name":"The Indoor Kids with Kumail Nanjiani and Emily V. Gordon"
	   },
	   r'':{
	      "stream":"http://www.bbc.co.uk/programmes/b00snr0w/episodes/downloads.rss",
	      "image":"",
	      "name":"The Infinite Monkey Cage"
	   },
	   r'':{
	      "stream":"http://feeds.frogpants.com/theinstance_feed.xml",
	      "image":"",
	      "name":"The Instance: The Podcast for Lovers of Blizzard Games"
	   },
	   r'':{
	      "stream":"http://iotpodcast.com/feed/podcast/",
	      "image":"",
	      "name":"The Internet of Things podcast"
	   },
	   r'':{
	      "stream":"http://jackbenny.libsyn.com/rss",
	      "image":"",
	      "name":"The Jack Benny Show"
	   },
	   r'':{
	      "stream":"http://altucher.stansberry.libsynpro.com/rss",
	      "image":"",
	      "name":"The James Altucher Show"
	   },
	   r'':{
	      "stream":"http://thejealouscurator.libsyn.com/rss",
	      "image":"",
	      "name":"The Jealous Curator : ART FOR YOUR EAR"
	   },
	   r'':{
	      "stream":"http://rss.art19.com/jillian-michaels",
	      "image":"",
	      "name":"The Jillian Michaels Show"
	   },
	   r'':{
	      "stream":"http://thenosugarcoatingpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Keto Diet Podcast"
	   },
	   r'':{
	      "stream":"https://www.ketovangelist.com/category/podcast/feed/",
	      "image":"",
	      "name":"The Ketovangelist Podcast"
	   },
	   r'':{
	      "stream":"http://www.themusclecarplace.com/category/kibbe-and-finnegan/feed",
	      "image":"",
	      "name":"The Kibbe and Finnegan Show"
	   },
	   r'':{
	      "stream":"http://feeds.koreasociety.org/tkspodcasts",
	      "image":"",
	      "name":"The Korea Society"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheLeviathanChroniclesPodcasts",
	      "image":"",
	      "name":"The Leviathan Chronicles"
	   },
	   r'':{
	      "stream":"http://thelifecoachschool.libsyn.com/rss",
	      "image":"",
	      "name":"The Life Coach School Podcast with Brooke Castillo"
	   },
	   r'':{
	      "stream":"http://lifetimecashflowpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Lifetime Cash Flow Through Real Estate Investing Podcast"
	   },
	   r'':{
	      "stream":"http://theliturgists.podbean.com/feed/",
	      "image":"",
	      "name":"The Liturgists Podcast"
	   },
	   r'':{
	      "stream":"http://d2grjfi36hr26b.cloudfront.net/podcast.xml",
	      "image":"",
	      "name":"The Lively Show"
	   },
	   r'':{
	      "stream":"http://llvlcshow.libsyn.com/rss",
	      "image":"",
	      "name":"The Livin' La Vida Low-Carb Show With Jimmy Moore"
	   },
	   r'':{
	      "stream":"http://rss.earwolf.com/the-longest-shortest-time",
	      "image":"",
	      "name":"The Longest Shortest Time"
	   },
	   r'':{
	      "stream":"http://essentialcomm.libsyn.com/rss",
	      "image":"",
	      "name":"The Look & Sound of Leadership"
	   },
	   r'':{
	      "stream":"http://thelovebomb.libsyn.com/rss",
	      "image":"",
	      "name":"The Love Bomb with Nico Tortorella"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/feeds/rss/podcast.xml?id=10528553",
	      "image":"",
	      "name":"The Lowe Post"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/MajorityReport",
	      "image":"",
	      "name":"The Majority Report with Sam Seder"
	   },
	   r'':{
	      "stream":"http://z1077fm.com/benvaughn.xml",
	      "image":"",
	      "name":"The Many Moods of Ben Vaughn hosted by Ben Vaughn"
	   },
	   r'':{
	      "stream":"http://www.onlyyouforever.com/feed/podcast/",
	      "image":"",
	      "name":"The Marriage Podcast for Smart People | from OnlyYouForever | Because Marriage Should Be Forever"
	   },
	   r'':{
	      "stream":"https://districtpodcast.s3.amazonaws.com/feed.xml",
	      "image":"",
	      "name":"The Martin Garrix Show"
	   },
	   r'':{
	      "stream":"http://www.quickanddirtytips.com/xml/mathdude.xml",
	      "image":"",
	      "name":"The Math Dude Quick and Dirty Tips to Make Math Easier"
	   },
	   r'':{
	      "stream":"http://themeditationpodcast.com/tmp.xml",
	      "image":"",
	      "name":"The Meditation Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/thememorypalace",
	      "image":"",
	      "name":"the memory palace"
	   },
	   r'':{
	      "stream":"http://mfceoproject.libsyn.com/rss2",
	      "image":"",
	      "name":"The MFCEO Project"
	   },
	   r'':{
	      "stream":"http://www.quickanddirtytips.com/mommy.xml",
	      "image":"",
	      "name":"The Mighty Mommy's Quick and Dirty Tips for Practical Parenting"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=863",
	      "image":"",
	      "name":"The Milo Yiannopoulos Show"
	   },
	   r'':{
	      "stream":"http://theminimalists.libsyn.com/rss",
	      "image":"",
	      "name":"The Minimalists Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/aol/fanhouse/mmahour/audio",
	      "image":"",
	      "name":"The MMA Hour with Ariel Helwani"
	   },
	   r'':{
	      "stream":"http://themodelhealthshow.libsyn.com/rss",
	      "image":"",
	      "name":"The Model Health Show: Nutrition | Exercise | Fitness | Health | Lifestyle"
	   },
	   r'':{
	      "stream":"http://lifelistened.com/feed/the-mom-hour/",
	      "image":"",
	      "name":"The Mom Hour with Meagan Francis and Sarah Powers"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/the-moment",
	      "image":"",
	      "name":"The Moment with Brian Koppelman"
	   },
	   r'':{
	      "stream":"http://feeds.getmortified.com/MortifiedPod",
	      "image":"",
	      "name":"The Mortified Podcast"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/naked_scientists_podcast",
	      "image":"",
	      "name":"The Naked Scientists Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheNationalArchivesPodcastSeries",
	      "image":"",
	      "name":"The National Archives Podcast Series"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/tnss_video_hd.xml",
	      "image":"",
	      "name":"The New Screen Savers (Video-HD)"
	   },
	   r'':{
	      "stream":"http://newyorkpubliclibrary.libsyn.com/rss",
	      "image":"",
	      "name":"The New York Public Library Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.wnyc.org/tnyfiction",
	      "image":"",
	      "name":"The New Yorker: Fiction"
	   },
	   r'':{
	      "stream":"http://feeds.wnyc.org/tnyauthorsvoice",
	      "image":"",
	      "name":"The New Yorker: The Writer's Voice - New Fiction from The New Yorker"
	   },
	   r'':{
	      "stream":"http://feeds.megaphone.fm/FLM2375047009",
	      "image":"",
	      "name":"The Next Picture Show"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:189059907/sounds.rss",
	      "image":"",
	      "name":"The No Film School Podcast"
	   },
	   r'':{
	      "stream":"http://rss.art19.com/nosleep",
	      "image":"",
	      "name":"The NoSleep Podcast"
	   },
	   r'':{
	      "stream":"http://www.quickanddirtytips.com/xml/nutrition.xml",
	      "image":"",
	      "name":"The Nutrition Diva's Quick and Dirty Tips for Eating Well and Feeling Fabulous"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/focus-on-the-family/adventures-in-odyssey-podcast",
	      "image":"",
	      "name":"The Official Adventures in Odyssey Podcast"
	   },
	   r'':{
	      "stream":"http://redchippoker.libsyn.com/rss",
	      "image":"",
	      "name":"The Official Red Chip Poker Podcast"
	   },
	   r'':{
	      "stream":"http://oneyoufeed.libsyn.com/rss",
	      "image":"",
	      "name":"The One You Feed"
	   },
	   r'':{
	      "stream":"http://orbitinghumancircus.libsyn.com/rss",
	      "image":"",
	      "name":"The Orbiting Human Circus (of the Air)"
	   },
	   r'':{
	      "stream":"http://theoverwhelmedbrain.libsyn.com/rss",
	      "image":"",
	      "name":"The Overwhelmed Brain | Personal Growth | Relationship Advice | Critical Thinking | Emotional Intelligence | Healing"
	   },
	   r'':{
	      "stream":"http://coconutsandkettlebells.com/feed/podcast/",
	      "image":"",
	      "name":"The Paleo Women Podcast: Health | Nutrition | Fitness | Hormones"
	   },
	   r'':{
	      "stream":"http://feeds2.feedburner.com/ThePartiallyExaminedLife",
	      "image":"",
	      "name":"The Partially Examined Life Philosophy Podcast"
	   },
	   r'':{
	      "stream":"http://theknow.roosterteeth.com/show/the-patch/feed/mp3",
	      "image":"",
	      "name":"The Patch"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ThePeoplesPharmacy",
	      "image":"",
	      "name":"The People's Pharmacy"
	   },
	   r'':{
	      "stream":"http://theperfectwife.libsyn.com/rss",
	      "image":"",
	      "name":"The Perfect Wife"
	   },
	   r'':{
	      "stream":"http://www.schiffradio.com/feed/podcast/",
	      "image":"",
	      "name":"The Peter Schiff Show Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ThePodfathers",
	      "image":"",
	      "name":"The Podfathers"
	   },
	   r'':{
	      "stream":"http://thepolicepodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Police Podcast"
	   },
	   r'':{
	      "stream":"http://politicsguys.com/feed/podcast/",
	      "image":"",
	      "name":"The Politics Guys"
	   },
	   r'':{
	      "stream":"http://thepopcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Popcast With Knox and Jamie"
	   },
	   r'':{
	      "stream":"http://positivehead.libsyn.com/rss",
	      "image":"",
	      "name":"The Positive Head Podcast | Weekly Interviews with Today's Consciousness Change-makers | A Daily Dose of Soul Food For Thought!"
	   },
	   r'':{
	      "stream":"http://www.oneplace.com/ministries/the-potters-touch/subscribe/podcast.xml",
	      "image":"",
	      "name":"The Potter's Touch"
	   },
	   r'':{
	      "stream":"http://www.lightsource.com/ministry/the-potters-house/subscribe/podcast.xml",
	      "image":"",
	      "name":"The Potter's Touch on LightSource.com"
	   },
	   r'':{
	      "stream":"http://medicalschoolhq.libsyn.com/rss",
	      "image":"",
	      "name":"The Premed Years | Medical School Headquarters | MCAT | AMCAS | Interviews"
	   },
	   r'':{
	      "stream":"http://psychologypodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Psychology Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/newsworks/ThePulse",
	      "image":"",
	      "name":"The Pulse"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheQaWithJeffGoldsmith",
	      "image":"",
	      "name":"The Q&A with Jeff Goldsmith"
	   },
	   r'':{
	      "stream":"http://quoteofthedayshow.libsyn.com/rss",
	      "image":"",
	      "name":"The Quote of the Day Show"
	   },
	   r'':{
	      "stream":"",
	      "image":"",
	      "name":"The Radio Adventures of Dr. Floyd Official Podcast,"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheRadioAdventuresOfEleanorAmplified",
	      "image":"",
	      "name":"The Radio Adventures of Eleanor Amplified"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/eL1krEll7iB4",
	      "image":"",
	      "name":"The Read"
	   },
	   r'':{
	      "stream":"https://realestateguysradio.com/wp-content/themes/real_estate_guys_10/feed/index2.php",
	      "image":"",
	      "name":"The Real Estate Guys Radio Show - Real Estate Investing Education for Effective Action"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4769828.rss",
	      "image":"",
	      "name":"The Ric Flair Show"
	   },
	   r'':{
	      "stream":"http://www.richroll.com/feed/podcast/",
	      "image":"",
	      "name":"The Rich Roll Podcast"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=12563086",
	      "image":"",
	      "name":"The Right Time with Bomani Jones"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ringermlbshow",
	      "image":"",
	      "name":"The Ringer MLB Show"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/RingerNBAShow",
	      "image":"",
	      "name":"The Ringer NBA Show"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ringernflshow",
	      "image":"",
	      "name":"The Ringer NFL Show"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:254359729/sounds.rss",
	      "image":"",
	      "name":"The Risk Takers"
	   },
	   r'':{
	      "stream":"http://Theroadbacktoyou.podbean.com/feed/",
	      "image":"",
	      "name":"The Road Back to You: Looking at life through the lens of the Enneagram"
	   },
	   r'':{
	      "stream":"http://robbell.podbean.com/feed/",
	      "image":"",
	      "name":"The RobCast"
	   },
	   r'':{
	      "stream":"http://robinsharma.libsyn.com/rss",
	      "image":"",
	      "name":"The Robin Sharma Mastery Sessions"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=619",
	      "image":"",
	      "name":"The Ross Report"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheRoundTableOfGentlemen",
	      "image":"",
	      "name":"The Roundtable of Gentlemen"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheRunnersWorldShow",
	      "image":"",
	      "name":"The Runner's World Show"
	   },
	   r'':{
	      "stream":"http://maddmike.libsyn.com/rss",
	      "image":"",
	      "name":"The Scarecast - Scary Stories & Creepypasta"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/4829847.rss",
	      "image":"",
	      "name":"The Scathing Atheist"
	   },
	   r'':{
	      "stream":"http://lewishowes.com/feed/podcast/",
	      "image":"",
	      "name":"The School of Greatness with Lewis Howes"
	   },
	   r'':{
	      "stream":"http://redorbit.podbean.com/feed/",
	      "image":"",
	      "name":"The Science of Success"
	   },
	   r'':{
	      "stream":"http://thesdrshow.libsyn.com/rss",
	      "image":"",
	      "name":"The SDR Show (Sex, Drugs, & Rock-n-Roll Show) w/ Big Jay Oakerson & Ralph Sutton"
	   },
	   r'':{
	      "stream":"http://secrettosuccess.libsyn.com/rss",
	      "image":"",
	      "name":"The Secret To Success with CJ & Eric Thomas | Inspiration | Personal Development | Success"
	   },
	   r'':{
	      "stream":"http://theserialkillerpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Serial Killer Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/seth-davis",
	      "image":"",
	      "name":"The Seth Davis Podcast"
	   },
	   r'':{
	      "stream":"http://selfishmomacademy.libsyn.com/rss",
	      "image":"",
	      "name":"The Shameless Mom Academy | Motherhood | Parent | Lifestyle | Inspiration | Motivation | Education | Mother | Full Life | Life"
	   },
	   r'':{
	      "stream":"http://www.sidehustlenation.com/feed/podcast/",
	      "image":"",
	      "name":"The Side Hustle Show: Business Ideas for Part-Time Entrepreneurs"
	   },
	   r'':{
	      "stream":"http://simplyscarypodcast.com/feed/podcast",
	      "image":"",
	      "name":"The Simply Scary Podcast"
	   },
	   r'':{
	      "stream":"http://www.theskepticsguide.org/feed/sgu",
	      "image":"",
	      "name":"The Skeptics' Guide to the Universe"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/spipodcast",
	      "image":"",
	      "name":"The Smart Passive Income Podcast: Online Business | Blogging | Passive Income | Pat Flynn"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheSmartest",
	      "image":"",
	      "name":"The Smartest Man in the World"
	   },
	   r'':{
	      "stream":"http://thesmithplays.podbean.com/feed/",
	      "image":"",
	      "name":"The SmithSquad Podcast"
	   },
	   r'':{
	      "stream":"http://shoutengine.com/TheSmokingTire.xml",
	      "image":"",
	      "name":"The Smoking Tire"
	   },
	   r'':{
	      "stream":"http://www.socialworkpodcast.com/socialworkpodcast.xml",
	      "image":"",
	      "name":"The Social Work Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/solidverbal",
	      "image":"",
	      "name":"The Solid Verbal: Living College Football"
	   },
	   r'':{
	      "stream":"https://www.splendidtable.org/feeds/podcast/itunes",
	      "image":"",
	      "name":"The Splendid Table"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/sporkful",
	      "image":"",
	      "name":"The Sporkful"
	   },
	   r'':{
	      "stream":"http://sportsmandragracingpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Sportsman Drag Racing Podcast w/ Luke & Jed"
	   },
	   r'':{
	      "stream":"http://feeds.adknit.com/app-search/nba/the-starters/all/720/200/",
	      "image":"",
	      "name":"The Starters"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=542",
	      "image":"",
	      "name":"The Steve Austin Show"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=436",
	      "image":"",
	      "name":"The Steve Austin Show - Unleashed!"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TheStoryCollider",
	      "image":"",
	      "name":"The Story Collider"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/thestoryhome",
	      "image":"",
	      "name":"The Story Home Children's Audio Stories"
	   },
	   r'':{
	      "stream":"http://daringfireball.net/thetalkshow/rss",
	      "image":"",
	      "name":"The Talk Show With John Gruber"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/kfi.xml",
	      "image":"",
	      "name":"The Tech Guy (MP3)"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/kornheiser",
	      "image":"",
	      "name":"The Tony Kornheiser Show"
	   },
	   r'':{
	      "stream":"http://podcasts.teach12.com/thetorch.xml",
	      "image":"",
	      "name":"The Torch: The Great Courses Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:259823538/sounds.rss",
	      "image":"",
	      "name":"The TSN Hockey BobCast"
	   },
	   r'':{
	      "stream":"http://thetwentyminutevc.libsyn.com/rss",
	      "image":"",
	      "name":"The Twenty Minute VC: Venture Capital | Startup Funding | The Pitch"
	   },
	   r'':{
	      "stream":"http://ultimatehealthpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Ultimate Health Podcast: Wellness, Nutrition, Fitness, & Exercise"
	   },
	   r'':{
	      "stream":"http://sealfit.libsyn.com/rss",
	      "image":"",
	      "name":"The Unbeatable Mind Podcast with Mark Divine"
	   },
	   r'':{
	      "stream":"http://pruittprep.com/feed/podcast/",
	      "image":"",
	      "name":"The Unexplainable Disappearance of Mars Patel"
	   },
	   r'':{
	      "stream":"http://urbanfarm.libsyn.com/rss",
	      "image":"",
	      "name":"The Urban Farm Podcast with Greg Peterson"
	   },
	   r'':{
	      "stream":"https://rss.art19.com/the-vanished-podcast",
	      "image":"",
	      "name":"The Vanished Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ThisIsMyNextPodcast",
	      "image":"",
	      "name":"The Vergecast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/Vertical-JJ",
	      "image":"",
	      "name":"The Vertical Podcast with JJ Redick"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/VerticalPodcast",
	      "image":"",
	      "name":"The Vertical Podcast with Woj"
	   },
	   r'':{
	      "stream":"http://feeds.thevillagechurch.net/culture-matters",
	      "image":"",
	      "name":"The Village Church - Culture Matters"
	   },
	   r'':{
	      "stream":"http://feeds.thevillagechurch.net/sermons",
	      "image":"",
	      "name":"The Village Church - Sermons"
	   },
	   r'':{
	      "stream":"http://rss-cmg.streamguys1.com/atlanta/atl750/the-eric-von-heassle.xml",
	      "image":"",
	      "name":"The Von Haessler Doctrine"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/VultureTV",
	      "image":"",
	      "name":"The Vulture TV Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/thewatchpod",
	      "image":"",
	      "name":"The Watch"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:116406291/sounds.rss",
	      "image":"",
	      "name":"The Weebcast"
	   },
	   r'':{
	      "stream":"http://twihl.podbean.com/feed/",
	      "image":"",
	      "name":"The Week in Health Law"
	   },
	   r'':{
	      "stream":"http://weeklyplanetpod.libsyn.com/rss",
	      "image":"",
	      "name":"The Weekly Planet"
	   },
	   r'':{
	      "stream":"http://weeklysubstandard.weeklystandard.libsynpro.com/rss",
	      "image":"",
	      "name":"The Weekly Substandard | A nerdcast on movies and pop-culture"
	   },
	   r'':{
	      "stream":"http://westwingweekly.libsyn.com/feed",
	      "image":"",
	      "name":"The West Wing Weekly"
	   },
	   r'':{
	      "stream":"http://www.thewoodworkingpodcast.com/feed/",
	      "image":"",
	      "name":"The Woodworking Podcast"
	   },
	   r'':{
	      "stream":"http://wordonfire.libsyn.com/rss",
	      "image":"",
	      "name":"The Word on Fire Show"
	   },
	   r'':{
	      "stream":"http://feeds.americanpublicmedia.org/writersalmanac",
	      "image":"",
	      "name":"The Writer's Almanac with Garrison KeillorThe Writer's Almanac with Garrison Keillor"
	   },
	   r'':{
	      "stream":"http://nerdistwriters.libsyn.com/rss",
	      "image":"",
	      "name":"The Writers Panel"
	   },
	   r'':{
	      "stream":"http://zigziglar.libsyn.com/rss",
	      "image":"",
	      "name":"The Ziglar Show - Inspiring Your True Performance"
	   },
	   r'':{
	      "stream":"http://baltimoreannapolispsychotherapypodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Therapy Chat | Psychotherapy | Mindfulness | Trauma | Attachment | Worthiness | Self Care | Parenting"
	   },
	   r'':{
	      "stream":"http://www.blogtalkradio.com/thethinkingatheist/podcast",
	      "image":"",
	      "name":"TheThinkingAtheist"
	   },
	   r'':{
	      "stream":"http://www.bbc.co.uk/programmes/b006qy05/episodes/downloads.rss",
	      "image":"",
	      "name":"Thinking Allowed"
	   },
	   r'':{
	      "stream":"http://thinkingsidewayspodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Thinking Sideways Podcast"
	   },
	   r'':{
	      "stream":"http://www.afterbuzztv.com/aftershows/this-is-us-afterbuzz-tv-aftershow/feed/",
	      "image":"",
	      "name":"This Is Us AfterBuzz TV AfterShow"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TIYL",
	      "image":"",
	      "name":"This Is Your Life with Michael Hyatt"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/thismorningamericasfirstnews",
	      "image":"",
	      "name":"This Morning With Gordon Deal"
	   },
	   r'':{
	      "stream":"https://simplecast.com/podcasts/2095/rss",
	      "image":"",
	      "name":"This Week I Learned"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/twig.xml",
	      "image":"",
	      "name":"This Week in Google (MP3)"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/twil.xml",
	      "image":"",
	      "name":"This Week in Law (MP3)"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/twimlai",
	      "image":"",
	      "name":"This Week in Machine Learning & AI Podcast"
	   },
	   r'':{
	      "stream":"http://marvel.com/podcasts/10/this_week_in_marvel/rss",
	      "image":"",
	      "name":"This Week in Marvel"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/twit.xml",
	      "image":"",
	      "name":"This Week in Tech (MP3)"
	   },
	   r'':{
	      "stream":"http://thrillersotr.rnn.libsynpro.com/rss",
	      "image":"",
	      "name":"Thrillers Old Time Radio"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ThrillingAdventureHour",
	      "image":"",
	      "name":"Thrilling Adventure Hour"
	   },
	   r'':{
	      "stream":"http://throwingshade.libsyn.com/rss",
	      "image":"",
	      "name":"Throwing Shade"
	   },
	   r'':{
	      "stream":"http://blart.libsyn.com/rss",
	      "image":"",
	      "name":"Til Death Do Us Blart"
	   },
	   r'':{
	      "stream":"https://ginl-podcast.s3.amazonaws.com/0_Resources/Timothy_Keller_Podcasts.xml",
	      "image":"",
	      "name":"Timothy Keller Sermons Podcast by Gospel in Life"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510306",
	      "image":"",
	      "name":"Tiny Desk Concerts - Audio"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510292",
	      "image":"",
	      "name":"Tiny Desk Concerts - Video"
	   },
	   r'':{
	      "stream":"http://toddwhite.libsyn.com/toddwhite",
	      "image":"",
	      "name":"Todd White Podcast"
	   },
	   r'':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=960",
	      "image":"",
	      "name":"Too $hort's Boombox"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/Recode-TETA",
	      "image":"",
	      "name":"Too Embarrassed to Ask"
	   },
	   r'':{
	      "stream":"http://onnit.libsyn.com/rss",
	      "image":"",
	      "name":"Total Human Optimization"
	   },
	   r'':{
	      "stream":"http://totallymarried.libsyn.com/rss",
	      "image":"",
	      "name":"Totally Married"
	   },
	   r'':{
	      "stream":"http://www.toyruncast.com/feed/",
	      "image":"",
	      "name":"TOY RUN - THE STAR WARS ACTION FIGURE CAST"
	   },
	   r'':{
	      "stream":"http://wwno.org/podcasts/88432/rss.xml",
	      "image":"",
	      "name":"TriPod: New Orleans At 300"
	   },
	   r'':{
	      "stream":"http://tritonia.libsyn.com/rss",
	      "image":"",
	      "name":"Tritonia"
	   },
	   r'':{
	      "stream":"http://www.blogtalkradio.com/dan-zupansky1/podcast",
	      "image":"",
	      "name":"True Murder: The Most Shocking Killers in True Crime History and the Authors That Have Written About Them"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=12426375",
	      "image":"",
	      "name":"TrueHoop"
	   },
	   r'':{
	      "stream":"https://shauntfitness.com/feed/podcast/",
	      "image":"",
	      "name":"Trust and Believe with Shaun T"
	   },
	   r'':{
	      "stream":"http://feeds.sideshownetwork.tv/Truth&Iliza",
	      "image":"",
	      "name":"Truth & Iliza"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/TruthForLife",
	      "image":"",
	      "name":"Truth For Life Broadcasts"
	   },
	   r'':{
	      "stream":"https://rss.art19.com/tumble",
	      "image":"",
	      "name":"Tumble Science Podcast for Kids"
	   },
	   r'':{
	      "stream":"https://audioboom.com/channels/3081610.rss",
	      "image":"",
	      "name":"Turned Out A Punk"
	   },
	   r'':{
	      "stream":"http://20khz.libsyn.com/rss",
	      "image":"",
	      "name":"Twenty Thousand Hertz"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/USPresidentsPodcast",
	      "image":"",
	      "name":"U.S. Presidents Podcast"
	   },
	   r'':{
	      "stream":"https://api.oyez.org/podcasts/opinion-announcements/2014",
	      "image":"",
	      "name":"U.S. Supreme Court Opinion Announcements"
	   },
	   r'':{
	      "stream":"https://api.oyez.org/podcasts/oral-arguments/2015",
	      "image":"",
	      "name":"U.S. Supreme Court Oral Arguments"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ufc-unfiltered",
	      "image":"",
	      "name":"UFC Unfiltered with Jim Norton and Matt Serra"
	   },
	   r'':{
	      "stream":"http://ultimafinalfantasy.libsyn.com/rss",
	      "image":"",
	      "name":"Ultima Final Fantasy | The Ultimate Final Fantasy Podcast"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/homilies3",
	      "image":"",
	      "name":"UMD NEWMAN CATHOLIC CAMPUS MINISTRY"
	   },
	   r'':{
	      "stream":"http://unbelievable.podbean.com/feed/",
	      "image":"",
	      "name":"Unbelievable?"
	   },
	   r'':{
	      "stream":"http://www.underthehoodshow.com/rss/rss_1.xml",
	      "image":"",
	      "name":"Under The Hood Automotive Talk Show"
	   },
	   r'':{
	      "stream":"http://underthescales.libsyn.com/rss",
	      "image":"",
	      "name":"Under the Scales"
	   },
	   r'':{
	      "stream":"http://www.oneplace.com/ministries/understanding-the-times/subscribe/podcast.xml",
	      "image":"",
	      "name":"Understanding the Times on OnePlace.com"
	   },
	   r'':{
	      "stream":"http://rainmaker.fm/series/unemployable/feed/",
	      "image":"",
	      "name":"Unemployable with Brian Clark"
	   },
	   r'':{
	      "stream":"http://rss.acast.com/unexplained",
	      "image":"",
	      "name":"Unexplained"
	   },
	   r'':{
	      "stream":"http://wwno.org/podcasts/90348/rss.xml",
	      "image":"",
	      "name":"Unprisoned: Stories From The System"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:224506341/sounds.rss",
	      "image":"",
	      "name":"Unsolved Murders: True Crime Stories"
	   },
	   r'':{
	      "stream":"http://www.spreaker.com/show/2043646/episodes/feed",
	      "image":"",
	      "name":"UNspoiled! Harry Potter"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:261640883/sounds.rss",
	      "image":"",
	      "name":"UnStyled"
	   },
	   r'':{
	      "stream":"http://kcur.org/podcasts/20/rss.xml",
	      "image":"",
	      "name":"Up To Date"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:180380860/sounds.rss",
	      "image":"",
	      "name":"UpToDate Talk"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/chanmanvtv/ValueTown",
	      "image":"",
	      "name":"Value Town - A Hearthstone Podcast"
	   },
	   r'':{
	      "stream":"http://www.afterbuzztv.com/aftershows/vanderpump-rules-afterbuzz-tv-aftershow/feed/",
	      "image":"",
	      "name":"Vanderpump Rules AfterBuzz TV AfterShow"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:250702053/sounds.rss",
	      "image":"",
	      "name":"VeloNews Podcasts"
	   },
	   r'':{
	      "stream":"http://verypink.libsyn.com/rss",
	      "image":"",
	      "name":"VeryPink Knits"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ChairborneCommandos",
	      "image":"",
	      "name":"Veteran Podcast And Military News Talk Radio Including Special Operations And Military Technology - Chairborne Commandos"
	   },
	   r'':{
	      "stream":"https://www.chds.us/?viewpoint&rss",
	      "image":"",
	      "name":"Viewpoints in Homeland Defense and Security"
	   },
	   r'':{
	      "stream":"http://podcast.wandwmusic.nl/podcast.php",
	      "image":"",
	      "name":"W&W Mainstage Podcast"
	   },
	   r'':{
	      "stream":"https://www.fbi.gov/feeds/wanted-by-the-fbi-podcast/itunes.xml",
	      "image":"",
	      "name":"Wanted by the FBI podcast"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:235660424/sounds.rss",
	      "image":"",
	      "name":"Warm Regards"
	   },
	   r'':{
	      "stream":"http://feeds.sideshownetwork.tv/WatchWhatCrappens",
	      "image":"",
	      "name":"Watch What Crappens"
	   },
	   r'':{
	      "stream":"http://baldmove.com/feed/watching-dead/",
	      "image":"",
	      "name":"Watching Dead - Walking Dead Podcast"
	   },
	   r'':{
	      "stream":"http://baldmove.com/feed/westworld",
	      "image":"",
	      "name":"Watching Westworld"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/WatermarkRadioPorchChannel",
	      "image":"",
	      "name":"Watermark Audio: The Porch Channel"
	   },
	   r'':{
	      "stream":"http://vicegamingnew.vice-media.libsynpro.com/rss",
	      "image":"",
	      "name":"Waypoint Radio"
	   },
	   r'':{
	      "stream":"http://whmpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"We Hate Movies"
	   },
	   r'':{
	      "stream":"http://theinvestorspodcast.libsyn.com/rss",
	      "image":"",
	      "name":"We Study Billionaires - The Investors Podcast"
	   },
	   r'':{
	      "stream":"http://wellseeyouinhellpod.libsyn.com/rss",
	      "image":"",
	      "name":"We'll See You In Hell"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/itpc/wwwwaylandws/Wayland_Productions/Were_Alive_-_Podcast/rssxml",
	      "image":"",
	      "name":"We're Alive - A "      Zombie" Story of Survival"
	   },
	   r'':{
	      "stream":"http://rss.art19.com/were-alive-lockdown",
	      "image":"",
	      "name":"We're Alive: Lockdown"
	   },
	   r'':{
	      "stream":"http://knkx.org/podcasts/term/2766/rss.xml",
	      "image":"",
	      "name":"Weather With Cliff Mass"
	   },
	   r'':{
	      "stream":"http://kuow.org/podcasts/19654/rss.xml",
	      "image":"",
	      "name":"Week In Review"
	   },
	   r'':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=17492726",
	      "image":"",
	      "name":"Weekend Observations with Stu & Jr."
	   },
	   r'':{
	      "stream":"http://weeklyinfusion.libsyn.com/rss",
	      "image":"",
	      "name":"Weekly Infusion"
	   },
	   r'':{
	      "stream":"http://shatontv.libsyn.com/rss",
	      "image":"",
	      "name":"Westworld"
	   },
	   r'':{
	      "stream":"http://www.coffeeklatchcrew.com/feed/westworld/",
	      "image":"",
	      "name":"Westworld"
	   },
	   r'':{
	      "stream":"http://www.afterbuzztv.com/aftershows/westworld-afterbuzz-tv-aftershow/feed/",
	      "image":"",
	      "name":"Westworld AfterBuzz TV AfterShow"
	   },
	   r'':{
	      "stream":"http://www.blogtalkradio.com/westworld/podcast",
	      "image":"",
	      "name":"Westworld with Jay, Jack, and Mike"
	   },
	   r'':{
	      "stream":"http://postshowrecaps.com/feed/westworld/",
	      "image":"",
	      "name":"Westworld: Post Show Recap with Josh Wigler & Jo Garfein"
	   },
	   r'':{
	      "stream":"http://whatshouldireadnext.libsyn.com/rss",
	      "image":"",
	      "name":"What Should I Read Next?: Book Talk | Reading Recommendations | Literary Matchmaking"
	   },
	   r'':{
	      "stream":"https://www.whitehouse.gov/podcast/video/press-briefings/rss.xml",
	      "image":"",
	      "name":"White House Press Briefings"
	   },
	   r'':{
	      "stream":"https://www.whitehouse.gov/podcast/audio/press-briefings/rss.xml",
	      "image":"",
	      "name":"White House Press Briefings (Audio)"
	   },
	   r'':{
	      "stream":"https://www.whitehouse.gov/podcast/video/speeches/rss.xml",
	      "image":"",
	      "name":"White House Speeches"
	   },
	   r'':{
	      "stream":"https://www.whitehouse.gov/podcast/audio/speeches/rss.xml",
	      "image":"",
	      "name":"White House Speeches (Audio)"
	   },
	   r'':{
	      "stream":"https://wfmu.org/podcast/LK.xml",
	      "image":"",
	      "name":"Why Oh Why"
	   },
	   r'':{
	      "stream":"http://feeds.twit.tv/ww.xml",
	      "image":"",
	      "name":"Windows Weekly (MP3)"
	   },
	   r'':{
	      "stream":"http://withinthewires.libsyn.com/rss",
	      "image":"",
	      "name":"Within the Wires"
	   },
	   r'':{
	      "stream":"http://wnpr.org/podcasts",
	      "image":"",
	      "name":"WNPR"
	   },
	   r'':{
	      "stream":"http://wolf359radio.libsyn.com/rss",
	      "image":"",
	      "name":"Wolf 359"
	   },
	   r'':{
	      "stream":"http://marvel.com/podcasts/12/women_of_marvel_podcast/rss",
	      "image":"",
	      "name":"Women of Marvel Podcast"
	   },
	   r'':{
	      "stream":"http://www.woodtalkshow.com/episodes/feed/",
	      "image":"",
	      "name":"Wood Talk"
	   },
	   r'':{
	      "stream":"http://feeds.podtrac.com/0YNYgrtCGEXR",
	      "image":"",
	      "name":"Wooden Overcoats"
	   },
	   r'':{
	      "stream":"http://woolful.com/feed/podcast/",
	      "image":"",
	      "name":"Woolful"
	   },
	   r'':{
	      "stream":"http://workingonamasterplan.com/feed/podcast/",
	      "image":"",
	      "name":"Working On A Masterplan: Dating Up"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:81949595/sounds.rss",
	      "image":"",
	      "name":"World Bank Podcasts"
	   },
	   r'':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510008",
	      "image":"",
	      "name":"World Cafe Words and Music from WXPN"
	   },
	   r'':{
	      "stream":"http://www.omnycontent.com/d/playlist/6e2a797b-0cc4-4c0b-a44d-a51e0019bc3c/3a51dc1f-d696-44f5-8bce-a51e0019f127/9af689bf-e634-4070-a49d-a51e001acb75/podcast.rss",
	      "image":"",
	      "name":"Worst Idea Of All Time Podcast"
	   },
	   r'':{
	      "stream":"http://wrestlingsoup.com/ws/feed.xml",
	      "image":"",
	      "name":"WRESTLING SOUP"
	   },
	   r'':{
	      "stream":"http://www.writingexcuses.com/feed/podcast/",
	      "image":"",
	      "name":"Writing Excuses"
	   },
	   r'':{
	      "stream":"http://feeds.wsjonline.com/wsj/podcast_moneybeat",
	      "image":"",
	      "name":"WSJ MoneyBeat"
	   },
	   r'':{
	      "stream":"http://feeds.wsjonline.com/wsj/podcast_wall_street_journal_tech_news_briefing",
	      "image":"",
	      "name":"WSJ Tech News Briefing"
	   },
	   r'':{
	      "stream":"http://feeds.wsjonline.com/wsj/podcast_wall_street_journal_whats_news",
	      "image":"",
	      "name":"WSJ What's News"
	   },
	   r'':{
	      "stream":"http://feeds.wsjonline.com/wsj/podcast_your_money_matters",
	      "image":"",
	      "name":"WSJ Your Money Matters"
	   },
	   r'':{
	      "stream":"http://wtkgtspodcast.libsyn.com/rss",
	      "image":"",
	      "name":"WTKGTS"
	   },
	   r'':{
	      "stream":"http://www.afterbuzztv.com/aftershows/wwe-monday-night-raw-afterbuzz-tv-aftershow/feed/",
	      "image":"",
	      "name":"WWE Monday Night RAW AfterBuzz TV AfterShow"
	   },
	   r'':{
	      "stream":"http://www.afterbuzztv.com/aftershows/wwes-smackdown-afterbuzz-tv-aftershow/feed/",
	      "image":"",
	      "name":"WWE SmackDown AfterBuzz TV AfterShow"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/potterpod",
	      "image":"",
	      "name":"Yer A Wizard Harry: The Harry Potter Bookclub"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/yogamazing",
	      "image":"",
	      "name":"YOGAmazing"
	   },
	   r'':{
	      "stream":"https://www.nps.gov/yose/learn/photosmultimedia/upload/yosemitevideos.xml",
	      "image":"",
	      "name":"Yosemite Presents"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:16745745/sounds.rss",
	      "image":"",
	      "name":"You Are Not So Smart"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/YouMadeItWeird",
	      "image":"",
	      "name":"You Made It Weird with Pete Holmes"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/MustRememberThis",
	      "image":"",
	      "name":"You Must Remember This"
	   },
	   r'':{
	      "stream":"http://youneedabudget.libsyn.com/rss",
	      "image":"",
	      "name":"You Need A Budget (YNAB)"
	   },
	   r'':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:198710859/sounds.rss",
	      "image":"",
	      "name":"You Talking YouTube To Me"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/YoureWelcomeWithChaelSonnen",
	      "image":"",
	      "name":"You're Welcome! With Chael Sonnen"
	   },
	   r'':{
	      "stream":"http://younghouselove.libsyn.com/rss",
	      "image":"",
	      "name":"Young House Love Has A Podcast"
	   },
	   r'':{
	      "stream":"http://kalw.org/podcasts/2094/rss.xml",
	      "image":"",
	      "name":"Your Call"
	   },
	   r'':{
	      "stream":"http://greensmoothiegirl.com/feed/podcast/",
	      "image":"",
	      "name":"Your High Vibration Life"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/YourMomsHouseWithChristinaPazsitzkyAndTomSegura",
	      "image":"",
	      "name":"Your Mom's House with Christina Pazsitzky and Tom Segura"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/npm",
	      "image":"",
	      "name":"Your Move with Andy Stanley Podcast"
	   },
	   r'':{
	      "stream":"http://yourparentingmojo.com/feed/podcast",
	      "image":"",
	      "name":"Your Parenting Mojo - Respectful, research-based parenting ideas to help kids thrive"
	   },
	   r'':{
	      "stream":"http://otrans.3cdn.net/6bfaeaf9e7cab15b8c_z6omv24jz.xml",
	      "image":"",
	      "name":"Your Weekly Radio Address from the President-elect"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ZenParentingRadio",
	      "image":"",
	      "name":"Zen Parenting Radio"
	   },
	   r'':{
	      "stream":"http://feeds.feedburner.com/ZeroBlogThirty",
	      "image":"",
	      "name":"Zero Blog Thirty"
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

