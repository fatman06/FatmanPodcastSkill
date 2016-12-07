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
	   r'(?i)^(life)(.+|)(after)$':{
	      "stream":"http://feeds.megaphone.fm/themessage",
	      "image":"",
	      "name":"LifeAfter"
	   },
	   r'(?i)^(lore|loar)$':{
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
	   #TOP 100 END
	   r'(?i)(these).+(their|there).+(stor)|(law).+(order)':{
	      "stream":"https://rss.art19.com/these-are-their-stories-the-law-and-order-podcast",
	      "image":"",
	      "name":"...These Are Their Stories: The Law & Order Podcast"
	   },
	   r'(?i)(10|ten).+(perc).+(happ)|(dan).+(harris)':{
	      "stream":"http://feeds.feedburner.com/abcradio/10percenthappier",
	      "image":"",
	      "name":"10 Percent Happier with Dan Harris"
	   },
	   r'(?i)(1947)|(nine)(.|)(teen)(.|)(forty)(.|)(seven)|(meet).+(the).+(press)':{
	      "stream":"http://meetthepress1947.nbcnews.libsynpro.com/rss",
	      "image":"",
	      "name":"1947: The Meet the Press Podcast"
	   },
	   r'(?i)(2|two).+(doc).+(talk)':{
	      "stream":"http://2docstalk.libsyn.com/rss",
	      "image":"",
	      "name":"2 Docs Talk"
	   },
	   r'(?i)(3|three)(.+|)(low|lau).+(house|haus)':{
	      "stream":"http://dj3lau.podbean.com/feed/",
	      "image":"",
	      "name":"3LAU HAUS"
	   },
	   r'(?i)(40|forty).+(week).+(preg)':{
	      "stream":"http://40weeks.libsyn.com/rss",
	      "image":"",
	      "name":"40 Weeks Pregnancy Podcast"
	   },
	   r'(?i)(48|forty.(eight|ate)).+(hour)':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1222?format=MP3_128K",
	      "image":"",
	      "name":"48 Hours"
	   },
	   r'(?i)(5|five).(min.+)\s(market)':{
	      "stream":"https://www.buzzsprout.com/57707.rss",
	      "image":"",
	      "name":"5 Minute Marketing: Shortcuts to Growing Your Business Online, 5 Minutes at a Time"
	   },
	   r'(?i)(5|five).(min.+)(church).+(hist)':{
	      "stream":"http://feeds.5minutesinchurchhistory.com/5ChurchHistory",
	      "image":"",
	      "name":"5 Minutes in Church History - A Weekly Christian Podcast with Stephen Nichols"
	   },
	   r'(?i)(6|six).(min.+)(eng)':{
	      "stream":"http://www.bbc.co.uk/programmes/p02pc9tn/episodes/downloads.rss",
	      "image":"",
	      "name":"6 Minute English"
	   },
	   r'(?i)(60|sixty).+(sec.+)(mind)':{
	      "stream":"https://www.scientificamerican.com/sciam/xml/iTunes.cfm?id=60-second-mind",
	      "image":"",
	      "name":"60-Second Mind"
	   },
	   r'(?i)(60|sixty).+(sec.+)(sci)':{
	      "stream":"https://www.scientificamerican.com/sciam/xml/iTunes.cfm?id=60-second-science",
	      "image":"",
	      "name":"60-Second Science"
	   },
	   r'(?i)(8|eight).+(4|four).(play)':{
	      "stream":"http://eightfour.libsyn.com/rss",
	      "image":"",
	      "name":"8-4 Play"
	   },
	   r'(?i)(cast).(of).(king)':{
	      "stream":"http://feeds.feedburner.com/castofkings",
	      "image":"",
	      "name":"A Cast of Kings - A Game of Thrones Podcast"
	   },
	   r'(?i)(Christmas).(carol)':{
	      "stream":"http://www.loyalbooks.com/book/a-christmas-carol-by-charles-dickens/feed",
	      "image":"",
	      "name":"A Christmas Carol by Charles Dickens"
	   },
	   r'(?i)((history).+(world).+(100|hundred).+(obj))|(his).+(of).+(the).+(wor)':{
	      "stream":"http://www.bbc.co.uk/programmes/b00nrtd2/episodes/downloads.rss",
	      "image":"",
	      "name":"A History of the World in 100 Objects"
	   },
	   r'(?i)(new).+(begin)':{
	      "stream":"http://feeds.harvest.org/ANB",
	      "image":"",
	      "name":"A New Beginning with Greg Laurie"
	   },
	   r'(?i)(prair).+(home).+(comp).+(high)':{
	      "stream":"https://feeds.publicradio.org/public_feeds/a-prairie-home-companion-highlights/itunes/rss",
	      "image":"",
	      "name":"A Prairie Home Companion Highlights"
	   },
	   r'(?i)(storm).+(of).+(spoil)':{
	      "stream":"http://feeds.feedburner.com/AStormOfSpoilers",
	      "image":"",
	      "name":"A STORM OF SPOILERS - A Game Of Thrones Podcast"
	   },
	   r'(?i)(sustain).+(mind)':{
	      "stream":"http://asustainablemind.libsyn.com/rss",
	      "image":"",
	      "name":"A Sustainable Mind"
	   },
	   r'(?i)(a|)(way).+(with).+(word)':{
	      "stream":"http://feeds.waywordradio.org/awwwpodcast",
	      "image":"",
	      "name":"A Way with Words"
	   },
	   r'(?i)(a16z)|(a).+(six(.|)teen|16).+(z)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:62921190/sounds.rss",
	      "image":"",
	      "name":"a16z"
	   },
	   r'(?i)(legal).+(talk).+(net)':{
	      "stream":"http://ltn.net.libsyn.com/aba",
	      "image":"",
	      "name":"ABA Journal Podcasts - Legal Talk Network"
	   },
	   r'(?i)(build).+(and).+(cit[iy])':{
	      "stream":"http://feeds.feedburner.com/AboutBuildingsAndCities",
	      "image":"",
	      "name":"About Buildings and Cities"
	   },
	   r'(?i)(above).+(and).+(beyond)':{
	      "stream":"http://static.aboveandbeyond.nu/grouptherapy/podcast.xml",
	      "image":"",
	      "name":"Above and Beyond: Group Therapy"
	   },
	   r'(?i)(accel).+(span)':{
	      "stream":"http://acceleratedspanishmasterofmemory.libsyn.com/rss",
	      "image":"",
	      "name":"Accelerated Spanish: Learn Spanish online the fastest and best way"
	   },
	   r'(?i)(ach).+(you).+(goal)':{
	      "stream":"http://halelrod.libsyn.com/rss",
	      "image":"",
	      "name":"Achieve Your Goals with Hal Elrod"
	   },
	   r'(?i)(Acquisitions).+(inc)':{
	      "stream":"https://www.penny-arcade.com/feed/podcasts-ai",
	      "image":"",
	      "name":"Acquisitions Incorporated: The Series"
	   },
	   r'(?i)(adam).+(ruin)':{
	      "stream":"http://maximumfun.org/feeds/are.xml",
	      "image":"",
	      "name":"Adam Ruins Everything"
	   },
	   r'(?i)(afford).+(anything)':{
	      "stream":"http://paulaandjaymoney.libsyn.com/rss",
	      "image":"",
	      "name":"Afford Anything"
	   },
	   r'(?i)(america).+(family).+(Phys)':{
	      "stream":"http://podcast.aafp.org/rss/",
	      "image":"",
	      "name":"AFP: American Family Physician Podcast"
	   },
	   r'(?i)(air)(.|)(line).+(pilot).+(guy)':{
	      "stream":"http://airlinepilotguy.com/podcast.xml",
	      "image":"",
	      "name":"Airline Pilot Guy - Aviation Podcast"
	   },
	   r'(?i)(air)(.|)(plane).+(geek)':{
	      "stream":"http://www.airplanegeeks.com/?feed=podcast",
	      "image":"",
	      "name":"Airplane Geeks Podcast"
	   },
	   r'(?i)(alan).+(watt)':{
	      "stream":"http://feeds.feedburner.com/awatts",
	      "image":"",
	      "name":"Alan Watts"
	   },
	   r'(?i)(alice).+(is).+(dead)':{
	      "stream":"http://aliceisntdead.libsyn.com/rss",
	      "image":"",
	      "name":"Alice Isn't Dead"
	   },
	   r'(?i)(all).+(ear)':{
	      "stream":"http://allearsenglish.libsyn.com/rss",
	      "image":"",
	      "name":"All Ears English Podcast"
	   },
	   r'(?i)(all).+(hand)':{
	      "stream":"http://www.navy.mil/podcast/NMCNradio/NMCNradio.xml",
	      "image":"",
	      "name":"All Hands Radio"
	   },
	   r'(?i)(all).+(in).+(the).+(mind)':{
	      "stream":"http://www.abc.net.au/radionational/feed/2888650/podcast.xml",
	      "image":"",
	      "name":"All In The Mind - ABC Radio National"
	   },
	   r'(?i)(all).+(song).+(consider)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510019&uid=n1qe4e85742c986fdb81d2d38ffa0d5d53",
	      "image":"",
	      "name":"All Songs Considered"
	   },
	   r'(?i)(all).+(the).+(book)':{
	      "stream":"http://allthebooks.libsyn.com/rss",
	      "image":"",
	      "name":"All the Books!"
	   },
	   r'(?i)(allegedly)|(theo von)|(matt).+(cole)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:157798900/sounds.rss",
	      "image":"",
	      "name":"Allegedly with Theo Von  & Matthew Cole Weiss"
	   },
	   r'(?i)(alt).+(lat)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510305",
	      "image":"",
	      "name":"Alt.Latino"
	   },
	   r'(?i)(alway).+(open)':{
	      "stream":"http://roosterteeth.com/show/always-open/feed/mp3",
	      "image":"",
	      "name":"Always Open"
	   },
	   r'(?i)(amaz).+(pod).+(ep)':{
	      "stream":"https://owltail.github.io/redrock/feed-bo-ts.xml",
	      "image":"",
	      "name":"Amazing Podcast Episodes: ~3x curated episodes per week"
	   },
	   r'(?i)(americ).+(test).+(kitch)':{
	      "stream":"http://feeds.feedburner.com/AmericasTestKitchenRadio",
	      "image":"",
	      "name":"America's Test Kitchen Radio"
	   },
	   r'(?i)(americ).+(conserv).+(Univ)':{
	      "stream":"http://acu.libsyn.com/rss",
	      "image":"",
	      "name":"American Conservative University Podcast"
	   },
	   r'(?i)(andy).+(stan).+(lead)':{
	      "stream":"http://feeds.feedburner.com/AndyStanleyLeadershipPodcast",
	      "image":"",
	      "name":"Andy Stanley Leadership Podcast"
	   },
	   r'(?i)(lip).+(serv)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:143463073/sounds.rss",
	      "image":"",
	      "name":"Angela Yee's Lip Service"
	   },
	   r'(?i)(annal|anal|annual).+(internal).+(med)':{
	      "stream":"http://feeds2.feedburner.com/AnnalsPodcast",
	      "image":"",
	      "name":"Annals of Internal Medicine Podcast"
	   },
	   r'(?i)(another).+(round)':{
	      "stream":"http://rss.acast.com/anotherround",
	      "image":"",
	      "name":"Another Round"
	   },
	   r'(?i)(art).+(of).+(charm)':{
	      "stream":"http://theartofcharmpodcast.theartofcharm.libsynpro.com/rss",
	      "image":"",
	      "name":"Art of Charm"
	   },
	   r'(?i)(aoki|a ok|a oh key ).+(house)':{
	      "stream":"http://feeds.feedburner.com/aokishouse",
	      "image":"",
	      "name":"AOKI'S HOUSE"
	   },
	   r'(?i)(new).+(from).+(lake)':{
	      "stream":"http://americanpublicmedia.publicradio.org/podcasts/xml/prairie_home_companion/news_from_lake_wobegon.xml",
	      "image":"",
	      "name":"APM: A Prairie Home Companion's News from Lake Wobegon"
	   },
	   r'(?i)((apple).+(byte|bite))|((extra).+(crunch))':{
	      "stream":"http://feed.cnet.com/feed/podcast/apple-byte-audio.xml",
	      "image":"",
	      "name":"Apple Byte: Extra Crunchy (MP3)"
	   },
	   r'(?i)(apple).+(talk)':{
	      "stream":"http://feeds.feedburner.com/imore-apple-talk",
	      "image":"",
	      "name":"Apple Talk"
	   },
	   r'(?i)(apple)(.+|)(inside)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:78650636/sounds.rss",
	      "image":"",
	      "name":"AppleInsider Podcast"
	   },
	   r'(?i)(appointment)(.+|)(tv|tele)':{
	      "stream":"http://feeds.feedburner.com/atvpodcast",
	      "image":"",
	      "name":"Appointment Television"
	   },
	   r'(?i)(arch)(.+|)((eighty)(.|)one|(81))':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:213324253/sounds.rss",
	      "image":"",
	      "name":"Archive 81"
	   },
	   r'(?i)(Skep.+Tank)|(Ari Shaffir)':{
	      "stream":"http://shaffir1.libsyn.com/rss",
	      "image":"",
	      "name":"Ari Shaffir's Skeptic Tank"
	   },
	   r'(?i)(armed).+(america)':{
	      "stream":"http://feeds.armedamericanradio.org/ArmedAmericanRadio",
	      "image":"",
	      "name":"Armed American Radio"
	   },
	   r'(?i)(around).+(horn)':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=2839445",
	      "image":"",
	      "name":"Around the Horn"
	   },
	   r'(?i)(around).+(NFL|N.F.L)':{
	      "stream":"http://aroundtheleague.libsyn.com/rss",
	      "image":"",
	      "name":"Around the NFL"
	   },
	   r'(?i)(art).+(wrestling)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:98602096/sounds.rss",
	      "image":"",
	      "name":"Art of Wrestling"
	   },
	   r'(?i)(ask).+(past).+(jo(|h)n)':{
	      "stream":"http://feed.desiringgod.org/ask-pastor-john.rss",
	      "image":"",
	      "name":"Ask Pastor John"
	   },
	   r'(?i)(ask).+(sci).+(mike)':{
	      "stream":"http://asksciencemike.podbean.com/feed/",
	      "image":"",
	      "name":"Ask Science Mike"
	   },
	   r'(?i)(aston).+(legend)':{
	      "stream":"https://audioboom.com/channels/4322549.rss",
	      "image":"",
	      "name":"Astonishing Legends"
	   },
	   r'(?i)(Astronomy.(161|one six one|one hundred sixty one))|Intro.+(to|two|too).+solar.+sys':{
	      "stream":"http://www.astronomy.ohio-state.edu/~pogge/Ast161/Audio/Podcast.xml",
	      "image":"",
	      "name":"Astronomy 161 - Introduction to Solar System Astronomy"
	   },
	   r'(?i)(Astronomy.cast)':{
	      "stream":"http://www.astronomycast.com/mp3.xml",
	      "image":"",
	      "name":"Astronomy Cast"
	   },
	   r'(?i)(at.+home.+sal)':{
	      "stream":"http://sallyclarkson.libsyn.com/rss",
	      "image":"",
	      "name":"At Home With Sally"
	   },
	   r'(?i)(aubrey|audrey).+marc':{
	      "stream":"http://warriorpoet.libsyn.com/rss",
	      "image":"",
	      "name":"Aubrey Marcus Podcast"
	   },
	   r'(?i)(audio).+(drama|dharma)':{
	      "stream":"http://feeds.feedburner.com/audiodharma",
	      "image":"",
	      "name":"Audio Dharma"
	   },
	   r'(?i)(auto)(.+|)(blog)':{
	      "stream":"http://www.autoblog.com/category/podcasts/rss.xml",
	      "image":"",
	      "name":"Autoblog Podcasts"
	   },
	   r'(?i)(award)(.+)(chatter)':{
	      "stream":"https://simplecast.com/podcasts/1396/rss",
	      "image":"",
	      "name":"Awards Chatter"
	   },
	   r'(?i)(aws|a.w.s)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:206714635/sounds.rss",
	      "image":"",
	      "name":"AWS Podcast"
	   },
	   r'(?i)(axe).+(blood).+(god)':{
	      "stream":"http://bloodgodpod.libsyn.com/rss",
	      "image":"",
	      "name":"Axe of the Blood God: USgamer's Official RPG Podcast"
	   },
	   r'(?i)(back).+(to|two).+(work)':{
	      "stream":"http://feeds.5by5.tv/b2w",
	      "image":"",
	      "name":"Back to Work"
	   },
	   r'(?i)(back)(.|)(seat).+rider':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=969",
	      "image":"",
	      "name":"Backseat Rider"
	   },
	   r'(?i)(balance).+(bite|byte)':{
	      "stream":"http://balancedbites.libsyn.com/rss",
	      "image":"",
	      "name":"Balanced Bites: Modern paleo living with Diane Sanfilippo & Liz Wolfe."
	   },
	   r'(?i)(bang).+(book).+(club)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:202224578/sounds.rss",
	      "image":"",
	      "name":"Banging Book Club"
	   },
	   r'(?i)(bar)(.|)(bell).+(shrug)':{
	      "stream":"http://barbellshrugged.libsyn.com/rss",
	      "image":"",
	      "name":"Barbell Shrugged - Talking Training w/ CrossFit Games Athletes, Strength Coaches & More"
	   },
	   r'(?i)(bar)(.|)(stool).+(run)':{
	      "stream":"http://feeds.feedburner.com/BarstoolRundown",
	      "image":"",
	      "name":"Barstool Rundown"
	   },
	   r'(?i)(base)(.|)(ball).+(tonight)':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=2386164",
	      "image":"",
	      "name":"Baseball Tonight with Buster Olney"
	   },
	   r'(?i)(bay).+(cur)':{
	      "stream":"https://ww2.kqed.org/news/category/bay-curious-podcast/feed/podcast",
	      "image":"",
	      "name":"Bay Curious"
	   },
	   r'(?i)(Inside).+(sci)':{
	      "stream":"http://www.bbc.co.uk/programmes/b036f7w2/episodes/downloads.rss",
	      "image":"",
	      "name":"BBC Inside Science"
	   },
	   r'(?i)(be).+(here).+(while)':{
	      "stream":"http://rachaelobriencomedy.libsyn.com/rss",
	      "image":"",
	      "name":"Be Here For A While"
	   },
	   r'(?i)(beautiful).+(stor)':{
	      "stream":"http://rss.earwolf.com/beautiful-anonymous",
	      "image":"",
	      "name":"Beautiful Stories From Anonymous People"
	   },
	   r'(?i)(Beauty).+(inside)':{
	      "stream":"http://beautyinsideout.libsyn.com/rss",
	      "image":"",
	      "name":"Beauty Inside Out with Kimberly Snyder"
	   },
	   r'(?i)(becom).+(super).+(male)':{
	      "stream":"http://feeds.feedburner.com/supermale",
	      "image":"",
	      "name":"Becoming a Super Male"
	   },
	   r'(?i)(becom).+(wise)':{
	      "stream":"http://www.onbeing.org/podcasts/becoming-wise.xml",
	      "image":"",
	      "name":"Becoming Wise"
	   },
	   r'(?i)(bed).+((stor)|(fairy)|(folk))':{
	      "stream":"http://talesfromthelilypad.podbean.com/feed/",
	      "image":"",
	      "name":"Bedtime Stories Fairytales and Folk Tales from the Lilypad for kids"
	   },
	   r'(?i)(beer)(.|)(smith)':{
	      "stream":"http://beersmith.com/content/feed/podcast/",
	      "image":"",
	      "name":"BeerSmith Home and Beer Brewing Podcast"
	   },
	   r'(?i)(behind)(.+)(bets)':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=5395837",
	      "image":"",
	      "name":"Behind the Bets"
	   },
	   r'(?i)(behind)(.+)(knife)':{
	      "stream":"http://behindtheknife.libsyn.com/rss",
	      "image":"",
	      "name":"Behind The Knife: The Surgery Podcast"
	   },
	   r'(?i)(ben)(.+)(green)(.|)(field)':{
	      "stream":"http://bengreenfieldfitness.libsyn.com/rss",
	      "image":"",
	      "name":"Ben Greenfield Fitness: Diet, Fat Loss and Performance"
	   },
	   r'(?i)(bert)(.|)(cast)':{
	      "stream":"http://bertcast.libsyn.com/rss",
	      "image":"",
	      "name":"Bertcast's podcast"
	   },
	   r'(?i)(best).+(old).+(time)':{
	      "stream":"http://bestofotr.rnn.beta.libsynpro.com/rss",
	      "image":"",
	      "name":"Best of Old Time Radio"
	   },
	   r'(?i)(beth).+(moore)':{
	      "stream":"http://bmoore86456.podomatic.com/rss2.xml",
	      "image":"",
	      "name":"Beth Moore's Podcast"
	   },
	   r'(?i)(beth).+(church)':{
	      "stream":"http://podcasts.ibethel.org/en/podcasts.rss",
	      "image":"",
	      "name":"Bethel Church Sermon of the Week"
	   },
	   r'(?i)beyond.+to.+do':{
	      "stream":"http://feeds.feedburner.com/beyondthetodolist",
	      "image":"",
	      "name":"Beyond the To Do List | Personal Productivity Perspectives"
	   },
	   r'(?i)beyond.+yach.+rock':{
	      "stream":"http://rss.art19.com/beyond-yacht-rock",
	      "image":"",
	      "name":"Beyond Yacht Rock"
	   },
	   r'(?i)big.+idea':{
	      "stream":"http://feeds.tvo.org/tvobigideas",
	      "image":"",
	      "name":"Big Ideas (Audio)"
	   },
	   r'(?i)big.+pic.+sci':{
	      "stream":"http://arewealone.libsyn.com/rss",
	      "image":"",
	      "name":"Big Picture Science"
	   },
	   r'(?i)bigger(.+|)pock':{
	      "stream":"http://feeds.feedburner.com/RealEstateNewsForReal",
	      "image":"",
	      "name":"Bigger Pockets Podcast"
	   },
	   r'(?i)biography':{
	      "stream":"http://www.latrobe.edu.au/marketing/assets/podcasts/rssfeeds/biography.xml",
	      "image":"",
	      "name":"Biography"
	   },
	   r'(?i)biology':{
	      "stream":"http://faculty.css.edu/gcizadlo/podcast/ap0809/anatphys0809.xml",
	      "image":"",
	      "name":"Biology 2110-2120: Anatomy and Physiology with Doc C"
	   },
	   r'(?i)bischoff.+wrestl':{
	      "stream":"https://audioboom.com/channels/4785680.rss",
	      "image":"",
	      "name":"Bischoff on Wrestling"
	   },
	   r'(?i)bitch.+(sesh|sess)':{
	      "stream":"http://rss.earwolf.com/bitch-sesh",
	      "image":"",
	      "name":"Bitch Sesh: A Real Housewives Breakdown"
	   },
	   r'(?i)(black).+(agend)':{
	      "stream":"http://blackagendaradio.podbean.com/feed/",
	      "image":"",
	      "name":"Black Agenda Radio"
	   },
	   r'(?i)(black).+(girl).+(in).+(om)':{
	      "stream":"https://simplecast.com/podcasts/1996/rss",
	      "image":"",
	      "name":"Black Girl In Om"
	   },
	   r'(?i)(Black).+(girl).+(talk)':{
	      "stream":"https://www.spreaker.com/show/1502744/episodes/feed",
	      "image":"",
	      "name":"Black Girls Talking"
	   },
	   r'(?i)(Black).+(list).+(table)':{
	      "stream":"http://feeds.feedburner.com/BlackListTableReads",
	      "image":"",
	      "name":"Black List Table Reads"
	   },
	   r'(?i)(Black).+(man).+(gun)':{
	      "stream":"http://urbanshooter.libsyn.com/rss",
	      "image":"",
	      "name":"Black Man With A Gun"
	   },
	   r'(?i)(bloom).+(bench)':{
	      "stream":"http://www.bloomberg.com/feeds/podcasts/benchmark.xml",
	      "image":"",
	      "name":"Bloomberg Benchmark"
	   },
	   r'(?i)(bloom).+(surv)':{
	      "stream":"http://www.bloomberg.com/feeds/podcasts/surveillance.xml",
	      "image":"",
	      "name":"Bloomberg Surveillance"
	   },
	   r'(?i)(blur).+(photo)':{
	      "stream":"http://feeds.feedburner.com/BlurryPhotos",
	      "image":"",
	      "name":"Blurry Photos"
	   },
	   r'(?i)(bod).+(boy)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:169774121/sounds.rss",
	      "image":"",
	      "name":"Bodega Boys"
	   },
	   r'(?i)((bon).(fire).(side)|bonfireside)':{
	      "stream":"http://feeds.duckfeed.tv/bsc",
	      "image":"",
	      "name":"Bonfireside Chat - A Dark Souls and Bloodborne Podcast"
	   },
	   r'(?i)(boxcar)':{
	      "stream":"http://boxcars711.podomatic.com/rss2.xml",
	      "image":"",
	      "name":"Boxcars711 Old Time Radio Pod"
	   },
	   r'(?i)(brain).+(matter)':{
	      "stream":"http://brainpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Brain Matters"
	   },
	   r'(?i)(brain).+(science).+(ginger)':{
	      "stream":"http://brainsciencepodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Brain Science with Ginger Campbell, MD: Neuroscience for Everyone"
	   },
	   r'(?i)(brains).+(on)':{
	      "stream":"https://feeds.publicradio.org/public_feeds/brains-on/itunes/rss",
	      "image":"",
	      "name":"Brains On! Science podcast for kids"
	   },
	   r'(?i)(brain)(.|)(stuff)':{
	      "stream":"http://www.howstuffworks.com/podcasts/brainstuff.rss",
	      "image":"",
	      "name":"BrainStuff"
	   },
	   r'(?i)(brand).+(boss)':{
	      "stream":"http://brandinglikeaboss.libsyn.com/rss",
	      "image":"",
	      "name":"Branding Like A Boss"
	   },
	   r'(?i)(bret).+(ellis)':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=592",
	      "image":"",
	      "name":"Bret Easton Ellis Podcast"
	   },
	   r'(?i)(brian).+(houst)':{
	      "stream":"http://feeds.feedburner.com/hillsong/podcast",
	      "image":"",
	      "name":"Brian Houston Podcast"
	   },
	   r'(?i)(broad)(.|)(way).+(back)':{
	      "stream":"http://broadwaybackstory.libsyn.com/rss",
	      "image":"",
	      "name":"Broadway Backstory"
	   },
	   r'(?i)(brook).+(event)':{
	      "stream":"http://brookingsevents.libsyn.com/rss",
	      "image":"",
	      "name":"Brookings Events"
	   },
	   r'(?i)(bruce).+(lee)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:210076721/sounds.rss",
	      "image":"",
	      "name":"Bruce Lee Podcast"
	   },
	   r'(?i)(buddhist).+(geek)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:36655593/sounds.rss",
	      "image":"",
	      "name":"Buddhist Geeks"
	   },
	   r'(?i)(buff).+(vamp)':{
	      "stream":"http://bufferingthevampireslayer.libsyn.com/rss",
	      "image":"",
	      "name":"Buffering the Vampire Slayer"
	   },
	   r'(?i)(build).+(your).+(tribe)':{
	      "stream":"http://chalenejohnson.libsyn.com/rss",
	      "image":"",
	      "name":"Build Your Tribe"
	   },
	   r'(?i)(build).+(story).+(brand)':{
	      "stream":"http://storybrand.libsyn.com/rss",
	      "image":"",
	      "name":"Building a Story Brand with Donald Miller | Clarify Your Message and Grow Your Business"
	   },
	   r'(?i)(bullet)(.|)(proof)':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=806",
	      "image":"",
	      "name":"Bulletproof Radio"
	   },
	   r'(?i)(bull)(.|)(eye)|jesse thorn':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510309",
	      "image":"",
	      "name":"Bullseye with Jesse Thorn"
	   },
	   r'(?i)(business).(english)':{
	      "stream":"http://feeds.feedburner.com/businessenglishpod",
	      "image":"",
	      "name":"Business English Pod :: Learn Business English Online"
	   },
	   r'(?i)(but).+(why)':{
	      "stream":"http://feedpress.me/vpr-but-why",
	      "image":"",
	      "name":"But Why: A Podcast for Curious Kids"
	   },
	   r'(?i)(Buzz(.|)Feed).+(internet).+(exp)':{
	      "stream":"http://rss.acast.com/internetexplorer",
	      "image":"",
	      "name":"BuzzFeed's Internet Explorer"
	   },
	   r'(?i)(cheap).+(ass).+(game)':{
	      "stream":"https://www.cheapassgamer.com/podcast/cagcast.xml",
	      "image":"",
	      "name":"Cheap Ass Gamer"
	   },
	   r'(?i)(call).+(chels)':{
	      "stream":"http://feeds.feedburner.com/CallChelseaPeretti",
	      "image":"",
	      "name":"Call Chelsea Peretti"
	   },
	   r'(?i)(call).+(your).+(girl)':{
	      "stream":"http://rss.acast.com/callyourgirlfriend",
	      "image":"",
	      "name":"Call Your Girlfriend"
	   },
	   r'(?i)(\s|^)(car)(.|)(cast)':{
	      "stream":"http://feeds.feedburner.com/CarCast",
	      "image":"",
	      "name":"CarCast"
	   },
	   r'(?i)(card).+(zone)':{
	      "stream":"http://podcasts.grantcardone.com/xml/cardonezone.xml",
	      "image":"",
	      "name":"Cardone Zone"
	   },
	   r'(?i)(career).+(day)':{
	      "stream":"http://careerdayshow.libsyn.com/rss",
	      "image":"",
	      "name":"Career Day"
	   },
	   r'(?i)(Carnegie Council)':{
	      "stream":"http://www.carnegiecouncil.org/resources/audio/rss/feed.xml",
	      "image":"",
	      "name":"Carnegie Council Audio Podcast"
	   },
	   r'(?i)(car(.|)stuff)':{
	      "stream":"http://www.howstuffworks.com/podcasts/carstuff.rss",
	      "image":"",
	      "name":"CarStuff"
	   },
	   r'(?i)(cath).+(ans)':{
	      "stream":"http://feeds.feedburner.com/catholic/cal",
	      "image":"",
	      "name":"Catholic Answers Live"
	   },
	   r'(?i)(cath).+(stuff|thing).+(you).+(should)':{
	      "stream":"http://feeds.feedburner.com/catholicstuffpodcast/DpqF",
	      "image":"",
	      "name":"Catholic Stuff You Should Know"
	   },
	   r'(?i)(eye).+(on).+(college)':{
	      "stream":"http://podcasts.cstv.com/feeds/mensbasketball.xml",
	      "image":"",
	      "name":"CBS Sports Eye On College Basketball Podcast"
	   },
	   r'(?i)(celt).+(christ)':{
	      "stream":"http://celticchristmaspodcast.com/rss",
	      "image":"",
	      "name":"Celtic Christmas Podcast"
	   },
	   r'(?i)(chan).+(thirty|33)':{
	      "stream":"http://feeds.feedburner.com/Channel33",
	      "image":"",
	      "name":"Channel 33"
	   },
	   r'(?i)(chat).+(with).+(trade)':{
	      "stream":"http://chatwithtraders.libsyn.com/rss",
	      "image":"",
	      "name":"Chat With Traders"
	   },
	   r'(?i)(cheap).+(heat)':{
	      "stream":"http://www.espn.com/espnradio/feeds/rss/podcast.xml?id=10116533",
	      "image":"",
	      "name":"Cheap Heat"
	   },
	   r'(?i)(child).+(fun).+(story)':{
	      "stream":"http://www.curiosoft.com/news/podcasts/storytimepodcasts.xml",
	      "image":"",
	      "name":"Children's Fun Storytime Podcast"
	   },
	   r'(?i)(\s|^)(chive)':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=720",
	      "image":"",
	      "name":"Chive Podcast"
	   },
	   r'(?i)(chris).+(hogan)|((retire).+inspire)':{
	      "stream":"http://chrishogan.ramsey.libsynpro.com/itunes",
	      "image":"",
	      "name":"Chris Hogan's Retire Inspired"
	   },
	   r'(?i)(Stereo Productions)':{
	      "stream":"http://feeds.feedburner.com/InStereoRadioShow",
	      "image":"",
	      "name":"Chus & Ceballos presents Stereo Productions Podcast"
	   },
	   r'(?i)(classical Classroom)':{
	      "stream":"https://www.houstonpublicmedia.org/podcasts/classical-classroom/",
	      "image":"",
	      "name":"Classical Classroom | Houston Public Media"
	   },
	   r'(?i)(classical master)':{
	      "stream":"http://rss.dw.com/xml/podcast_classical-masterpieces",
	      "image":"",
	      "name":"Classical Masterpieces | Deutsche Welle"
	   },
	   r'(?i)(Classical Performance)':{
	      "stream":"http://www.wgbh.org/online/clas/clas_performance.xml",
	      "image":"",
	      "name":"Classical Performance Podcast"
	   },
	   r'(?i)(Classics For Kids)':{
	      "stream":"http://www.classicsforkids.com/podcasts/classicsforkids.xml",
	      "image":"",
	      "name":"Classics For Kids"
	   },
	   r'(?i)(Coaching.+Leaders)':{
	      "stream":"http://coachingforleaders.com/podcast/feed/",
	      "image":"",
	      "name":"Coaching for Leaders"
	   },
	   r'(?i)(Code)(.|)break':{
	      "stream":"http://feeds.feedburner.com/CodebreakerByMarketplaceAndTechInsider",
	      "image":"",
	      "name":"Codebreaker"
	   },
	   r'(?i)(Code)(.|)(new|noob)':{
	      "stream":"http://feeds.codenewbie.org/cnpodcast.xml",
	      "image":"",
	      "name":"CodeNewbie"
	   },
	   r'(?i)(Code|coding).+(block)':{
	      "stream":"http://feeds.podtrac.com/tBPkjrcL0_m0",
	      "image":"",
	      "name":"Coding Blocks | Software and Web Programming / Security / Best Practices / Microsoft .NET"
	   },
	   r'(?i)(coffee).+(french)':{
	      "stream":"http://rss.acast.com/coffeebreakfrench",
	      "image":"",
	      "name":"Coffee Break French"
	   },
	   r'(?i)(coffee).+(german)':{
	      "stream":"http://rss.acast.com/coffeebreakgerman",
	      "image":"",
	      "name":"Coffee Break German"
	   },
	   r'(?i)(coffee).+(ital)':{
	      "stream":"http://rss.acast.com/coffeebreakitalian",
	      "image":"",
	      "name":"Coffee Break Italian"
	   },
	   r'(?i)(coffee).+(spanish)':{
	      "stream":"http://rss.acast.com/coffeebreakspanish",
	      "image":"",
	      "name":"Coffee Break Spanish"
	   },
	   r'(?i)(college).+(football).+(live)':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=13250702",
	      "image":"",
	      "name":"College Football Live"
	   },
	   r'(?i)^(collider)$':{
	      "stream":"http://amcmovietalk.libsyn.com/rss",
	      "image":"",
	      "name":"Collider"
	   },
	   r'(?i)(complete).+(un)':{
	      "stream":"http://cupodcast.podbean.com/feed/",
	      "image":"",
	      "name":"Completely Unnecessary Podcast"
	   },
	   r'(?i)(desus|jesus).+(mero|mario)':{
	      "stream":"http://content.complex.com/podcasts/desusvsmero/feeds.rss",
	      "image":"",
	      "name":"Complex Presents: Desus vs. Mero"
	   },
	   r'(?i)(conscious).+(parent)':{
	      "stream":"http://buildgreatminds.com/feed/podcast/",
	      "image":"",
	      "name":"Conscious Parenting For Confident & Successful Kids"
	   },
	   r'(?i)(conserv).+(fed)':{
	      "stream":"http://www.buzzsprout.com/73426.rss",
	      "image":"",
	      "name":"Conservation Federation"
	   },
	   r'(?i)(contract).+(office)':{
	      "stream":"https://www.buzzsprout.com/43525.rss",
	      "image":"",
	      "name":"Contracting Officer Podcast: Government Contracting, proposal management, proposal writing, governmental contracting, targeting"
	   },
	   r'(?i)(conversion)':{
	      "stream":"http://conversioncast.libsyn.com/rss",
	      "image":"",
	      "name":"ConversionCast"
	   },
	   r'(?i)(cool)(.|)game':{
	      "stream":"http://feeds.feedburner.com/CoolGamesInc",
	      "image":"",
	      "name":"CoolGames Inc"
	   },
	   r'(?i)^(core)($|.pod)':{
	      "stream":"http://feeds.frogpants.com/core_feed.xml",
	      "image":"",
	      "name":"CORE"
	   },
	   r'(?i)(cortex)':{
	      "stream":"https://www.relay.fm/cortex/feed",
	      "image":"",
	      "name":"Cortex"
	   },
	   r'(?i)(council).+(func)':{
	      "stream":"http://councilonhumanfunction.libsyn.com/rss",
	      "image":"",
	      "name":"Council On Human Function Podcast"
	   },
	   r'(?i)(Craig Groeschel)':{
	      "stream":"http://feedpress.me/CGLeadershipAudioiTunes",
	      "image":"",
	      "name":"Craig Groeschel Leadership Podcast"
	   },
	   r'(?i)(creat).+(dog)':{
	      "stream":"http://feeds.feedburner.com/CreativeDogTrainingOnline",
	      "image":"",
	      "name":"Creative Dog Training Online Podcast"
	   },
	   r'(?i)(creat).+(pep)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:87660023/sounds.rss",
	      "image":"",
	      "name":"Creative Pep Talk"
	   },
	   r'(?i)(Creflo Dollar Ministries)':{
	      "stream":"http://feed.theplatform.com/f/IfSiAC/p5z4rSbJ7OuA",
	      "image":"",
	      "name":"Creflo Dollar Ministries Audio Podcast"
	   },
	   r'(?i)(crime writers)':{
	      "stream":"https://rss.art19.com/crime-writers-on",
	      "image":"",
	      "name":"Crime Writers On..."
	   },
	   r'(?i)(crit.+hit)':{
	      "stream":"http://www.majorspoilers.com/media/criticalhit.xml",
	      "image":"",
	      "name":"Critical Hit: A Dungeons and Dragons Campaign"
	   },
	   r'(?i)(Crucible)':{
	      "stream":"http://feeds.feedburner.com/CrucibleRadio",
	      "image":"",
	      "name":"Crucible Radio"
	   },
	   r'(?i)(ctrl|control).+walt.+delete':{
	      "stream":"https://rss.art19.com/ctrl-walt-delete",
	      "image":"",
	      "name":"Ctrl-Walt-Delete"
	   },
	   r'(?i)(cult).+love':{
	      "stream":"http://boldturquoise.com/feed/podcast/",
	      "image":"",
	      "name":"Cultivating the Lovely- The Podcast"
	   },
	   r'(?i)(come|cum).+town':{
	      "stream":"http://shoutengine.com/CumTown.xml",
	      "image":"",
	      "name":"Cum Town"
	   },
	   r'(?i)(Daily Meditation)':{
	      "stream":"http://thedailymeditationpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Daily Meditation Podcast"
	   },
	   r'(?i)(Charles Stanley|in touch ministries)':{
	      "stream":"https://www.intouch.org/listen/podcast/today-on-radio",
	      "image":"",
	      "name":"Daily Radio Program with Charles Stanley - In Touch Ministries"
	   },
	   r'(?i)(daily.+tech.+news)':{
	      "stream":"http://feeds.feedburner.com/DailyTechNewsShow",
	      "image":"",
	      "name":"Daily Tech News Show"
	   },
	   r'(?i)(history.+hit)|dan snow':{
	      "stream":"http://rss.acast.com/dansnowshistoryhit",
	      "image":"",
	      "name":"Dan Snow's HISTORY HIT"
	   },
	   r'(?i)(dark.+(tome|home))':{
	      "stream":"https://rss.art19.com/dark-tome",
	      "image":"",
	      "name":"Dark Tome"
	   },
	   r'(?i)(dark.+night)':{
	      "stream":"http://darkestnight.libsyn.com/rss",
	      "image":"",
	      "name":"Darkest Night"
	   },
	   r'(?i)(dark.+radio)':{
	      "stream":"http://twincitiesnewstalk.iheart.com/podcast/itunes/darknessradio_itunes.xml",
	      "image":"",
	      "name":"Darkness Radio"
	   },
	   r'(?i)(data.+sci.+home)':{
	      "stream":"http://worldofpiggy.com/podcast.xml",
	      "image":"",
	      "name":"Data Science at Home"
	   },
	   r'(?i)(data.+skeptic)':{
	      "stream":"http://dataskeptic.libsyn.com/rss",
	      "image":"",
	      "name":"Data Skeptic"
	   },
	   r'(?i)(dead.+pilot.+soc)':{
	      "stream":"http://deadpilotssociety.libsyn.com/rss",
	      "image":"",
	      "name":"Dead Pilots Society"
	   },
	   r'(?i)(hank.+(jon|john))':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:156542883/sounds.rss",
	      "image":"",
	      "name":"Dear Hank and John"
	   },
	   r'(?i)(dear.+(potter))':{
	      "stream":"http://feeds.feedburner.com/HarryPotterSeminar",
	      "image":"",
	      "name":"Dear Mr. Potter: A Harry Potter Seminar"
	   },
	   r'(?i)(dear.+(sugar))':{
	      "stream":"http://feeds.wbur.org/dearsugar/podcast?feed=podcast",
	      "image":"",
	      "name":"Dear Sugar"
	   },
	   r'(?i)(decod.+(west))':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:259871793/sounds.rss",
	      "image":"",
	      "name":"Decoding Westworld"
	   },
	   r'(?i)(decon.+(success))|chris (winfield|winsfield)':{
	      "stream":"http://chriswinfield.libsyn.com/rss",
	      "image":"",
	      "name":"Deconstructing Success with Chris Winfield"
	   },
	   r'(?i)(Decrypted)':{
	      "stream":"http://www.bloomberg.com/feeds/podcasts/decrypted.xml",
	      "image":"",
	      "name":"Decrypted"
	   },
	   r'(?i)(deep.+energy)':{
	      "stream":"http://feeds.feedburner.com/DeepEnergy-MusicForMeditationRelaxationMassageAndYoga",
	      "image":"",
	      "name":"Deep Energy 2.0 - Music for Sleep, Meditation, Relaxation, Massage and Yoga"
	   },
	   r'(?i)(deep.+house.+cat)':{
	      "stream":"http://feeds.feedburner.com/PhilDahouseCat",
	      "image":"",
	      "name":"Deep House Cat"
	   },
	   r'(?i)(deep.+cho)':{
	      "stream":"http://www.blogtalkradio.com/deepakchopra/podcast",
	      "image":"",
	      "name":"Deepak Chopra Radio"
	   },
	   r'(?i)(deep.+shade.+house)':{
	      "stream":"http://feeds.feedburner.com/dsoh",
	      "image":"",
	      "name":"Deeper Shades of House - Deep House Podcast with Lars Behrenroth"
	   },
	   r'(?i)(defensive.+securi)':{
	      "stream":"http://www.defensivesecurity.org/feed/podcast/",
	      "image":"",
	      "name":"Defensive Security Podcast - Malware, Hacking, Cyber Security & Infosec"
	   },
	   r'(?i)(design.+detail)':{
	      "stream":"https://simplecast.com/podcasts/1034/rss",
	      "image":"",
	      "name":"Design Details"
	   },
	   r'(?i)(design.+matters)|Debbie Millman':{
	      "stream":"http://designobserver.com/show.designmatters2009-10.xml",
	      "image":"",
	      "name":"Design Matters with Debbie Millman: 2009-2016"
	   },
	   r'(?i)(dest.+community)':{
	      "stream":"http://DestinyCommunityPodcast.podbean.com/feed/",
	      "image":"",
	      "name":"Destiny Community Podcast"
	   },
	   r'(?i)(Detective.+(OTR|O.T.R))':{
	      "stream":"http://detectiveotr.rnn.libsynpro.com/rss",
	      "image":"",
	      "name":"Detective OTR"
	   },
	   r'(?i)(Dev.+tea)':{
	      "stream":"http://feeds.feedburner.com/DeveloperTea",
	      "image":"",
	      "name":"Developer Tea"
	   },
	   r'(?i)(Dir.+current)':{
	      "stream":"http://energy.gov/podcasts/direct-current-energygov-podcast?format=itunes",
	      "image":"",
	      "name":"Direct Current - An Energy.gov Podcast"
	   },
	   r'(?i)(Discovery)':{
	      "stream":"http://www.bbc.co.uk/programmes/p002w557/episodes/downloads.rss",
	      "image":"",
	      "name":"Discovery"
	   },
	   r'(?i)^(Dissect)$':{
	      "stream":"https://www.cityscoutmag.com/feed/dissect",
	      "image":"",
	      "name":"Dissect"
	   },
	   r'(?i)(DIY|D.I.Y).+Mus':{
	      "stream":"http://feeds.feedburner.com/cdbabydiymusicpodcast",
	      "image":"",
	      "name":"DIY Musician Podcast"
	   },
	   r'(?i)(Don Diablo)|(hex.+radio)':{
	      "stream":"https://www.thisisdistorted.com/repository/xml/DonDiabloHexagonRadio1422895802.xml",
	      "image":"",
	      "name":"Don Diablo Presents Hexagon Radio"
	   },
	   r'(?i)(Henry Cloud)|leadership.+univ':{
	      "stream":"http://feeds.feedburner.com/LeadershipUniversityPodcast",
	      "image":"",
	      "name":"Dr. Henry Cloud's Leadership University Podcast"
	   },
	   r'(?i)(Wayne.+Dyer)':{
	      "stream":"http://drwaynedyer.hayhouse.libsynpro.com/rss",
	      "image":"",
	      "name":"Dr. Wayne W. Dyer Podcast"
	   },
	   r'(?i)(dragon(.|)(baller|bowler))':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:182624645/sounds.rss",
	      "image":"",
	      "name":"DragonBallerZ : a Dragonball Z Podcast | an NthCast Production"
	   },
	   r'(?i)(dread(.|)time).+stor':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=981",
	      "image":"",
	      "name":"Dreadtime Stories with Malcolm McDowell"
	   },
	   r'(?i)(drink.+champ)':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1441?format=MP3_128K",
	      "image":"",
	      "name":"Drink Champs"
	   },
	   r'(?i)(drink.+bro)':{
	      "stream":"http://drinkingbros.libsyn.com/rss",
	      "image":"",
	      "name":"Drinkin' Bros."
	   },
	   r'(?i)(drunk.+drag)':{
	      "stream":"http://feeds.feedburner.com/DnDPodcast",
	      "image":"",
	      "name":"Drunks and Dragons - Dungeons and Dragons 5e Actual Play"
	   },
	   r'(?i)(dude.+soup)':{
	      "stream":"http://funhaus.roosterteeth.com/show/dude-soup/feed/mp3",
	      "image":"",
	      "name":"Dude Soup"
	   },
	   r'(?i)(dumb.+gay.+pol)':{
	      "stream":"http://rss.acast.com/dumbgaypolitics",
	      "image":"",
	      "name":"Dumb, Gay Politics"
	   },
	   r'(?i)(dun.+on.+basket)':{
	      "stream":"http://www.blogtalkradio.com/duncdon/podcast",
	      "image":"",
	      "name":"Dunc'd On Basketball Podcast"
	   },
	   r'(?i)(dun.+truss)|(family.+hour)':{
	      "stream":"http://feeds.feedburner.com/DuncanTrussell",
	      "image":"",
	      "name":"Duncan Trussell Family Hour"
	   },
	   r'(?i)(dun.+mast.+block)':{
	      "stream":"http://dungeonmasterblock.podbean.com/feed/",
	      "image":"",
	      "name":"Dungeon Master's Block"
	   },
	   r'(?i)(dun.+random)':{
	      "stream":"http://dungeonsandrandomness.podbean.com/feed/",
	      "image":"",
	      "name":"Dungeons and Randomness: A D&D Podcast"
	   },
	   r'(?i)(eagle.+nation)':{
	      "stream":"http://teamrwb.libsyn.com/rss",
	      "image":"",
	      "name":"Eagle Nation Podcast"
	   },
	   r'(?i)(ear.+bisc)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:59736920/sounds.rss",
	      "image":"",
	      "name":"Ear Biscuits"
	   },
	   r'(?i)(ear.+you.+happy)':{
	      "stream":"http://feeds.feedburner.com/EarnYouHappy",
	      "image":"",
	      "name":"Earn Your Happy Podcast | Motivation | Self-Love | Entrepreneurship | Confidence | Fitness and Life Coaching with Lori Harder"
	   },
	   r'(?i)(EconTalk)':{
	      "stream":"http://files.libertyfund.org/econtalk/EconTalk.xml",
	      "image":"",
	      "name":"EconTalk"
	   },
	   r'(?i)(ED MYLETT)':{
	      "stream":"http://edmylett.libsyn.com/rss",
	      "image":"",
	      "name":"ED MYLETT SHOW"
	   },
	   r'(?i)(Effect.+Wild)':{
	      "stream":"http://www.baseballprospectus.com/blog/daily_podcast/feed.xml",
	      "image":"",
	      "name":"Effectively Wild: The Daily Baseball Prospectus Podcast"
	   },
	   r'(?i)(Effort.+English)':{
	      "stream":"http://effortlessenglish.libsyn.com/rss",
	      "image":"",
	      "name":"Effortless English Podcast"
	   },
	   r'(?i)(Election.+College)':{
	      "stream":"http://electioncollege.libsyn.com/rss",
	      "image":"",
	      "name":"Election College | Presidential Election History"
	   },
	   r'(?i)(Eleven.+life)':{
	      "stream":"http://eleventylife.libsyn.com/rss",
	      "image":"",
	      "name":"Eleventy Life"
	   },
	   r'(?i)(ELLISTRONICS)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:255132557/sounds.rss",
	      "image":"",
	      "name":"ELLISTRONICS"
	   },
	   r'(?i)(Elmo.+Adv)':{
	      "stream":"http://downloads.cdn.sesame.org/podcast/outreach/english_rss.xml",
	      "image":"",
	      "name":"Elmo's Adventures in Spending, Saving, and Sharing"
	   },
	   r'(?i)(Em.+basic)':{
	      "stream":"http://embasic.libsyn.com/rss",
	      "image":"",
	      "name":"EM Basic"
	   },
	   r'(?i)(Em.+crit)':{
	      "stream":"http://emcrit.org/feed/podcast/",
	      "image":"",
	      "name":"EMCrit Podcast - Critical Care and Resuscitation"
	   },
	   r'(?i)(Em.+med.+case)':{
	      "stream":"https://emergencymedicinecases.com/feed/podcast/",
	      "image":"",
	      "name":"Emergency Medicine Cases"
	   },
	   r'(?i)(Em.+Infect.+dis)':{
	      "stream":"https://www2c.cdc.gov/podcasts/createrss.asp?t=a&c=49",
	      "image":"",
	      "name":"Emerging Infectious Diseases"
	   },
	   r'(?i)(Emper.+Rome)':{
	      "stream":"http://www.latrobe.edu.au/marketing/assets/podcasts/rssfeeds/caesar.xml",
	      "image":"",
	      "name":"Emperors of Rome"
	   },
	   r'(?i)(English.+Second.+Lang)':{
	      "stream":"http://feeds.feedburner.com/EnglishAsASecondLanguagePodcast",
	      "image":"",
	      "name":"English as a Second Language (ESL) Podcast - Learn English Online"
	   },
	   r'(?i)(Enjoying.+Life)':{
	      "stream":"http://simplerhappierlifepodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Enjoying Life On A Budget Podcast"
	   },
	   r'(?i)(Enough.+About.+Me)|Kirk Minihane':{
	      "stream":"http://feeds.feedburner.com/enoughaboutmepodcast",
	      "image":"",
	      "name":"Enough About Me with Kirk Minihane"
	   },
	   r'(?i)(Entrepr.+Thought.+Lead)':{
	      "stream":"http://web.stanford.edu/group/edcorner/uploads/podcast/EducatorsCorner.xml",
	      "image":"",
	      "name":"Entrepreneurial Thought Leaders"
	   },
	   r'(?i)(Entrepr.+Fire)':{
	      "stream":"http://entrepreneuronfire.libsyn.com/rss",
	      "image":"",
	      "name":"Entrepreneur on FIRE"
	   },
	   r'(?i)(Epic.+real.+est.+invest)':{
	      "stream":"http://eprei.libsyn.com/rss",
	      "image":"",
	      "name":"Epic Real Estate Investing"
	   },
	   r'(?i)(ESPN FC)':{
	      "stream":"http://www.espn.com/espnradio/feeds/rss/podcast.xml?id=10672984",
	      "image":"",
	      "name":"ESPN FC"
	   },
	   r'(?i)(every(.|)day.+drive)':{
	      "stream":"http://shoutengine.com/EverydayDriverCarDebate.xml",
	      "image":"",
	      "name":"Everyday Driver Car Debate"
	   },
	   r'(?i)(Exchange.+Goldman)':{
	      "stream":"http://www.goldmansachs.com/exchanges-podcast/feed.rss",
	      "image":"",
	      "name":"Exchanges at Goldman Sachs"
	   },
	   r'(?i)(Explain.+thing.+me)':{
	      "stream":"http://explainthingstome.libsyn.com/rss",
	      "image":"",
	      "name":"Explain Things To Me"
	   },
	   r'(?i)(Exponent)':{
	      "stream":"http://exponent.fm/feed/",
	      "image":"",
	      "name":"Exponent"
	   },
	   r'(?i)(fan(.|)bro).+show':{
	      "stream":"http://feeds.podtrac.com/vZEXwaruRy29",
	      "image":"",
	      "name":"FanBrosShow"
	   },
	   r'(?i)(fan).+focus.+footba':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=2942325",
	      "image":"",
	      "name":"Fantasy Focus Football"
	   },
	   r'(?i)(fan).+football.+today':{
	      "stream":"http://podcasts.cstv.com/feeds/fantasyfootball.xml",
	      "image":"",
	      "name":"Fantasy Football Today Podcast"
	   },
	   r'(?i)fantasy.+football.+week':{
	      "stream":"http://kfan.iheart.com/podcast/itunes/FantasyFBWeekly_itunes.xml",
	      "image":"",
	      "name":"Fantasy Football Weekly"
	   },
	   r'(?i)(fantasy)(.|)pro':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:243341313/sounds.rss",
	      "image":"",
	      "name":"FantasyPros - Fantasy Football Podcast"
	   },
	   r'(?i)(fat)(.|)man.+bat':{
	      "stream":"http://feeds.feedburner.com/FatManOnBatman",
	      "image":"",
	      "name":"Fat Man on Batman"
	   },
	   r'(?i)(FBI|F.B.I).+this.+week':{
	      "stream":"https://www.fbi.gov/feeds/fbi-this-week-podcast/itunes.xml",
	      "image":"",
	      "name":"FBI, This Week Podcast"
	   },
	   r'(?i)(FDNY|F.D.N.U|new.+york.+fire.+dept|fire.+department.+new.+york)':{
	      "stream":"http://www.fdnypro.org/feed/podcast",
	      "image":"",
	      "name":"FDNY Pro"
	   },
	   r'(?i)(Federal.+soc)':{
	      "stream":"http://fedsoc.server326.com/audio/MP3s/fsaudio.xml",
	      "image":"",
	      "name":"Federalist Society Event Audio"
	   },
	   r'(?i)film.+(sack|stack)':{
	      "stream":"http://feeds.frogpants.com/filmsack_feed.xml",
	      "image":"",
	      "name":"Film Sack"
	   },
	   r'(?i)(film(.|)(spot))':{
	      "stream":"http://feeds.feedburner.com/cinecast",
	      "image":"",
	      "name":"Filmspotting"
	   },
	   r'(?i)(financ).+independ':{
	      "stream":"http://feeds.feedburner.com/MadFientistPodcast",
	      "image":"",
	      "name":"Financial Independence Podcast"
	   },
	   r'(?i)(fire)(.|)team.+chat':{
	      "stream":"http://feeds.feedburner.com/FireteamChatIgnsDestinyPodcast",
	      "image":"",
	      "name":"Fireteam Chat: IGN's Destiny Podcast"
	   },
	   r'(?i)(first).+take':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=6247496",
	      "image":"",
	      "name":"First Take"
	   },
	   r'(?i)(first).+thing':{
	      "stream":"http://feedpress.me/first-things-podcast",
	      "image":"",
	      "name":"First Things Podcast"
	   },
	   r'(?i)((fit).+conf|Vinnie T)':{
	      "stream":"http://angriesttrainer.libsyn.com/rss",
	      "image":"",
	      "name":"Fitness Confidential with Vinnie Tortorich"
	   },
	   r'(?i)(flash.+forward)':{
	      "stream":"http://www.flashforwardpod.com/feed/podcast/",
	      "image":"",
	      "name":"Flash Forward"
	   },
	   r'(?i)(fly(.|)lady)':{
	      "stream":"http://www.blogtalkradio.com/flylady/podcast",
	      "image":"",
	      "name":"FlyLady and Friends"
	   },
	   r'(?i)(focus.+family).+daily':{
	      "stream":"http://feeds.feedburner.com/FocusOnTheFamilyDailyBroadcast",
	      "image":"",
	      "name":"Focus on the Family Daily Broadcast"
	   },
	   r'(?i)(focus.+marriage)':{
	      "stream":"http://feeds.feedburner.com/focus-on-the-family/focus-on-marriage",
	      "image":"",
	      "name":"Focus on the Family: Focus on Marriage"
	   },
	   r'(?i)(focus.+parent)':{
	      "stream":"http://feeds.feedburner.com/focus-on-the-family/focus-on-parenting",
	      "image":"",
	      "name":"Focus on the Family: Focus on Parenting"
	   },
	   r'(?i)(food.+psych)':{
	      "stream":"http://foodpsych.libsyn.com/rss",
	      "image":"",
	      "name":"Food Psych - Intuitive Eating, Positive Body Image, & Eating Disorder Recovery"
	   },
	   r'(?i)(Gaurd.+Football.+Week)|(Football.+Week).+gaurd':{
	      "stream":"https://www.theguardian.com/football/series/footballweekly/podcast.xml",
	      "image":"",
	      "name":"Football Weekly - The Guardian"
	   },
	   r'(?i)(For Azeroth)':{
	      "stream":"http://feeds.feedburner.com/forazeroth",
	      "image":"",
	      "name":"For Azeroth!: A World of Warcraft Podcast"
	   },
	   r'(?i)(For.+cry.+out)':{
	      "stream":"http://feeds.feedburner.com/TheParentExperiment",
	      "image":"",
	      "name":"For Crying Out Loud"
	   },
	   r'(?i)found.+fitness':{
	      "stream":"http://podcast.foundmyfitness.com/rss.xml",
	      "image":"",
	      "name":"FoundMyFitness"
	   },
	   r'(?i)(fresh.+life)':{
	      "stream":"http://feeds.feedburner.com/FreshLifeChurch",
	      "image":"",
	      "name":"Fresh Life Church"
	   },
	   r'(?i)(from.+top)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510026",
	      "image":"",
	      "name":"From the Top"
	   },
	   r'(?i)(front(.|)line)':{
	      "stream":"http://feeds.feedburner.com/FrontlineAudiocastPbs",
	      "image":"",
	      "name":"FRONTLINE: Audiocast | PBS"
	   },
	   r'(?i)(full.+sith)':{
	      "stream":"http://www.thamike.com/fullofsith/fosxml.xml",
	      "image":"",
	      "name":"Full Of Sith: Star Wars News, Discussions and Interviews"
	   },
	   r'(?i)(Game.+Thrones.The.pod)':{
	      "stream":"http://baldmove.com/feed/game-of-thrones-podcast/",
	      "image":"",
	      "name":"Game of Thrones The Podcast"
	   },
	   r'(?i)(Game.+scoop)':{
	      "stream":"http://feeds.ign.com/ignfeeds/podcasts/gamescoop/",
	      "image":"",
	      "name":"Game Scoop!"
	   },
	   r'(?i)(Gastro(.|)pod)':{
	      "stream":"https://gastropod.com/feed/",
	      "image":"",
	      "name":"Gastropod"
	   },
	   r'(?i)(gate(.|)way).+church':{
	      "stream":"http://gatewaypeople.com/ministries/life/podcast/audio/this",
	      "image":"",
	      "name":"Gateway Church Audio Podcast"
	   },
	   r'(?i)(Geek.+Guide.+Galaxy)':{
	      "stream":"http://www.davidbarrkirtley.com/podcast/geeksguideshow.xml",
	      "image":"",
	      "name":"Geek's Guide to the Galaxy - Science Fiction Interviews, Movie Reviews, Sci-Fi Books and Writing"
	   },
	   r'(?i)(Genius.+Network)':{
	      "stream":"http://geniusnetwork.libsyn.com/rss",
	      "image":"",
	      "name":"Genius Network - The World's Best Wisdom - Presented By Joe Polish"
	   },
	   r'(?i)(get.+fit.+guy)':{
	      "stream":"http://www.quickanddirtytips.com/xml/getfitguy.xml",
	      "image":"",
	      "name":"Get-Fit Guy's Quick and Dirty Tips to Slim Down and Shape Up"
	   },
	   r'(?i)(get.+it.+done.+guy)':{
	      "stream":"http://www.quickanddirtytips.com/xml/getitdone.xml",
	      "image":"",
	      "name":"Get-It-Done Guy's Quick and Dirty Tips to Work Less and Do More"
	   },
	   r'(?i)(Ghost.+Stor.+destiny)':{
	      "stream":"http://destinyghoststories.podbean.com/feed/",
	      "image":"",
	      "name":"Ghost Stories, a Destiny Podcast"
	   },
	   r'(?i)(Giant).+(bomb)':{
	      "stream":"http://www.giantbomb.com/feeds/podcast/",
	      "image":"",
	      "name":"Giant Bombcast"
	   },
	   r'(?i)(Giant).+(hist)':{
	      "stream":"http://gohistorypodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Giants of History"
	   },
	   r'(?i)(Gilbert).+(Got|god)':{
	      "stream":"http://feeds.sideshownetwork.tv/GilbertGottfried",
	      "image":"",
	      "name":"Gilbert Gottfried's Amazing Colossal Podcast"
	   },
	   r'(?i)(Gilmore).+(Girls).+year.+life.+after':{
	      "stream":"http://www.afterbuzztv.com/aftershows/gilmore-girls-afterbuzz-tv-aftershow/feed/",
	      "image":"",
	      "name":"Gilmore Girls: A Year In The Life After Show"
	   },
	   r'(?i)(Gilmored)':{
	      "stream":"http://gilmored.libsyn.com/rss",
	      "image":"",
	      "name":"Gilmored: A New Gilmore Girls Podcast"
	   },
	   r'(?i)(girl).+on.+(guy)':{
	      "stream":"http://girlonguy.libsyn.com/rss",
	      "image":"",
	      "name":"Girl on Guy with Aisha Tyler"
	   },
	   r'(?i)((girl)(.|)boss.+radio)|(Sophia Amoruso)':{
	      "stream":"http://feeds.feedburner.com/girlbossradio",
	      "image":"",
	      "name":"Girlboss Radio with Sophia Amoruso"
	   },
	   r'(?i)(Glob.+Recon)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:200760230/sounds.rss",
	      "image":"",
	      "name":"Global Recon Podcast"
	   },
	   r'(?i)(Glor.+mund)|(Chris.+N[oi]ckels)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:123887054/sounds.rss",
	      "image":"",
	      "name":"Glorious in the Mundane Podcast with Christy Nockels"
	   },
	   r'(?i)(god.+awful.+movie)':{
	      "stream":"https://audioboom.com/channels/4829841.rss",
	      "image":"",
	      "name":"God Awful Movies"
	   },
	   r'(?i)(god.+cent.+mom)':{
	      "stream":"http://feeds.feedburner.com/GodCenteredMomPodcast",
	      "image":"",
	      "name":"God Centered Mom Podcast"
	   },
	   r'(?i)(godsfall|god fall)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:8760975/sounds.rss",
	      "image":"",
	      "name":"Godsfall: Divine & Conquer"
	   },
	   r'(?i)(going.+in.raw)':{
	      "stream":"http://goinginraw.libsyn.com/rss",
	      "image":"",
	      "name":"GOING IN RAW PRO WRESTLING PODCAST"
	   },
	   r'(?i)(good.+job.+brain)':{
	      "stream":"http://goodjobbrain.libsyn.com/rss",
	      "image":"",
	      "name":"Good Job, Brain!"
	   },
	   r'(?i)(good.+life.+proj)':{
	      "stream":"http://www.goodlifeproject.com/feed/podcast/",
	      "image":"",
	      "name":"Good Life Project"
	   },
	   r'(?i)watch(.|)dog.+report':{
	      "stream":"http://www.gao.gov/podcast/watchdog.xml",
	      "image":"",
	      "name":"Government Accountability Office (GAO) Podcast: Watchdog Report"
	   },
	   r'(?i)(gov.+info.+sec)':{
	      "stream":"http://www.govinfosecurity.com/itunes_rss_podcasts.php",
	      "image":"",
	      "name":"Government Information Security Podcast"
	   },
	   r'(?i)(gov(.+|)love)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:116855785/sounds.rss",
	      "image":"",
	      "name":"GovLove"
	   },
	   r'(?i)(gravy)':{
	      "stream":"http://sfagravy.libsyn.com/rss",
	      "image":"",
	      "name":"Gravy"
	   },
	   r'(?i)(grim.+fairy.+tale)':{
	      "stream":"http://www.loyalbooks.com/book/fairy-tales-by-the-brothers-grimm/feed",
	      "image":"",
	      "name":"Grimms' Fairy Tales by Jacob & Wilhelm Grimm"
	   },
	   r'(?i)(grump.+old.+geek)':{
	      "stream":"http://grumpyoldgeeks.libsyn.com/rss",
	      "image":"",
	      "name":"Grumpy Old Geeks - Covering tech news, security, movies, tv shows, and books for tech savvy adults"
	   },
	   r'(?i)(Guardian.+radio)':{
	      "stream":"http://guardianradio.podbean.com/feed",
	      "image":"",
	      "name":"Guardian Radio"
	   },
	   r'(?i)(Guitar Music Theory)':{
	      "stream":"http://recordings.talkshoe.com/rss37557.xml",
	      "image":"",
	      "name":"Guitar Music Theory Lessons - Desi Serna"
	   },
	   r'(?i)(Gun talk)':{
	      "stream":"http://guntalk.libsyn.com/rss",
	      "image":"",
	      "name":"Gun Talk"
	   },
	   r'(?i)(gun(.|)fight.+cast)':{
	      "stream":"http://www.gunfightercast.com/wordpress/feed/podcast/",
	      "image":"",
	      "name":"Gunfighter Cast"
	   },
	   r'(?i)(half.+size)':{
	      "stream":"http://www.halfsizeme.com/feed/podcast/",
	      "image":"",
	      "name":"Half Size Me"
	   },
	   r'(?i)(Hannibal Buress|Hand.+Ramble)':{
	      "stream":"http://rss.earwolf.com/handsome-rambler",
	      "image":"",
	      "name":"Hannibal Buress: Handsome Rambler"
	   },
	   r'(?i)(Happier.+gretch)':{
	      "stream":"http://feeds.feedburner.com/HappierWithGretchenRubin",
	      "image":"",
	      "name":"Happier with Gretchen Rubin"
	   },
	   r'(?i)(Happy.+sad.+conf)':{
	      "stream":"http://feeds.feedburner.com/HappySadConfused",
	      "image":"",
	      "name":"Happy Sad Confused"
	   },
	   r'(?i)(harmon)':{
	      "stream":"http://feeds.feedburner.com/HarmontownPodcast",
	      "image":"",
	      "name":"Harmontown with Dan Harmon"
	   },
	   r'(?i)(Harvest Bible Chapel)':{
	      "stream":"http://harvestbible.podbean.com/feed/",
	      "image":"",
	      "name":"Harvest Bible Chapel"
	   },
	   r'(?i)(Harvest.+Greg Laurie)':{
	      "stream":"http://feeds.harvest.org/sunday-audio",
	      "image":"",
	      "name":"Harvest: Greg Laurie Audio"
	   },
	   r'(?i)(Hay.+house.+med)':{
	      "stream":"http://hhmeds.hayhouse.libsynpro.com/rss",
	      "image":"",
	      "name":"Hay House Meditations"
	   },
	   r'(?i)(Hay.+house.+radio)':{
	      "stream":"http://hhradio.hayhouse.libsynpro.com/rss",
	      "image":"",
	      "name":"Hay House Radio Podcast"
	   },
	   r'(?i)(harvard.+business.+idea)':{
	      "stream":"http://feeds.harvardbusiness.org/harvardbusiness/ideacast",
	      "image":"",
	      "name":"Harvard Business IdeaCast"
	   },
	   r'(?i)(healthy.+birth.+happy.+bab)':{
	      "stream":"http://healthybirthshappybabies.libsyn.com/rss",
	      "image":"",
	      "name":"Healthy Births, Happy Babies"
	   },
	   r'(?i)(Heart Wisdom)':{
	      "stream":"http://heartwisdom.libsyn.com/rss",
	      "image":"",
	      "name":"Heart Wisdom with Jack Kornfield"
	   },
	   r'(?i)(heldeep radio)':{
	      "stream":"http://heldeepradio.spinninpodcasts.com/rss",
	      "image":"",
	      "name":"Heldeep Radio"
	   },
	   r'(?i)(Helga)':{
	      "stream":"http://feeds.wqxr.org/wqxr-helga",
	      "image":"",
	      "name":"Helga"
	   },
	   r'(?i)(Hello.+Magic.+Tavern)':{
	      "stream":"http://feedpress.me/magictavern",
	      "image":"",
	      "name":"Hello from the Magic Tavern"
	   },
	   r'(?i)(Here.+we.+are)':{
	      "stream":"http://www.herewearepodcast.com/rss",
	      "image":"",
	      "name":"Here We Are"
	   },
	   r'(?i)(Here.+the.+thing|ale[cx].baldwin)':{
	      "stream":"http://feeds.feedburner.com/wnycheresthething",
	      "image":"",
	      "name":"Here's The Thing with Alec Baldwin"
	   },
	   r'(?i)(Hidden track)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:262464075/sounds.rss",
	      "image":"",
	      "name":"Hidden Tracks: Stories from BART"
	   },
	   r'(?i)(Hills(.|)dale)':{
	      "stream":"http://feeds.feedburner.com/hillsdaledialogues",
	      "image":"",
	      "name":"Hillsdale Dialogues Podcast"
	   },
	   r'(?i)(hip hop daily)':{
	      "stream":"http://hiphopdaily.libsyn.com/rss",
	      "image":"",
	      "name":"HIP HOP DAILY"
	   },
	   r'(?i)(hist.+black)':{
	      "stream":"https://feeds.publicradio.org/public_feeds/historically-black/itunes/rss",
	      "image":"",
	      "name":"Historically Black"
	   },
	   r'(?i)(hist.+japan)':{
	      "stream":"http://historyofjapan.libsyn.com/rss",
	      "image":"",
	      "name":"History of Japan"
	   },
	   r'(?i)(hist.+philo)':{
	      "stream":"http://hopwag.podbean.com/feed/",
	      "image":"",
	      "name":"History of Philosophy Without Any Gaps"
	   },
	   r'(?i)(hist.+on.+fire)':{
	      "stream":"http://feeds.podtrac.com/xUnmFXZLuavF",
	      "image":"",
	      "name":"History on Fire"
	   },
	   r'(?i)(hist.+today)':{
	      "stream":"http://historytoday.podomatic.com/rss2.xml",
	      "image":"",
	      "name":"History Today Podcast"
	   },
	   r'(?i)(hist.+viking)':{
	      "stream":"https://cdn-podcasts.video.aetnd.com/vikings-podcast.xml",
	      "image":"",
	      "name":"History Vikings Podcast"
	   },
	   r'(?i)(holly.+babble)':{
	      "stream":"http://feeds.feedburner.com/HollywoodBabbleOnPod",
	      "image":"",
	      "name":"Hollywood Babble-On"
	   },
	   r'(?i)(home(.|)made.+stor)':{
	      "stream":"http://rss.acast.com/homemadestories",
	      "image":"",
	      "name":"Homemade Stories"
	   },
	   r'(?i)(hosp.+inter.+med)':{
	      "stream":"http://hospitalmedicine.podbean.com/feed/",
	      "image":"",
	      "name":"Hospital and Internal Medicine Podcast"
	   },
	   r'(?i)(hot.+take(.|)down)':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=12474672",
	      "image":"",
	      "name":"Hot Takedown"
	   },
	   r'(?i)(hound.+tall)|moshe kasher':{
	      "stream":"http://feeds.feedburner.com/HoundTall",
	      "image":"",
	      "name":"Hound Tall with Moshe Kasher"
	   },
	   r'(?i)(How.+To.+Be.+Amazing)|Michael Ian Black':{
	      "stream":"http://feeds.howtobeamazingshow.com/htbashow",
	      "image":"",
	      "name":"How To Be Amazing with Michael Ian Black"
	   },
	   r'(?i)(How.+To.+do.+every)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510303",
	      "image":"",
	      "name":"How To Do Everything"
	   },
	   r'(?i)(hunt.+Talk.+radio|Randy Newberg.+filtered)':{
	      "stream":"http://hunttalk.libsyn.com/rss",
	      "image":"",
	      "name":"Hunt Talk Radio, Randy Newberg Unfiltered"
	   },
	   r'(?i)(Talk.+star.+trek)':{
	      "stream":"http://rss.art19.com/i-just-want-to-talk-star-trek",
	      "image":"",
	      "name":"I Just Want To Talk Star Trek"
	   },
	   r'(?i)(tell.+my.+husband.+new)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:188712331/sounds.rss",
	      "image":"",
	      "name":"I Tell My Husband The News"
	   },
	   r'(?i)(I.+was.+there.+to)':{
	      "stream":"http://feeds.feedburner.com/IWasThereToo",
	      "image":"",
	      "name":"I Was There Too"
	   },
	   r'(?i)(I.+name.+this.+later)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:138976584/sounds.rss",
	      "image":"",
	      "name":"I'll Name This Podcast Later"
	   },
	   r'(?i)(Ice.(T($|\s)|tea))|(final level)':{
	      "stream":"http://icetfinallevel.libsyn.com/rss",
	      "image":"",
	      "name":"Ice T Final Level"
	   },
	   r'(?i)(local.+gov.+life)':{
	      "stream":"http://feeds.feedburner.com/LocalGovLife",
	      "image":"",
	      "name":"ICMA: Local Gov Life"
	   },
	   r'(?i)(ICU|I.C.U).+round':{
	      "stream":"http://burndoc.libsyn.com/rss",
	      "image":"",
	      "name":"ICU Rounds"
	   },
	   r'(?i)(Idle.thumb)':{
	      "stream":"http://www.idlethumbs.net/feeds/idle-thumbs",
	      "image":"",
	      "name":"Idle Thumbs"
	   },
	   r'(?i)(I|eye)(.|)fan(.|)boy':{
	      "stream":"http://feeds.feedburner.com/ifanboyPOW",
	      "image":"",
	      "name":"iFanboy.com Comic Book Podcast"
	   },
	   r'(?i)(IGN|I.G.N).game':{
	      "stream":"http://feeds.ign.com/ignfeeds/podcasts/games/",
	      "image":"",
	      "name":"IGN Games Podcasts"
	   },
	   r'(?i)(Imagin.+world)':{
	      "stream":"http://feeds.feedburner.com/imaginaryworldspodcast",
	      "image":"",
	      "name":"Imaginary Worlds"
	   },
	   r'(?i)(Improp.+Etiq)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:224639879/sounds.rss",
	      "image":"",
	      "name":"Improper Etiquette"
	   },
	   r'(?i)(^In.Our.Time$)':{
	      "stream":"http://www.bbc.co.uk/programmes/b006qykl/episodes/downloads.rss",
	      "image":"",
	      "name":"In Our Time"
	   },
	   r'(?i)(In.Our.Time.+hist)':{
	      "stream":"http://www.bbc.co.uk/programmes/p01dh5yg/episodes/downloads.rss",
	      "image":"",
	      "name":"In Our Time: History"
	   },
	   r'(?i)(Innovation and Leadership)':{
	      "stream":"http://icollective.libsyn.com/rss",
	      "image":"",
	      "name":"Innovation and Leadership"
	   },
	   r'(?i)(Inquiring Minds)':{
	      "stream":"http://feeds.feedburner.com/inquiring-minds",
	      "image":"",
	      "name":"Inquiring Minds"
	   },
	   r'(?i)(Insecure Aftershow)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:259882856/sounds.rss",
	      "image":"",
	      "name":"Insecuritea: The Insecure Aftershow"
	   },
	   r'(?i)(Inside Appalachia)':{
	      "stream":"http://wvpublic.org/podcasts/41/rss.xml",
	      "image":"",
	      "name":"Inside Appalachia"
	   },
	   r'(?i)(Inside.+(NYPD|N.Y.P.D))':{
	      "stream":"http://www.nyc.gov/html/nypd/audio/podcast_nycgov.xml",
	      "image":"",
	      "name":"Inside the NYPD"
	   },
	   r'(?i)(Inside.+(team).+room)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:132077920/sounds.rss",
	      "image":"",
	      "name":"Inside The Team Room"
	   },
	   r'(?i)insight.+liv.+dail':{
	      "stream":"http://feeds.feedburner.com/InsightForLivingDailyBroadcast",
	      "image":"",
	      "name":"Insight for Living Daily Broadcast"
	   },
	   r'(?i)(Inspir.+Living)':{
	      "stream":"http://podcast.livinghour.org/feed/",
	      "image":"",
	      "name":"Inspirational Living: Motivation, Self-Help, Spirituality & Positive Thinking"
	   },
	   r'(?i)(Inspir.+nation)':{
	      "stream":"http://inspirenation.libsyn.com/rss",
	      "image":"",
	      "name":"Inspire Nation | Daily Inspiration - Motivation - Meditation | Law of Attraction | Health | Career | Spirituality | Self-Help"
	   },
	   r'(?i)(Inspir.+to.+action)|InspiredtToAction\.com':{
	      "stream":"http://feeds.feedburner.com/inspiredtoaction/GvcC",
	      "image":"",
	      "name":"InspiredtToAction.com - Inspiration for Motherhood"
	   },
	   r'(?i)(Intersections)':{
	      "stream":"http://brookingsintersections.libsyn.com/rss",
	      "image":"",
	      "name":"Intersections"
	   },
	   r'(?i)(Invest Like.+Best)':{
	      "stream":"http://investlikethebest.libsyn.com/rss",
	      "image":"",
	      "name":"Invest Like the Best"
	   },
	   r'(?i)(Invested)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:142420018/sounds.rss",
	      "image":"",
	      "name":"Invested: The Rule #1 Podcast"
	   },
	   r'(?i)(Irish.+Celtic.+Music)':{
	      "stream":"http://bellobard.libsyn.com/rss",
	      "image":"",
	      "name":"Irish and Celtic Music Podcast"
	   },
	   r'(?i)(It.+cole.+world)':{
	      "stream":"http://realcoleworld.podomatic.com/rss2.xml",
	      "image":"",
	      "name":"It's a Cole World"
	   },
	   r'(?i)(It.+super.+effect)':{
	      "stream":"http://feeds.feedburner.com/pkmncast",
	      "image":"",
	      "name":"It's Super Effective"
	   },
	   r'(?i)(Jalen.+jacoby)':{
	      "stream":"http://www.espn.com/espnradio/feeds/rss/podcast.xml?id=9545077",
	      "image":"",
	      "name":"Jalen and Jacoby"
	   },
	   r'(?i)(James.+bond)':{
	      "stream":"http://feeds.feedburner.com/JamesBonding",
	      "image":"",
	      "name":"James Bonding"
	   },
	   r'(?i)(James.+MacDonald)|(walk in the word)':{
	      "stream":"http://feeds.feedburner.com/walkintheword/wxZf",
	      "image":"",
	      "name":"James MacDonald: Walk in the Word Audio"
	   },
	   r'(?i)(java(.|)script).+jab':{
	      "stream":"https://feeds.feedwrench.com/JavaScriptJabber.rss",
	      "image":"",
	      "name":"JavaScript Jabber"
	   },
	   r'(?i)(jay.+silent.+bob).+old':{
	      "stream":"http://feeds.feedburner.com/JaySilentBobGetOld",
	      "image":"",
	      "name":"Jay and Silent Bob Get Old"
	   },
	   r'(?i)(jenna.+julien)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:109532020/sounds.rss",
	      "image":"",
	      "name":"Jenna and Julien Podcast"
	   },
	   r'(?i)(jesus.+call)':{
	      "stream":"http://jesuscalling.libsyn.com/jclibpodcast",
	      "image":"",
	      "name":"Jesus Calling Podcast"
	   },
	   r'(?i)(jim.+beaver)|(project.action)':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=950",
	      "image":"",
	      "name":"Jim Beaver's Project Action"
	   },
	   r'(?i)(Jim Corn)':{
	      "stream":"https://audioboom.com/channels/4756470.rss",
	      "image":"",
	      "name":"Jim Cornette Experience"
	   },
	   r'(?i)(Jim.+norton.+sam.+rob)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:258167968/sounds.rss",
	      "image":"",
	      "name":"Jim Norton and Sam Roberts"
	   },
	   r'(?i)(Jim Rome)|daily jungle':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1476?format=MP3_128K",
	      "image":"",
	      "name":"Jim Rome's Daily Jungle"
	   },
	   r'(?i)(Jimquisition)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:125332894/sounds.rss",
	      "image":"",
	      "name":"Jimquisition"
	   },
	   r'(?i)(John Piper Sermons)':{
	      "stream":"http://feed.desiringgod.org/messages.rss",
	      "image":"",
	      "name":"John Piper Sermons"
	   },
	   r'(?i)(Joseph Prince)':{
	      "stream":"http://feeds.feedburner.com/JosephPrinceAudioPodcast",
	      "image":"",
	      "name":"Joseph Prince Audio Podcast"
	   },
	   r'(?i)(Joyce Meyer)':{
	      "stream":"http://feeds.feedburner.com/joycemeyer/SFiE",
	      "image":"",
	      "name":"Joyce Meyer Radio Podcast"
	   },
	   r'(?i)(Juan Epstein)':{
	      "stream":"http://rosenbergradio.com/category/juan-epstein/feed/",
	      "image":"",
	      "name":"Juan Epstein"
	   },
	   r'(?i)(John Hodgman)':{
	      "stream":"http://feeds.feedburner.com/todayinthepast",
	      "image":"",
	      "name":"Judge John Hodgman"
	   },
	   r'(?i)(Juicy Scoop)|heather.+M(c|ac)Donald':{
	      "stream":"http://rss.art19.com/juicy-scoop",
	      "image":"",
	      "name":"Juicy Scoop with Heather McDonald"
	   },
	   r'(?i)(Keto Talk)|(Jimmy Moore.+doc)':{
	      "stream":"http://ketotalk.libsyn.com/rss",
	      "image":"",
	      "name":"Keto Talk With Jimmy Moore & The Doc"
	   },
	   r'(?i)(Kevin Pollak)':{
	      "stream":"http://feeds.feedburner.com/KevinPollaksChatShow-Audio",
	      "image":"",
	      "name":"Kevin Pollak's Chat Show"
	   },
	   r'(?i)(Kid.+Music Planet)':{
	      "stream":"http://feeds.feedburner.com/kidsmusicplanetpodcast",
	      "image":"",
	      "name":"Kids Music Planet Podcast"
	   },
	   r'(?i)(Killing.+the.+Town)':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=970",
	      "image":"",
	      "name":"Killing the Town with Storm and Cyrus"
	   },
	   r'(?i)(Kind(a|\sof) funny)':{
	      "stream":"http://feeds.podtrac.com/DBhVerLhyNUM",
	      "image":"",
	      "name":"Kinda Funny Gamescast"
	   },
	   r'(?i)(King Falls)':{
	      "stream":"https://audioboom.com/channels/4256036.rss",
	      "image":"",
	      "name":"King Falls AM"
	   },
	   r'(?i)(Kiss.+Me.+Quick)':{
	      "stream":"http://kisstherose.libsyn.com/rss",
	      "image":"",
	      "name":"Kiss Me Quick's Erotica: Sexy Stories with Rose Caraway"
	   },
	   r'(?i)(Knife(.|)point).+horro':{
	      "stream":"http://knifepointhorror.libsyn.com/rss",
	      "image":"",
	      "name":"Knifepoint Horror"
	   },
	   r'(?i)(night.+ren)':{
	      "stream":"http://shoutengine.com/KnightsofRen.xml",
	      "image":"",
	      "name":"Knights of Ren"
	   },
	   r'(?i)(Kris Vallotton)':{
	      "stream":"http://feeds.feedburner.com/kvministries",
	      "image":"",
	      "name":"Kris Vallotton's Podcast"
	   },
	   r'(?i)(Lad.+Who Lunch)':{
	      "stream":"http://feeds.podtrac.com/ladieswholunch",
	      "image":"",
	      "name":"Ladies Who Lunch"
	   },
	   r'(?i)(Lady(.|)gang)':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=836",
	      "image":"",
	      "name":"LadyGang"
	   },
	   r'(?i)(Latin.+USA)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510016&uid=p1qe4e85742c986fdb81d2d38ffa0d5d53",
	      "image":"",
	      "name":"Latino USA"
	   },
	   r'(?i)(Lead.+singer)':{
	      "stream":"http://feeds.feedburner.com/leadsingersyndrome",
	      "image":"",
	      "name":"Lead Singer Syndrome"
	   },
	   r'(?i)(Learn.+code)':{
	      "stream":"http://learntocodewithme.libsyn.com/rss",
	      "image":"",
	      "name":"Learn to Code With Me"
	   },
	   r'(?i)(Learn.+true.+health)|ashley james':{
	      "stream":"http://learntruehealth.libsyn.com/rss",
	      "image":"",
	      "name":"Learn True Health with Ashley James"
	   },
	   r'(?i)(Learn.+machine)':{
	      "stream":"http://learningmachines101.libsyn.com/rss",
	      "image":"",
	      "name":"Learning Machines 101"
	   },
	   r'(?i)(Let.+my.+people.+think)':{
	      "stream":"http://www.oneplace.com/ministries/let-my-people-think/subscribe/podcast.xml",
	      "image":"",
	      "name":"Let My People Think on OnePlace.com"
	   },
	   r'(?i)(Lilian Garcia)|Making Their Way':{
	      "stream":"http://www.afterbuzztv.com/aftershows/making-their-way-to-the-ring-afterbuzz-tv/feed/",
	      "image":"",
	      "name":"Lilian Garcia: Making Their Way To The Ring"
	   },
	   r'(?i)(Lime(.|)town)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:125221818/sounds.rss",
	      "image":"",
	      "name":"Limetown"
	   },
	   r'(?i)(Limit.+resource)':{
	      "stream":"http://limitedresources.libsyn.com/rss",
	      "image":"",
	      "name":"Limited Resources"
	   },
	   r'(?i)(Linear.+Digress)':{
	      "stream":"http://feeds.feedburner.com/udacity-linear-digressions?format=xml",
	      "image":"",
	      "name":"Linear Digressions"
	   },
	   r'(?i)(Listen Money Matters)':{
	      "stream":"http://www.listenmoneymatters.com/feed/podcast/",
	      "image":"",
	      "name":"Listen Money Matters"
	   },
	   r'(?i)(Little+.gold.+men)':{
	      "stream":"http://feeds.feedburner.com/littlegoldmenpodcast",
	      "image":"",
	      "name":"Little Gold Men"
	   },
	   r'(?i)(Live.+wire)':{
	      "stream":"http://www.livewireradio.org/podcast_feed",
	      "image":"",
	      "name":"Live Wire Radio"
	   },
	   r'(?i)(Living.+Edge)|Chip Ingram':{
	      "stream":"http://feeds.feedburner.com/lote-daily",
	      "image":"",
	      "name":"Living on the Edge with Chip Ingram Daily Podcast"
	   },
	   r'(?i)(London.+Economics)':{
	      "stream":"http://www.lse.ac.uk/assets/richmedia/webFeeds/publicLecturesAndEvents_iTunesStore.xml",
	      "image":"",
	      "name":"London School of Economics: Public lectures and events"
	   },
	   r'(?i)(Love and Logic)':{
	      "stream":"https://www.loveandlogic.com/feeds/loveandlogic.rss",
	      "image":"",
	      "name":"Love and Logic - Solutions for parents and teachers"
	   },
	   r'(?i)(Love Life)|matt.+huss':{
	      "stream":"http://lovelife.libsyn.com/rss",
	      "image":"",
	      "name":"Love Life with Matthew Hussey"
	   },
	   r'(?i)(Love Me)':{
	      "stream":"http://www.cbc.ca/podcasting/includes/loveme.xml",
	      "image":"",
	      "name":"Love Me"
	   },
	   r'(?i)(Love(.|)line)|(amber rose)':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1485?format=MP3_128K",
	      "image":"",
	      "name":"Loveline with Amber Rose"
	   },
	   r'(?i)(Mac (OS|o.s) Ken)':{
	      "stream":"http://macosken.libsyn.com/rss",
	      "image":"",
	      "name":"Mac OS Ken"
	   },
	   r'(?i)(Mac.+power)':{
	      "stream":"https://www.relay.fm/mpu/feed",
	      "image":"",
	      "name":"Mac Power Users"
	   },
	   r'(?i)(Mac(.|)break).+week':{
	      "stream":"http://feeds.twit.tv/mbw.xml",
	      "image":"",
	      "name":"MacBreak Weekly (MP3)"
	   },
	   r'(?i)(Mac(.|)world)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:58576458/sounds.rss",
	      "image":"",
	      "name":"Macworld"
	   },
	   r'(?i)(Mad.+about.+movies)':{
	      "stream":"http://feeds.feedburner.com/madmovies",
	      "image":"",
	      "name":"Mad About Movies"
	   },
	   r'(?i)(Magic.+Amateur)':{
	      "stream":"http://mariabartholdi.com/podcastgen/feed.xml",
	      "image":"",
	      "name":"Magic the Amateuring"
	   },
	   r'(?i)(Magic.+gather.+drive.+work)':{
	      "stream":"http://www.wizards.com/drivetoworkpodcast.xml",
	      "image":"",
	      "name":"Magic: The Gathering Drive to Work Podcast"
	   },
	   r'(?i)(Major Nelson)':{
	      "stream":"http://feeds.feedburner.com/mnitunes",
	      "image":"",
	      "name":"Major Nelson Radio"
	   },
	   r'(?i)(Make Me Smart.+with)|Kai and Molly':{
	      "stream":"https://feeds.publicradio.org/public_feeds/make-me-smart-with-kai-and-molly/itunes/rss",
	      "image":"",
	      "name":"Make Me Smart with Kai and Molly"
	   },
	   r'(?i)(Make Me Smarter)':{
	      "stream":"http://feeds.feedburner.com/MakeMeSmarterFootballPodcast",
	      "image":"",
	      "name":"Make Me Smarter Football Podcast"
	   },
	   r'(?i)(Making it)':{
	      "stream":"http://feeds.podtrac.com/jjhM1Pd5OUeO",
	      "image":"",
	      "name":"Making It With Jimmy Diresta, Bob Clagett and David Picciuto"
	   },
	   r'(?i)(Manager Tool)':{
	      "stream":"https://files.manager-tools.com/files/public/feeds/manager-tools-podcasts.xml",
	      "image":"",
	      "name":"Manager Tools"
	   },
	   r'(?i)Marathon.+Train.+Academy':{
	      "stream":"http://marathontrainingacademy.com/feed/podcast",
	      "image":"",
	      "name":"Marathon Training Academy"
	   },
	   r'(?i)(Explain.+It.+All)':{
	      "stream":"http://thestashed.com/podcasts/2015/vol1/stashed-media-network_marisa-explains-it-all.xml",
	      "image":"",
	      "name":"Marisa Explains It All With Tunisia And Jamal"
	   },
	   r'(?i)(Mark Bell)':{
	      "stream":"http://shoutengine.com/MarkBellsPowerCast.xml",
	      "image":"",
	      "name":"Mark Bell's PowerCast"
	   },
	   r'(?i)(Market(.|)fool)':{
	      "stream":"http://feeds.feedburner.com/Marketfoolery",
	      "image":"",
	      "name":"MarketFoolery"
	   },
	   r'(?i)(Marketing School)':{
	      "stream":"http://mschool.growtheverywhere.libsynpro.com/rss",
	      "image":"",
	      "name":"Marketing School"
	   },
	   r'(?i)^(Marketplace)$':{
	      "stream":"http://feeds.americanpublicmedia.org/MarketplacePodcast",
	      "image":"",
	      "name":"Marketplace"
	   },
	   r'(?i)(Marketplace Tech)':{
	      "stream":"https://feeds.publicradio.org/public_feeds/apm-marketplace-tech/itunes/rss",
	      "image":"",
	      "name":"Marketplace Tech"
	   },
	   r'(?i)(Martinis and Your Money)':{
	      "stream":"http://martinisandyourmoney.libsyn.com/rss",
	      "image":"",
	      "name":"Martinis and Your Money Podcast"
	   },
	   r'(?i)(Master of Memory)':{
	      "stream":"http://masterofmemory.com/feed/podcast/",
	      "image":"",
	      "name":"Master of Memory: Accelerated learning, education, memorization"
	   },
	   r'(?i)(Masterpiece studio)':{
	      "stream":"https://simplecast.com/podcasts/1528/rss",
	      "image":"",
	      "name":"MASTERPIECE Studio"
	   },
	   r'(?i)(Masters in Business)':{
	      "stream":"http://www.bloomberg.com/feeds/podcasts/masters_in_business.xml",
	      "image":"",
	      "name":"Masters in Business"
	   },
	   r'(?i)(Eggcellent Adventure)':{
	      "stream":"https://rss.art19.com/matt-and-dorees-eggcellent-adventure",
	      "image":"",
	      "name":"Matt and Doree's Eggcellent Adventure"
	   },
	   r'(?i)(Max Lucado)':{
	      "stream":"http://maxlucado.com/feed/custom",
	      "image":"",
	      "name":"Max Lucado"
	   },
	   r'(?i)(Me.+and.+Paranormal)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:68947374/sounds.rss",
	      "image":"",
	      "name":"Me and Paranormal You"
	   },
	   r'(?i)(Meat(.|)eater)':{
	      "stream":"http://www.themeateater.com/podcasts/feed/podcast/",
	      "image":"",
	      "name":"MeatEater Podcast"
	   },
	   r'(?i)(Meditation Mini)':{
	      "stream":"https://audioboom.com/channels/4581642.rss",
	      "image":"",
	      "name":"Meditation Minis Podcast"
	   },
	   r'(?i)(Meditation Oasis)':{
	      "stream":"http://meditationoasis.libsyn.com/rss",
	      "image":"",
	      "name":"Meditation Oasis"
	   },
	   r'(?i)(Men.+blazer)':{
	      "stream":"http://feeds.feedburner.com/MenInBlazers",
	      "image":"",
	      "name":"Men In Blazers"
	   },
	   r'(?i)(Mental Illness Happy Hour)':{
	      "stream":"http://mentalpod.libsyn.com/rss",
	      "image":"",
	      "name":"Mental Illness Happy Hour"
	   },
	   r'(?i)(Mentors for Military)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:193038850/sounds.rss",
	      "image":"",
	      "name":"Mentors for Military Podcast"
	   },
	   r'(?i)(Met(t|)a Hour)|Sharon Salzberg':{
	      "stream":"http://mettahour.libsyn.com/rss",
	      "image":"",
	      "name":"Metta Hour with Sharon Salzberg"
	   },
	   r'(?i)(Mike and mike)':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=2445552",
	      "image":"",
	      "name":"Mike and Mike"
	   },
	   r'(?i)(Mind pump)':{
	      "stream":"http://artizen.audello.com/podcast/1/",
	      "image":"",
	      "name":"Mind Pump: Raw Fitness Truth"
	   },
	   r'(?i)(Mindful Living)':{
	      "stream":"http://mindfullivingspiritualawakening.libsyn.com/rss",
	      "image":"",
	      "name":"Mindful Living Spiritual Awakening"
	   },
	   r'(?i)(Mischief.+Managed)':{
	      "stream":"http://devonhyland.ca/mm/rss_feed.xml",
	      "image":"",
	      "name":"Mischief Managed Podcast - Your Recommended Dose of Harry Potter Nonsense"
	   },
	   r'(?i)(missing.+murdered)':{
	      "stream":"http://www.cbc.ca/podcasting/includes/missing.xml",
	      "image":"",
	      "name":"Missing and Murdered: Who Killed Alberta Williams?"
	   },
	   r'(?i)(mix(.|)er)':{
	      "stream":"https://mixergy.com/?feed=mixergy_feed&rss_source=itunes&",
	      "image":"",
	      "name":"Mixergy - Startup Stories with 1000+ entrepreneurs including founders of Wikipedia, Y Combinator, Pixar and more."
	   },
	   r'(?i)(money).+(rest).+(us)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:95405521/sounds.rss",
	      "image":"",
	      "name":"Money For the Rest of Us"
	   },
	   r'(?i)(money).+(girl)':{
	      "stream":"http://www.quickanddirtytips.com/money.xml",
	      "image":"",
	      "name":"Money Girl's Quick and Dirty Tips for a Richer Life"
	   },
	   r'(?i)(monster)(.+|)(cat)':{
	      "stream":"https://www.monstercat.com/podcast/feed.xml",
	      "image":"",
	      "name":"Monstercat Podcast"
	   },
	   r'(?i)(monster)(.+|)(talk)':{
	      "stream":"http://skeptic.libsyn.com/rss",
	      "image":"",
	      "name":"MonsterTalk"
	   },
	   r'(?i)(mosaic)|(erwin)':{
	      "stream":"http://feed.theplatform.com/f/IfSiAC/mqWRck66SwGc",
	      "image":"",
	      "name":"MOSAIC - Erwin Raphael McManus  (Audio)"
	   },
	   r'(?i)(mother).+(may).+(sleep)':{
	      "stream":"http://rss.acast.com/mothermayisleepwithpodcast",
	      "image":"",
	      "name":"Mother, May I Sleep With Podcast?"
	   },
	   r'(?i)(motley).+(fool)':{
	      "stream":"http://feeds2.feedburner.com/MotleyFoolMoney",
	      "image":"",
	      "name":"Motley Fool Money"
	   },
	   r'(?i)(Move.+Sticks)|(Daniel Jeremiah)|(buck.+brook)':{
	      "stream":"http://movethesticks.libsyn.com/rss",
	      "image":"",
	      "name":"Move the Sticks with Daniel Jeremiah & Bucky Brooks"
	   },
	   r'(?i)(MTG(.|)gold)|(magic.+gathering.+gold)':{
	      "stream":"https://www.mtggoldfish.com/podcasts/feed.rss",
	      "image":"",
	      "name":"MTGGoldfish Podcast"
	   },
	   r'(?i)(muggle)(.|)cast':{
	      "stream":"https://audioboom.com/channels/4855957.rss",
	      "image":"",
	      "name":"MuggleCast"
	   },
	   r'(?i)(muscle.+life)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:87377017/sounds.rss",
	      "image":"",
	      "name":"Muscle for Life"
	   },
	   r'(?i)((MWF|M.W.F).+motivation)':{
	      "stream":"http://mwfmotivation.libsyn.com/rss",
	      "image":"",
	      "name":"MWF Motivation Podcast"
	   },
	   r'(?i)(my.+bro.+me)':{
	      "stream":"http://mbmbam.libsyn.com/rss",
	      "image":"",
	      "name":"My Brother, My Brother And Me"
	   },
	   r'(?i)(seven.+cha)':{
	      "stream":"http://mysevenchakras7.libsyn.com/rss",
	      "image":"",
	      "name":"My Seven Chakras with Aditya"
	   },
	   r'(?i)(Myster.+bound)':{
	      "stream":"http://recordings.talkshoe.com/rss21864.xml",
	      "image":"",
	      "name":"Mysteries Abound"
	   },
	   r'(?i)(Myster.+univ)':{
	      "stream":"http://mysteriousuniverse.org/feed/podcast/",
	      "image":"",
	      "name":"Mysterious Universe"
	   },
	   r'(?i)^(Myster.+show)':{
	      "stream":"http://feeds.gimletmedia.com/mysteryshow",
	      "image":"",
	      "name":"Mystery Show"
	   },
	   r'(?i)^(Myster.+theat)':{
	      "stream":"http://mysterytheatre.rnn.beta.libsynpro.com/rss",
	      "image":"",
	      "name":"Mystery Theatre"
	   },
	   r'(?i)(naked.+astro)':{
	      "stream":"http://rss.acast.com/naked_astronomy_podcast",
	      "image":"",
	      "name":"Naked Astronomy"
	   },
	   r'(?i)(nat).+(thing)':{
	      "stream":"http://wrvo.org/podcasts/15101/rss.xml",
	      "image":"",
	      "name":"Nature of Things"
	   },
	   r'(?i)(nature).+(podcast)':{
	      "stream":"http://rss.acast.com/nature",
	      "image":"",
	      "name":"Nature Podcast"
	   },
	   r'(?i)(NBA).+(lock)':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=3634017",
	      "image":"",
	      "name":"NBA Lockdown"
	   },
	   r'(?i)(near).+(east)':{
	      "stream":"http://www.washingtoninstitute.org/podcast/",
	      "image":"",
	      "name":"Near East Policycast"
	   },
	   r'(?i)(new).+(eng).+journal.+this.+week':{
	      "stream":"http://feeds.feedburner.com/nejm-this-week-audio-summaries",
	      "image":"",
	      "name":"New England Journal of Medicine This Week - Audio Summaries"
	   },
	   r'(?i)(new).+(eng).+journal.+inter':{
	      "stream":"http://podcast.nejm.org/nejm_audio_interview.xml",
	      "image":"",
	      "name":"New England Journal of Medicine Interviews"
	   },
	   r'(?i)(new).+(york).+mag.+sex':{
	      "stream":"http://feeds.feedburner.com/NewYorkMagazinesSexLives",
	      "image":"",
	      "name":"New York Magazine's Sex Lives"
	   },
	   r'(?i)(new).+(york).+out':{
	      "stream":"http://www.newyorker.com/feed/podcast/out-loud",
	      "image":"",
	      "name":"New Yorker: Out Loud"
	   },
	   r'(?i)(NFL).+(fantasy).+live':{
	      "stream":"http://nflfantasy.libsyn.com/rss",
	      "image":"",
	      "name":"NFL Fantasy Live"
	   },
	   r'(?i)(Dave.+Dameshek)':{
	      "stream":"http://dameshek.libsyn.com/rss",
	      "image":"",
	      "name":"NFL: The Dave Dameshek Football Program"
	   },
	   r'(?i)(nintendo.+voice)':{
	      "stream":"http://feeds.ign.com/ignfeeds/podcasts/wii/",
	      "image":"",
	      "name":"Nintendo Voice Chat"
	   },
	   r'(?i)(no.+guitar.+safe)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:162332893/sounds.rss",
	      "image":"",
	      "name":"No Guitar Is Safe"
	   },
	   r'(?i)(no.+jump)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:154009125/sounds.rss",
	      "image":"",
	      "name":"No Jumper"
	   },
	   r'(?i)(no.+laying.+up)':{
	      "stream":"http://feeds.feedburner.com/NLUpodcasts",
	      "image":"",
	      "name":"No Laying Up - Golf Podcast"
	   },
	   r'(?i)(no.+meat.+ath)':{
	      "stream":"http://nomeatathleteradio.libsyn.com/rss",
	      "image":"",
	      "name":"No Meat Athlete Radio"
	   },
	   r'(?i)(no.+such.+thin).+(fish)':{
	      "stream":"https://audioboom.com/channels/2399216.rss",
	      "image":"",
	      "name":"No Such Thing As A Fish"
	   },
	   r'(?i)(non(.|)profit.+messy)':{
	      "stream":"http://www.joangarry.com/feed/podcast",
	      "image":"",
	      "name":"Nonprofits Are Messy: Lessons in Leadership | Fundraising | Board Development | Communications"
	   },
	   r'(?i)(Norm.+mac)':{
	      "stream":"http://norm.videopodcastnetwork.libsynpro.com/rss",
	      "image":"",
	      "name":"Norm Macdonald Live"
	   },
	   r'(?i)((Norml|normal).+weekly)':{
	      "stream":"http://norml.org/rss/normlnews_podcast.xml",
	      "image":"",
	      "name":"NORML Weekly News Podcast"
	   },
	   r'(?i)((north).+molly)':{
	      "stream":"http://feeds.feedburner.com/NorthMollywood",
	      "image":"",
	      "name":"North Mollywood"
	   },
	   r'(?i)((north).+point).+(comm)':{
	      "stream":"http://feeds.feedburner.com/WeeklyPodcastNorthPoint",
	      "image":"",
	      "name":"North Point Community Church"
	   },
	   r'(?i)((stand).+dev)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:174789515/sounds.rss",
	      "image":"",
	      "name":"Not So Standard Deviations"
	   },
	   r'(?i)((not).+deep)|(grace.+(helbig|hell big))':{
	      "stream":"http://feeds.feedburner.com/NotTooDeepWithGraceHelbig",
	      "image":"",
	      "name":"Not Too Deep with Grace Helbig"
	   },
	   r'(?i)(Notes.+Spanish.+adv)':{
	      "stream":"http://notesinspanish.libsyn.com/rss",
	      "image":"",
	      "name":"Notes in Spanish Advanced"
	   },
	   r'(?i)(Notes.+Spanish.+int)':{
	      "stream":"http://intnotesinspanish.libsyn.com/rss",
	      "image":"",
	      "name":"Notes in Spanish Intermediate"
	   },
	   r'(?i)(Nouman Ali Khan)':{
	      "stream":"http://www.muslimcentral.com/audio/nouman-ali-khan/feed/",
	      "image":"",
	      "name":"Nouman Ali Khan"
	   },
	   r'(?i)^(NOVA)$':{
	      "stream":"http://www.pbs.org/wgbh/nova/rss/nova-podcast.xml",
	      "image":"",
	      "name":"NOVA"
	   },
	   r'(?i)(Nova science(.|)now)':{
	      "stream":"http://feeds.pbs.org/pbs/wgbh/nova/nsn-audio",
	      "image":"",
	      "name":"NOVA scienceNOW"
	   },
	   r'(?i)(now.+play)':{
	      "stream":"http://podcast.nowplayingpodcast.com/feed/",
	      "image":"",
	      "name":"Now Playing - The Movie Review Podcast"
	   },
	   r'(?i)((NPR|N.P.R).+mount.+stage)':{
	      "stream":"http://feedpress.me/mountainstagepodcast",
	      "image":"",
	      "name":"NPR's Mountain Stage"
	   },
	   r'(?i)(off camera)|(sam jones)':{
	      "stream":"http://feeds.feedburner.com/OffCameraWithSamJones",
	      "image":"",
	      "name":"Off Camera with Sam Jones"
	   },
	   r'(?i)(off topic)':{
	      "stream":"http://achievementhunter.roosterteeth.com/show/off-topic-the-achievement-hunter-podcast/feed/mp3",
	      "image":"",
	      "name":"Off Topic"
	   },
	   r'(?i)(off.+play)':{
	      "stream":"http://playstation.libsyn.com/rss",
	      "image":"",
	      "name":"Official PlayStation Blogcast"
	   },
	   r'(?i)(off(.|)shore)':{
	      "stream":"http://feeds.civilbeat.org/civilbeatoffshore",
	      "image":"",
	      "name":"OFFSHORE"
	   },
	   r'(?i)(oh.no)':{
	      "stream":"http://feeds.feedburner.com/OhNoPodcast",
	      "image":"",
	      "name":"Oh No Ross and Carrie"
	   },
	   r'(?i)(Old.+Time.+Radio.+Myster.+Theat)':{
	      "stream":"http://www.mysteryshows.com/Podcasts/Mystery-Shows-Feed.xml",
	      "image":"",
	      "name":"Old Time Radio Mystery Theater"
	   },
	   r'(?i)(On.+the.+media)':{
	      "stream":"http://feeds.wnyc.org/onthemedia",
	      "image":"",
	      "name":"On the Media"
	   },
	   r'(?i)(On.+viol.+Extre)':{
	      "stream":"http://feeds.feedburner.com/OnViolentExtremism",
	      "image":"",
	      "name":"On Violent Extremism"
	   },
	   r'(?i)(One.+chur)':{
	      "stream":"http://onechurchla.org/feed/podcast/",
	      "image":"",
	      "name":"One Church LA"
	   },
	   r'(?i)(One.shot)':{
	      "stream":"http://oneshotpodcast.com/category/one-shot/one-shot-podcast/feed/",
	      "image":"",
	      "name":"One Shot"
	   },
	   r'(?i)(Amy.+Porter)|(online.+market.+made)':{
	      "stream":"http://www.amyporterfield.com/feed/podcast/?wpmfeedkey=42",
	      "image":"",
	      "name":"Online Marketing Made Easy with Amy Porterfield"
	   },
	   r'(?i)(only.+game)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510052",
	      "image":"",
	      "name":"Only A Game"
	   },
	   r'(?i)(only.+human)':{
	      "stream":"http://feeds.wnyc.org/only-human",
	      "image":"",
	      "name":"Only Human"
	   },
	   r'(?i)(only.+stupid.+answer)':{
	      "stream":"https://audioboom.com/channels/4828446.rss",
	      "image":"",
	      "name":"Only Stupid Answers"
	   },
	   r'(?i)(open.+mind)':{
	      "stream":"http://www.blogtalkradio.com/ufo_radio/podcast",
	      "image":"",
	      "name":"Open Minds UFO Radio"
	   },
	   r'(?i)(open.+source)|(chris.+L[yi]d)':{
	      "stream":"http://radioopensource.org/feed/",
	      "image":"",
	      "name":"Open Source with Christopher Lydon"
	   },
	   r'(?i)(oper.+self.+reset)':{
	      "stream":"http://www.operationselfreset.com/feed/podcast/",
	      "image":"",
	      "name":"Operation Self Reset"
	   },
	   r'(?i)(Optimal.+Fin.+Daily)':{
	      "stream":"http://optimalfinancedaily.libsyn.com/rss",
	      "image":"",
	      "name":"Optimal Finance Daily: The Best Of Personal Finance | Minimalism | Investing"
	   },
	   r'(?i)(Optimal.+liv.+Daily)':{
	      "stream":"http://optimallivingdaily.libsyn.com/rss",
	      "image":"",
	      "name":"Optimal Living Daily"
	   },
	   r'(?i)(Orbit.+path)':{
	      "stream":"http://feeds.prx.org/orbitalpath",
	      "image":"",
	      "name":"Orbital Path"
	   },
	   r'(?i)(Order.+man)':{
	      "stream":"http://orderofman.libsyn.com/rss",
	      "image":"",
	      "name":"Order of Man: Finance | Fitness | Leadership | Manly Skills | Relationships | Self-Mastery | Style"
	   },
	   r'(?i)(Out West)':{
	      "stream":"http://feeds.feedburner.com/outwestpodcast",
	      "image":"",
	      "name":"Out West: Westworld Fan Theories, Dissected"
	   },
	   r'(?i)(Out(.|)kick).+show|(clay travis)':{
	      "stream":"http://feeds.feedburner.com/Outkick",
	      "image":"",
	      "name":"Outkick The Show with Clay Travis"
	   },
	   r'(?i)(Out(.|)side)':{
	      "stream":"http://podcast.outsideonline.com/OutsidePodcast",
	      "image":"",
	      "name":"Outside Podcast"
	   },
	   r'(?i)(Over.+it).+(with)':{
	      "stream":"http://overitandonwithit.libsyn.com/rss",
	      "image":"",
	      "name":"Over It And On With It"
	   },
	   r'(?i)(Over(.|)watchers)':{
	      "stream":"http://feeds.feedburner.com/overwatchers",
	      "image":"",
	      "name":"Overwatchers: The Overwatch Podcast"
	   },
	   r'(?i)(pale(.|)(OMG|O.M.G|Oh My God)).+uncens':{
	      "stream":"http://paleomg.com/feed/podcast/",
	      "image":"",
	      "name":"PaleOMG Uncensored"
	   },
	   r'(?i)(parent(.|)cast)':{
	      "stream":"http://feeds.feedburner.com/parentcast",
	      "image":"",
	      "name":"ParentCast"
	   },
	   r'(?i)(Parenting.+Beyond.+Disc)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:209924999/sounds.rss",
	      "image":"",
	      "name":"Parenting Beyond Discipline"
	   },
	   r'(?i)(Parenting.+great.+kid)|(Meg Meeker)':{
	      "stream":"http://megmeeker.megmeekerpodcast.libsynpro.com/rss",
	      "image":"",
	      "name":"Parenting Great Kids with Dr. Meg Meeker"
	   },
	   r'(?i)(Parenting.+on.+purpo)':{
	      "stream":"http://parentingonpurpose.org/podcast.ashx",
	      "image":"",
	      "name":"Parenting On Purpose (Parenting On Purpose)"
	   },
	   r'(?i)(partial.+Deri)':{
	      "stream":"http://feeds.feedburner.com/PartiallyDerivative",
	      "image":"",
	      "name":"Partially Derivative"
	   },
	   r'(?i)(pass.+city)':{
	      "stream":"http://feeds.feedburner.com/PassionCityChurchPodcast",
	      "image":"",
	      "name":"Passion City Church Podcast"
	   },
	   r'(?i)(past.+rick)':{
	      "stream":"http://feeds.feedburner.com/DailyHopeWithRickWarrenPodcast",
	      "image":"",
	      "name":"Pastor Rick's Daily Hope"
	   },
	   r'(?i)(pc.+game)':{
	      "stream":"http://www.pcgamer.com/spark_podcast/2/",
	      "image":"",
	      "name":"PC Gamer"
	   },
	   r'(?i)(pea.in.the.pod)':{
	      "stream":"http://feeds.feedburner.com/peainthepodcast",
	      "image":"",
	      "name":"Pea In The Podcast"
	   },
	   r'(?i)(Perm(.|)cult).+voice':{
	      "stream":"http://feeds.feedburner.com/PermacultureVoicesPodcast",
	      "image":"",
	      "name":"Permaculture Voices: Profitable and Practical Permaculture - Focusing on Farming, Business, Design"
	   },
	   r'(?i)(Personal.+growth)':{
	      "stream":"http://feeds.feedburner.com/PersonalGrowthPodcast",
	      "image":"",
	      "name":"Personal Growth Podcast"
	   },
	   r'(?i)(Person.+hack)':{
	      "stream":"http://feeds.feedburner.com/PersonalityHackerPodcast",
	      "image":"",
	      "name":"Personality Hacker Podcast"
	   },
	   r'(?i)(Peta)':{
	      "stream":"http://www.peta.org/scripts/podcast.xml",
	      "image":"",
	      "name":"PETA's Podcast"
	   },
	   r'(?i)(Peter King)':{
	      "stream":"http://feeds.feedburner.com/the-mmqb-king",
	      "image":"",
	      "name":"Peter King, The MMQB Podcast"
	   },
	   r'(?i)(Phil.+This)':{
	      "stream":"http://philosophizethis.libsyn.com/rss",
	      "image":"",
	      "name":"Philosophize This!"
	   },
	   r'(?i)(Phil.+(byte|bite))':{
	      "stream":"http://philosophybites.libsyn.com/rss",
	      "image":"",
	      "name":"Philosophy Bites"
	   },
	   r'(?i)((Phish|fish)(.|)cast)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:271543223/sounds.rss",
	      "image":"",
	      "name":"PhishCast"
	   },
	   r'(?i)(Physician Assistant Board)':{
	      "stream":"http://physicianassistantboards.libsyn.com/rss",
	      "image":"",
	      "name":"Physician Assistant Boards Podcast: Exam Review | Medicine | PANCE Preparation |"
	   },
	   r'(?i)(Physician Assistant Exam)':{
	      "stream":"http://feeds.feedburner.com/physicianassistantexamreviewpodcasts",
	      "image":"",
	      "name":"Physician Assistant Exam Review"
	   },
	   r'(?i)(Piano.+jazz)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510056",
	      "image":"",
	      "name":"Piano Jazz Shorts"
	   },
	   r'(?i)(planet.+radio)':{
	      "stream":"http://www.planetary.org/multimedia/podcasts/planetary-radio-podcast-rss.xml",
	      "image":"",
	      "name":"Planetary Radio: Space Exploration, Astronomy and Science"
	   },
	   r'(?i)(please.+finish).+book':{
	      "stream":"http://www.pleasefinishyourbook.com/feed/podcast",
	      "image":"",
	      "name":"Please, Finish Your Book!"
	   },
	   r'(?i)(pod.+beyond)':{
	      "stream":"http://feeds.ign.com/ignfeeds/podcasts/beyond/",
	      "image":"",
	      "name":"Podcast Beyond"
	   },
	   r'(?i)(pod.+unlock)':{
	      "stream":"http://feeds.ign.com/ignfeeds/podcasts/xbox360/",
	      "image":"",
	      "name":"Podcast Unlocked"
	   },
	   r'(?i)(point.+inquiry)':{
	      "stream":"http://pointofinquiry.libsyn.com/rss",
	      "image":"",
	      "name":"Point of Inquiry"
	   },
	   r'(?i)(police.+mag)':{
	      "stream":"http://feeds2.feedburner.com/POLICE-Podcasts?format=xml",
	      "image":"",
	      "name":"POLICE Magazine - Podcasts"
	   },
	   r'(?i)(police.+radio)':{
	      "stream":"http://americaoutloud.com/feed/police-radio/",
	      "image":"",
	      "name":"POLICE RADIO"
	   },
	   r'(?i)(polic.+matter)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:174823287/sounds.rss",
	      "image":"",
	      "name":"Policing Matters"
	   },
	   r'(?i)(politic.+politic)':{
	      "stream":"http://feeds.feedburner.com/squarespace/WtCx",
	      "image":"",
	      "name":"Politics Politics Politics"
	   },
	   r'(?i)(polygon.+qual.+control)':{
	      "stream":"http://feeds.feedburner.com/polygonqualitycontrol",
	      "image":"",
	      "name":"Polygon's Quality Control"
	   },
	   r'(?i)(pop.+cult.+happy)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510282",
	      "image":"",
	      "name":"Pop Culture Happy Hour"
	   },
	   r'(?i)^(pop(.|)cast)$':{
	      "stream":"https://feeds.podtrac.com/_-sJYvsFQrn_",
	      "image":"",
	      "name":"Popcast"
	   },
	   r'(?i)(potter(.|)cast)':{
	      "stream":"http://pottercast.libsyn.com/rss",
	      "image":"",
	      "name":"PotterCast - The Harry Potter Podcast"
	   },
	   r'(?i)(power.+purp)':{
	      "stream":"http://powerandpurpose.libsyn.com/rss",
	      "image":"",
	      "name":"Power and Purpose With Mastin Kipp"
	   },
	   r'(?i)(power.+mom)':{
	      "stream":"http://powerofmoms.libsyn.com/rss",
	      "image":"",
	      "name":"Power of Moms Radio"
	   },
	   r'(?i)(power.+trad)':{
	      "stream":"http://powertradingradio.libsyn.com/rss",
	      "image":"",
	      "name":"Power Trading Radio - A Trader's Perspective on Investing in Stocks, Futures, Forex, Options Podcast"
	   },
	   r'(?i)(prec.+sleep)':{
	      "stream":"https://www.preciouslittlesleep.com/feed/podcast/",
	      "image":"",
	      "name":"Precious Little Sleep Parenting Podcast"
	   },
	   r'(?i)(preg.+conf)':{
	      "stream":"http://feeds.feedburner.com/PregnancyConfidential",
	      "image":"",
	      "name":"Pregnancy Confidential"
	   },
	   r'(?i)^(president.+are.+people)':{
	      "stream":"http://audiblepapt.libsyn.com/rss",
	      "image":"",
	      "name":"Presidents Are People Too!"
	   },
	   r'(?i)(Primal.+blue)':{
	      "stream":"http://primalblueprint.libsyn.com/rss",
	      "image":"",
	      "name":"Primal Blueprint Podcast"
	   },
	   r'(?i)(Prob.+sci)':{
	      "stream":"http://probablyscience.libsyn.com/rss",
	      "image":"",
	      "name":"Probably Science"
	   },
	   r'(?i)(Prog.+throw)':{
	      "stream":"http://feeds.feedburner.com/ProgrammingThrowdown",
	      "image":"",
	      "name":"Programming Throwdown"
	   },
	   r'(?i)(PS.I.love)':{
	      "stream":"http://feeds.podtrac.com/nOTae4fRptyc",
	      "image":"",
	      "name":"PS I Love You XOXO"
	   },
	   r'(?i)(Psycho(.|)babble)|(Tyler Oakley)|(Korey Kuhl)':{
	      "stream":"http://feeds.podtrac.com/psychobabble",
	      "image":"",
	      "name":"Psychobabble with Tyler Oakley & Korey Kuhl"
	   },
	   r'(?i)(Psycho.+ill)':{
	      "stream":"http://psychsessions.com/feed/podcast/",
	      "image":"",
	      "name":"Psychology Illustrated: Psych Sessions Podcast"
	   },
	   r'(?i)(Psycho.+everyday)':{
	      "stream":"http://feeds.feedburner.com/thepsychfiles",
	      "image":"",
	      "name":"Psychology in Everyday Life: The Psych Files"
	   },
	   r'(?i)(pure.+(non.|)fiction)':{
	      "stream":"http://www.purenonfiction.net/feed/podcast/",
	      "image":"",
	      "name":"Pure Nonfiction: Inside Documentary Film"
	   },
	   r'(?i)(Quanta Science)':{
	      "stream":"http://www.quantamagazine.org/feed/podcast/",
	      "image":"",
	      "name":"Quanta Science Podcast"
	   },
	   r'(?i)(Quirks.+Quarks)':{
	      "stream":"http://www.cbc.ca/podcasting/includes/quirksaio.xml",
	      "image":"",
	      "name":"Quirks and Quarks Complete Show from CBC Radio"
	   },
	   r'(?i)((RA.|Resident Advis.+)Podcast)':{
	      "stream":"https://www.residentadvisor.net/xml/podcast.xml",
	      "image":"",
	      "name":"Resident Advisor Podcast"
	   },
	   r'(?i)(Rad.+ Pers.+Finance)':{
	      "stream":"http://radicalpersonalfinance.libsyn.com/rss",
	      "image":"",
	      "name":"Radical Personal Finance"
	   },
	   r'(?i)(Radio Ambulan)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510315",
	      "image":"",
	      "name":"Radio Ambulante"
	   },
	   r'(?i)(Rad.+ det.+story)':{
	      "stream":"http://detective.libsyn.com/rss",
	      "image":"",
	      "name":"Radio Detective Story Hour"
	   },
	   r'(?i)(Rad.+ head(.|)space)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:77542725/sounds.rss",
	      "image":"",
	      "name":"Radio Headspace"
	   },
	   r'(?i)(radio(.|)west)':{
	      "stream":"http://radiowest.kuer.org/podcasts/220/rss.xml",
	      "image":"",
	      "name":"RadioWest Podcasts"
	   },
	   r'(?i)(ram dass)|(here .+ now)':{
	      "stream":"http://ramdasshereandnow.libsyn.com/rss",
	      "image":"",
	      "name":"Ram Dass Here And Now"
	   },
	   r'(?i)(rap).+radar':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1327?format=MP3_128K",
	      "image":"",
	      "name":"Rap Radar Podcast"
	   },
	   r'(?i)(read).+script':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:158340237/sounds.rss",
	      "image":"",
	      "name":"Read Scripture Podcast Series"
	   },
	   r'(?i)(read).+loud.+rev':{
	      "stream":"https://amongstlovelythings.com/feed/podcast/",
	      "image":"",
	      "name":"Read-Aloud Revival"
	   },
	   r'(?i)(real).+crime.+prof':{
	      "stream":"http://rss.art19.com/real-crime-profile",
	      "image":"",
	      "name":"Real Crime Profile"
	   },
	   r'(?i)(real).+Deal':{
	      "stream":"http://www.iradeo.com/113248/feed/143029.xml",
	      "image":"",
	      "name":"Real Deal Music Radio"
	   },
	   r'(?i)(real).+estate.+new':{
	      "stream":"http://realestatenews.libsyn.com/rss",
	      "image":"",
	      "name":"Real Estate News"
	   },
	   r'(?i)(real).+ghost.+stor':{
	      "stream":"https://audioboom.com/channels/4567086.rss",
	      "image":"",
	      "name":"Real Ghost Stories Online"
	   },
	   r'(?i)(real).+(Byte|bite)|Stephanie Beatriz|Courtney Kocak':{
	      "stream":"http://realitybytespod.videopodcastnetwork.libsynpro.com/rss",
	      "image":"",
	      "name":"Reality Bytes with Stephanie Beatriz & Courtney Kocak"
	   },
	   r'(?i)(reason).+(doubt)':{
	      "stream":"http://feeds.feedburner.com/CarollaReasonableDoubt",
	      "image":"",
	      "name":"Reasonable Doubt"
	   },
	   r'(?i)(rebel).+(FM|F.M)':{
	      "stream":"http://rebelfm.libsyn.com/rss",
	      "image":"",
	      "name":"Rebel FM"
	   },
	   r'(?i)(rebel).+(force)':{
	      "stream":"http://rebelforceradio.libsyn.com/rss",
	      "image":"",
	      "name":"Rebel Force Radio: Star Wars Podcast"
	   },
	   r'(?i)(reclaim).+(audio)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:184343600/sounds.rss",
	      "image":"",
	      "name":"Reclaimed Audio Podcast"
	   },
	   r'(?i)(recode).+(decode)':{
	      "stream":"http://feeds.feedburner.com/Recode-Decode",
	      "image":"",
	      "name":"Recode Decode, hosted by Kara Swisher"
	   },
	   r'(?i)(recode).+(media)|Peter Kafka':{
	      "stream":"http://feeds.feedburner.com/Recode-Media",
	      "image":"",
	      "name":"Recode Media with Peter Kafka"
	   },
	   r'(?i)(I Do Podcast)':{
	      "stream":"http://idopodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Relationships, Sex, Dating and Marriage Advice - I Do Podcast"
	   },
	   r'(?i)(RELEVANT)':{
	      "stream":"http://www.relevantmagazine.com/taxonomy/term/79/feed",
	      "image":"",
	      "name":"RELEVANT Podcast"
	   },
	   r'(?i)(Renew).+you.+mind|R.C. Sproul':{
	      "stream":"http://feeds.ligonier.org/RenewingYourMind",
	      "image":"",
	      "name":"Renewing Your Mind with R.C. Sproul"
	   },
	   r'(?i)(residual).+income':{
	      "stream":"http://residualincomepodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Residual Income Podcast"
	   },
	   r'(?i)Janet Lansbury|Unruffled':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:91056977/sounds.rss",
	      "image":"",
	      "name":"Respectful Parenting: Janet Lansbury Unruffled"
	   },
	   r'(?i)Retro(.|)(naut|not)':{
	      "stream":"http://retronauts.libsyn.com/rss",
	      "image":"",
	      "name":"Retronauts"
	   },
	   r'(?i)reverb.+ radio':{
	      "stream":"http://feeds.feedburner.com/ReverberationRadio",
	      "image":"",
	      "name":"Reverberation Radio"
	   },
	   r'(?i)Revive Our Hearts|Nancy.+Wolgemuth':{
	      "stream":"http://www.reviveourhearts.com/podcasts/revive-our-hearts.rss",
	      "image":"",
	      "name":"Revive Our Hearts with Nancy DeMoss Wolgemuth"
	   },
	   r'(?i)rev.+health':{
	      "stream":"http://chriskresser.com/feed/podcast",
	      "image":"",
	      "name":"Revolution Health Radio"
	   },
	   r'(?i)revolutions':{
	      "stream":"http://revolutionspodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Revolutions"
	   },
	   r'(?i)re(.|)wild.+your':{
	      "stream":"http://rewildyourself.libsyn.com/rss",
	      "image":"",
	      "name":"ReWild Yourself"
	   },
	   r'(?i)rich.+dad.+radio':{
	      "stream":"http://richdadradio.libsyn.com/rss",
	      "image":"",
	      "name":"Rich Dad Radio Show: In-Your-Face Advice on Investing, Personal Finance, & Starting a Business"
	   },
	   r'(?i)rick.+warr.+mini':{
	      "stream":"http://feeds.feedburner.com/RickWarrensMinistryPodcastShow",
	      "image":"",
	      "name":"Rick Warren's Ministry Podcast"
	   },
	   r'(?i)ring.+uni':{
	      "stream":"http://feeds.feedburner.com/RingerUniversity",
	      "image":"",
	      "name":"Ringer University"
	   },
	   r'(?i)risk.+busin':{
	      "stream":"http://risky.biz/feeds/risky-business",
	      "image":"",
	      "name":"Risky Business"
	   },
	   r'(?i)rob.+has.+a ':{
	      "stream":"http://feeds.feedburner.com/RobCesternino",
	      "image":"",
	      "name":"Rob Has a Podcast"
	   },
	   r'(?i)Rob.+Wolf|Paleo Solution':{
	      "stream":"http://robbwolf.libsyn.com/rss",
	      "image":"",
	      "name":"Robb Wolf - The Paleo Solution Podcast - Paleo diet, nutrition, fitness, and health"
	   },
	   r'(?i)Rolling.+stone.+music':{
	      "stream":"http://feeds.megaphone.fm/rollingstonemusicnow",
	      "image":"",
	      "name":"Rolling Stone Music Now"
	   },
	   r'(?i)Roost.+teeth':{
	      "stream":"http://roosterteeth.com/show/rt-podcast/feed/mp3",
	      "image":"",
	      "name":"Rooster Teeth Podcast"
	   },
	   r'(?i)Rose.+bud':{
	      "stream":"http://rosebuddies.libsyn.com/rss",
	      "image":"",
	      "name":"Rose Buddies"
	   },
	   r'(?i)Roto(.|)Grind':{
	      "stream":"https://rotogrinders.com/podcasts.rss",
	      "image":"",
	      "name":"RotoGrinders Daily Fantasy Fix"
	   },
	   r'(?i)Rule.+break.+invest':{
	      "stream":"http://rulebreakerinvesting.libsyn.com/rss",
	      "image":"",
	      "name":"Rule Breaker Investing"
	   },
	   r'(?i)What.+The Tee|Michelle Visage':{
	      "stream":"http://rupaul.libsyn.com/rupaul.rss",
	      "image":"",
	      "name":"RuPaul: What's The Tee? with Michelle Visage"
	   },
	   r'(?i)Russ.+Kane':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=3028618",
	      "image":"",
	      "name":"Russillo and Kanell"
	   },
	   r'(?i)just.+think':{
	      "stream":"http://rzim.org/just-thinking-broadcasts/feed/",
	      "image":"",
	      "name":"RZIM: Just Thinking Broadcasts"
	   },
	   r'(?i)saddle(.|)back.+church':{
	      "stream":"http://mediacenter.saddleback.com/mc/podcaststream.aspx?p=1&iid=-1&site=1",
	      "image":"",
	      "name":"Saddleback Church Weekend Messages"
	   },
	   r'(?i)Sam.Robert.+wrestling':{
	      "stream":"http://samrobertswrestling.libsyn.com/rss",
	      "image":"",
	      "name":"Sam Roberts Wrestling Podcast"
	   },
	   r'(?i)Sampler':{
	      "stream":"http://feeds.gimletmedia.com/samplershow",
	      "image":"",
	      "name":"Sampler"
	   },
	   r'(?i)Sasquatch.+Chronic':{
	      "stream":"http://www.blogtalkradio.com/bigfoothotspot/podcast",
	      "image":"",
	      "name":"Sasquatch Chronicles"
	   },
	   r'(?i)Sasquatch.+Synd':{
	      "stream":"http://podcast.sasquatchsyndicate.com/rss",
	      "image":"",
	      "name":"Sasquatch Syndicate"
	   },
	   r'(?i)savage.+love':{
	      "stream":"http://savagelove.libsyn.com/rss",
	      "image":"",
	      "name":"Savage Lovecast"
	   },
	   r'(?i)saw(.|)bone':{
	      "stream":"http://sawbones.libsyn.com/rss",
	      "image":"",
	      "name":"Sawbones: A Marital Tour of Misguided Medicine"
	   },
	   r'(?i)no.+jargon':{
	      "stream":"http://nojargon.libsyn.com/rss",
	      "image":"",
	      "name":"Scholars Strategy Network's No Jargon"
	   },
	   r'(?i)sci.+in.+action':{
	      "stream":"http://www.bbc.co.uk/programmes/p002vsnb/episodes/downloads.rss",
	      "image":"",
	      "name":"Science in Action"
	   },
	   r'(?i)sci.+mag':{
	      "stream":"http://www.sciencemag.org/rss/podcast.xml",
	      "image":"",
	      "name":"Science Magazine Podcast"
	   },
	   r'(?i)sci.+ talk':{
	      "stream":"https://www.scientificamerican.com/sciam/xml/iTunes.cfm?id=science-talk",
	      "image":"",
	      "name":"Science Talk"
	   },
	   r'(?i)sci.+sort.+of':{
	      "stream":"http://sciencesortof.libsyn.com/rss",
	      "image":"",
	      "name":"Science... sort of"
	   },
	   r'(?i)screen(.|)junk':{
	      "stream":"http://api.breakmedia.com/content/contentfeed/get?apiRequestJson=%7bid:1179,pageNumber:1,pageSize:52,responseType:%22itunespodcastrss%22%7d",
	      "image":"",
	      "name":"ScreenJunkies Movie Fights"
	   },
	   r'(?i)script(.|)note':{
	      "stream":"http://scriptnotes.net/rss",
	      "image":"",
	      "name":"Scriptnotes Podcast"
	   },
	   r'(?i)Secular.+bud':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:196546667/sounds.rss",
	      "image":"",
	      "name":"Secular Buddhism"
	   },
	   r'(?i)Sec.+now':{
	      "stream":"http://feeds.twit.tv/sn.xml",
	      "image":"",
	      "name":"Security Now (MP3)"
	   },
	   r'(?i)See.+something|say.+something':{
	      "stream":"http://rss.acast.com/seesomethingsaysomething",
	      "image":"",
	      "name":"See Something Say Something"
	   },
	   r'(?i)^select.+shorts$':{
	      "stream":"http://feeds.feedburner.com/Selected-Shorts",
	      "image":"",
	      "name":"Selected Shorts"
	   },
	   r'(?i)selected.+short.+to.+hot':{
	      "stream":"http://feeds.feedburner.com/TooHotForRadio",
	      "image":"",
	      "name":"Selected Shorts: Too Hot For Radio"
	   },
	   r'(?i)self.+made.+m[ae]n':{
	      "stream":"http://selfmademan.libsyn.com/rss",
	      "image":"",
	      "name":"Self Made Man"
	   },
	   r'(?i)self.+suff.+life':{
	      "stream":"http://www.theselfsufficientlife.com/feed/podcast/",
	      "image":"",
	      "name":"Self-Sufficient Life"
	   },
	   r'(?i)serendipity':{
	      "stream":"http://feeds.feedburner.com/libsyn/vbTa",
	      "image":"",
	      "name":"Serendipity"
	   },
	   r'(?i)sermon of the day':{
	      "stream":"http://feed.desiringgod.org/sermon-of-the-day.rss",
	      "image":"",
	      "name":"Sermon of the Day"
	   },
	   r'(?i)Seth.+Startup.+School':{
	      "stream":"http://rss.earwolf.com/startup-school",
	      "image":"",
	      "name":"Seth Godin's Startup School"
	   },
	   r'(?i)Sex.+Get.+Real':{
	      "stream":"http://sexgetsreal.libsyn.com/rss",
	      "image":"",
	      "name":"Sex Gets Real: Talking Sex, Relationships, and Kink with Dawn Serra"
	   },
	   r'(?i)Sex.+nerd':{
	      "stream":"http://rss.art19.com/sex-nerd-sandra.xml",
	      "image":"",
	      "name":"Sex Nerd Sandra"
	   },
	   r'(?i)Sex.+emily':{
	      "stream":"http://emilymorse.libsyn.com/rss",
	      "image":"",
	      "name":"Sex With Emily"
	   },
	   r'(?i)sherlock':{
	      "stream":"http://sherlock.libsyn.com/rss",
	      "image":"",
	      "name":"Sherlock Holmes Adventures"
	   },
	   r'(?i)side.+hustle.+pro':{
	      "stream":"http://sidehustlepro.libsyn.com/rss",
	      "image":"",
	      "name":"Side Hustle Pro: Female Entrepreneurs | Black Women Business Owners | Sidepreneurs"
	   },
	   r'(?i)side(.|)door':{
	      "stream":"http://feeds.podtrac.com/Q2-QW4_lLftD",
	      "image":"",
	      "name":"Sidedoor"
	   },
	   r'(?i)Silent Sales Machine':{
	      "stream":"http://silentsalesmachine.libsyn.com/rss",
	      "image":"",
	      "name":"Silent Sales Machine Radio"
	   },
	   r'(?i)Sin(.|)cast':{
	      "stream":"http://cinemasins.libsyn.com/rss",
	      "image":"",
	      "name":"SinCast - Presented by CinemaSins"
	   },
	   r'(?i)Skeptoid':{
	      "stream":"http://skeptoid.com/podcast.xml",
	      "image":"",
	      "name":"Skeptoid"
	   },
	   r'(?i)skip.+shannon|undisputed':{
	      "stream":"http://feeds.feedburner.com/SkipandShannonUndisputed",
	      "image":"",
	      "name":"Skip and Shannon: Undisputed"
	   },
	   r'(?i)slate.+money':{
	      "stream":"http://feeds.feedburner.com/SlateMoney",
	      "image":"",
	      "name":"Slate Money"
	   },
	   r'(?i)Lexicon.+Valley':{
	      "stream":"http://feeds.feedburner.com/SlateLexiconValley",
	      "image":"",
	      "name":"Slate Presents Lexicon Valley"
	   },
	   r'(?i)Slate.+Audio.+Book':{
	      "stream":"http://feeds.feedburner.com/SlateAudioBookClub",
	      "image":"",
	      "name":"Slate's Audio Book Club"
	   },
	   r'(?i)culture.+gab(.|)fest':{
	      "stream":"http://feeds.feedburner.com/SlateCultureGabfest",
	      "image":"",
	      "name":"Slate's Culture Gabfest"
	   },
	   r'(?i)Mom.+Dad.+Fighting':{
	      "stream":"http://feeds.feedburner.com/SlateMomAndDadAreFighting",
	      "image":"",
	      "name":"Slate's Mom and Dad Are Fighting"
	   },
	   r'(?i)sleep with silk':{
	      "stream":"http://feeds.feedburner.com/silknature",
	      "image":"",
	      "name":"Sleep with Silk: Nature Sounds (to help insomnia, anxiety, stress, relax, focus, meditate, ASMR)"
	   },
	   r'(?i)slow.+german':{
	      "stream":"http://feeds.schlaflosinmuenchen.com/slowsim.xml",
	      "image":"",
	      "name":"Slow German"
	   },
	   r'(?i)slumber Party':{
	      "stream":"http://feeds.feedburner.com/SlumberPartyWithAlieAndGeorgia",
	      "image":"",
	      "name":"Slumber Party With Alie and Georgia"
	   },
	   r'(?i)small.+town.+horror':{
	      "stream":"http://smalltownhorror.libsyn.com/rss",
	      "image":"",
	      "name":"Small Town Horror"
	   },
	   r'(?i)Smart Drug':{
	      "stream":"http://feeds.smartdrugsmarts.com/podcast/sds.xml",
	      "image":"",
	      "name":"Smart Drug Smarts: Brain Optimization | Nootropics | Neuroscience"
	   },
	   r'(?i)Smodcast':{
	      "stream":"http://feeds.feedburner.com/SModcasts",
	      "image":"",
	      "name":"SModcast"
	   },
	   r'(?i)Sneak attack':{
	      "stream":"http://sneakattack.libsyn.com/rss",
	      "image":"",
	      "name":"Sneak Attack!: A Dungeons and Dragons Adventure"
	   },
	   r'(?i)Snoop dog':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:213836126/sounds.rss",
	      "image":"",
	      "name":"Snoop Dogg's GGN Podcast"
	   },
	   r'(?i)So Money|Farnoosh Torabi':{
	      "stream":"http://feeds.megaphone.fm/somoney",
	      "image":"",
	      "name":"So Money with Farnoosh Torabi"
	   },
	   r'(?i)soft.+eng.+daily':{
	      "stream":"http://softwareengineeringdaily.com/feed/podcast/",
	      "image":"",
	      "name":"Software Engineering Daily"
	   },
	   r'(?i)software.+eng.+radio':{
	      "stream":"http://feeds.feedburner.com/se-radio",
	      "image":"",
	      "name":"Software Engineering Radio - The Podcast for Professional Software Developers"
	   },
	   r'(?i)sounds off':{
	      "stream":"http://solomonster.podbean.com/feed/",
	      "image":"",
	      "name":"Solomonster Sounds Off"
	   },
	   r'(?i)something.+wrestle|bruce.+prichard':{
	      "stream":"https://audioboom.com/channels/4792166.rss",
	      "image":"",
	      "name":"Something to Wrestle with Bruce Prichard"
	   },
	   r'(?i)song.+explode':{
	      "stream":"http://songexploder.libsyn.com/rss",
	      "image":"",
	      "name":"Song Exploder"
	   },
	   r'(?i)so.+many.+white':{
	      "stream":"http://feeds.wnyc.org/sooomanywhiteguys",
	      "image":"",
	      "name":"Sooo Many White Guys"
	   },
	   r'(?i)so.+opinion':{
	      "stream":"http://feeds.feedburner.com/TheSoundOpinionsPodcast",
	      "image":"",
	      "name":"Sound Opinions"
	   },
	   r'(?i)Sound(.|)Cloud.+Commun':{
	      "stream":"http://feeds.feedburner.com/thisweekinsoundcloud",
	      "image":"",
	      "name":"SoundCloud Community"
	   },
	   r'(?i)Sound.+trail':{
	      "stream":"http://www.soundsofthetrail.com/?feed=podcast",
	      "image":"",
	      "name":"Sounds of the Trail"
	   },
	   r'(?i)Sound.+true':{
	      "stream":"http://www.soundstrue.com/podcast/feed/podcast/",
	      "image":"",
	      "name":"Sounds True: Insights at the Edge"
	   },
	   r'(?i)Spanish.+podcast':{
	      "stream":"http://newsinslowspanish.libsyn.com/rss",
	      "image":"",
	      "name":"Spanish Podcast"
	   },
	   r'(?i)Spare the Rock|spoil the child':{
	      "stream":"http://feeds.feedburner.com/stritunes",
	      "image":"",
	      "name":"Spare the Rock, Spoil the Child Playlists"
	   },
	   r'(?i)Spark.+stor':{
	      "stream":"http://sparklestories.libsyn.com/rss",
	      "image":"",
	      "name":"Sparkle Stories Podcast"
	   },
	   r'(?i)Spawned':{
	      "stream":"http://feeds.feedburner.com/SpawnedWithKristenAndLizOfCoolmompicks",
	      "image":"",
	      "name":"Spawned with Kristen and Liz of CoolMomPicks"
	   },
	   r'(?i)Speak.+Yourself':{
	      "stream":"http://feeds.feedburner.com/speak-for-yourself",
	      "image":"",
	      "name":"Speak For Yourself with Cowherd & Whitlock"
	   },
	   r'(?i)Speak.+forum':{
	      "stream":"http://kuow.org/podcasts/721/rss.xml",
	      "image":"",
	      "name":"Speakers Forum"
	   },
	   r'(?i)Speak.+psycho':{
	      "stream":"http://feeds.feedburner.com/SpeakingOfPsychology",
	      "image":"",
	      "name":"Speaking of Psychology"
	   },
	   r'(?i)Special Sauce|ed Levine':{
	      "stream":"http://seriouseats.libsyn.com/rss",
	      "image":"",
	      "name":"Special Sauce with Ed Levine"
	   },
	   r'(?i)Speed dial':{
	      "stream":"http://feeds.feedburner.com/SpeedDial",
	      "image":"",
	      "name":"Speed Dial"
	   },
	   r'(?i)Spirits':{
	      "stream":"http://spiritspodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Spirits"
	   },
	   r'(?i)spit.+chic':{
	      "stream":"http://feeds.feedburner.com/SpittinChiclets",
	      "image":"",
	      "name":"Spittin' Chiclets"
	   },
	   r'(?i)Paul.+Tompkins|SPONTANEANATION':{
	      "stream":"http://rss.earwolf.com/spontaneanation-with-paul-f-tompkins",
	      "image":"",
	      "name":"SPONTANEANATION with Paul F. Tompkins"
	   },
	   r'(?i)sports.+gambling':{
	      "stream":"http://www.spreaker.com/user/8206201/episodes/feed",
	      "image":"",
	      "name":"Sports Gambling Radio - By BangTheBook"
	   },
	   r'(?i)stack.+ben':{
	      "stream":"http://stackingbenjamins.libsyn.com/rss",
	      "image":"",
	      "name":"Stacking Benjamins: Earn, Save, and Spend Money With a Plan"
	   },
	   r'(?i)Stanford.+Inno.+lab|Tina Seelig':{
	      "stream":"http://ecorner.stanford.edu/StanfordInnovationLab.xml",
	      "image":"",
	      "name":"Stanford Innovation Lab with Tina Seelig"
	   },
	   r'(?i)Star.+war.+min':{
	      "stream":"http://feeds.feedburner.com/StarWarsMinute",
	      "image":"",
	      "name":"Star Wars Minute"
	   },
	   r'(?i)Start(.|)up podcast':{
	      "stream":"http://feeds.hearstartup.com/hearstartup",
	      "image":"",
	      "name":"StartUp Podcast"
	   },
	   r'(?i)Start(.|)up.+school.+radio':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:150759713/sounds.rss",
	      "image":"",
	      "name":"Startup School Radio"
	   },
	   r'(?i)Stem.+talk':{
	      "stream":"https://www.ihmc.us/stemtalk/feed/podcast/",
	      "image":"",
	      "name":"STEM-Talk"
	   },
	   r'(?i)still.+grow':{
	      "stream":"http://6ftmama.com/feed/podcast/",
	      "image":"",
	      "name":"Still Growing...A Weekly Gardening Podcast"
	   },
	   r'(?i)still.+process':{
	      "stream":"http://feeds.podtrac.com/LhS5ax2CPGou",
	      "image":"",
	      "name":"Still Processing"
	   },
	   r'(?i)still.+untitle|Adam Savage':{
	      "stream":"http://www.tested.com/podcast-xml/still-untitled-the-adam-savage-project/",
	      "image":"",
	      "name":"Still Untitled: The Adam Savage Project"
	   },
	   r'(?i)^Stories.Podcast$':{
	      "stream":"http://rss.art19.com/stories-podcast",
	      "image":"",
	      "name":"Stories Podcast"
	   },
	   r'(?i)Stor.+Star.+War':{
	      "stream":"http://feeds.feedburner.com/StoryAndStarWars",
	      "image":"",
	      "name":"Story and Star Wars"
	   },
	   r'(?i)Story(.|)Cor':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510200",
	      "image":"",
	      "name":"StoryCorps"
	   },
	   r'(?i)Story(.|)nor':{
	      "stream":"http://feeds.feedburner.com/Storynory",
	      "image":"",
	      "name":"Storynory - Stories for Kids"
	   },
	   r'(?i)Straight Up':{
	      "stream":"https://api.radio.com/v2/podcast/rss/1243?format=MP3_128K",
	      "image":"",
	      "name":"Straight Up with Stassi"
	   },
	   r'(?i)Stranger':{
	      "stream":"http://feeds.strangersnomore.org/StrangersNoMore",
	      "image":"",
	      "name":"Strangers"
	   },
	   r'(?i)Stronger Marriages|Anatomy of Marriage':{
	      "stream":"http://feeds.feedburner.com/AnatomyOfMarriage",
	      "image":"",
	      "name":"Stronger Marriages: Anatomy of Marriage"
	   },
	   r'(?i)Student.+Gun':{
	      "stream":"http://feeds.feedburner.com/StudentOfTheGunRadio",
	      "image":"",
	      "name":"Student of the Gun Radio"
	   },
	   r'(?i)studio (360|three sixty)|Kurt Andersen':{
	      "stream":"http://feeds.feedburner.com/studio360/podcast",
	      "image":"",
	      "name":"Studio 360 with Kurt Andersen"
	   },
	   r'(?i)Stuff.+Mom.+Never':{
	      "stream":"http://www.howstuffworks.com/podcasts/stuff-mom-never-told-you.rss",
	      "image":"",
	      "name":"Stuff Mom Never Told You"
	   },
	   r'(?i)stuff.+don(.|)t.+want':{
	      "stream":"http://www.howstuffworks.com/podcasts/stuff-they-dont-want-you-to-know-audio.rss",
	      "image":"",
	      "name":"Stuff They Don't Want You To Know Audio"
	   },
	   r'(?i)Stuff.+blow.+mind':{
	      "stream":"http://www.howstuffworks.com/podcasts/stuff-to-blow-your-mind.rss",
	      "image":"",
	      "name":"Stuff To Blow Your Mind"
	   },
	   r'(?i)Success talk':{
	      "stream":"http://successtalks.libsyn.com/rss",
	      "image":"",
	      "name":"SUCCESS Talks"
	   },
	   r'(?i)Sun.+Supp':{
	      "stream":"http://rss.acast.com/sundaysupplement",
	      "image":"",
	      "name":"Sunday Supplement - Sky Sports"
	   },
	   r'(?i)super.+best.+friend':{
	      "stream":"http://superbestfriendcast.libsyn.com/rss",
	      "image":"",
	      "name":"Super Best Friendcast!"
	   },
	   r'(?i)surpr.+awe':{
	      "stream":"http://feeds.gimletmedia.com/surprisinglyawesome",
	      "image":"",
	      "name":"Surprisingly Awesome"
	   },
	   r'(?i)survi.+mom':{
	      "stream":"http://survivalmomradio.libsyn.com/rss",
	      "image":"",
	      "name":"Survival Mom Podcast"
	   },
	   r'(?i)survi.+fan':{
	      "stream":"http://joannandstacy.libsyn.com/rss",
	      "image":"",
	      "name":"Survivor Fans Podcast"
	   },
	   r'(?i)Sustainable.+World':{
	      "stream":"http://pdcastsusworldradio.libsyn.com/rss",
	      "image":"",
	      "name":"Sustainable World Radio- Ecology and Permaculture Podcast"
	   },
	   r'(?i)Switch.+Pop':{
	      "stream":"http://feeds.feedburner.com/SwitchedOnPopPodcast",
	      "image":"",
	      "name":"Switched On Pop"
	   },
	   r'(?i)Tact.+Talk|Allison Barrie':{
	      "stream":"https://audioboom.com/channels/4854348.rss",
	      "image":"",
	      "name":"Tactical Talk with Allison Barrie"
	   },
	   r'(?i)Book Of The Day|Tai Lopez':{
	      "stream":"http://thetailopezshow.libsyn.com/rss",
	      "image":"",
	      "name":"Tai Lopez Book Of The Day Show"
	   },
	   r'(?i)Tale.+Horror':{
	      "stream":"http://horrortales.libsyn.com/rss",
	      "image":"",
	      "name":"Tales of Horror Podcast"
	   },
	   r'(?i)Talk.+pyth':{
	      "stream":"https://talkpython.fm/episodes/rss",
	      "image":"",
	      "name":"Talk Python To Me - Python conversations for passionate developers"
	   },
	   r'(?i)Talk.+Simpson':{
	      "stream":"http://feeds.feedburner.com/LaserTimeTalkingSimpsons",
	      "image":"",
	      "name":"Talking Simpsons"
	   },
	   r'(?i)Christopher Ryan|Tangent.+speak':{
	      "stream":"http://tangent.libsyn.com/rss",
	      "image":"",
	      "name":"Tangentially Speaking with Dr. Christopher Ryan"
	   },
	   r'(?i)TANIS':{
	      "stream":"http://tanis.libsyn.com/rss",
	      "image":"",
	      "name":"TANIS"
	   },
	   r'(?i)tara brach':{
	      "stream":"http://tarabrach.libsyn.com/rss",
	      "image":"",
	      "name":"Tara Brach"
	   },
	   r'(?i)tax.+season':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:143461576/sounds.rss",
	      "image":"",
	      "name":"Tax Season"
	   },
	   r'(?i)taylor talk':{
	      "stream":"http://taylortalk.libsyn.com/rss",
	      "image":"",
	      "name":"Taylor Talk"
	   },
	   r'(?i)(TD|T.D.).+Jake':{
	      "stream":"http://feeds.feedburner.com/TdJakesPodcast",
	      "image":"",
	      "name":"TD Jakes Podcast"
	   },
	   r'(?i)Teach.+Me.+Talk.+laura':{
	      "stream":"http://www.blogtalkradio.com/laura-mize/podcast",
	      "image":"",
	      "name":"Teach Me To Talk with Laura and Friends"
	   },
	   r'(?i)Team.+Beach(.|)body':{
	      "stream":"http://images.beachbody.com/podcasts/beachbodycoach.xml",
	      "image":"",
	      "name":"Team Beachbody Coach Podcast"
	   },
	   r'(?i)Tech.+new.+this.+week':{
	      "stream":"http://feeds.podtrac.com/EJbKUnHP5ywQ",
	      "image":"",
	      "name":"Tech News This Week"
	   },
	   r'(?i)Tech.+new.+today':{
	      "stream":"http://feeds.twit.tv/tnt.xml",
	      "image":"",
	      "name":"Tech News Today (MP3)"
	   },
	   r'(?i)Tech(.|)stuff':{
	      "stream":"http://www.howstuffworks.com/podcasts/techstuff.rss",
	      "image":"",
	      "name":"TechStuff"
	   },
	   r'(?i)Tell.+(em|em).+steve.+dave':{
	      "stream":"http://feeds.feedburner.com/TellEmSteveDave",
	      "image":"",
	      "name":"Tell 'Em Steve-Dave"
	   },
	   r'(?i)Terms':{
	      "stream":"https://rss.art19.com/terms",
	      "image":"",
	      "name":"Terms"
	   },
	   r'(?i)Terrible.+thank':{
	      "stream":"https://feeds.publicradio.org/public_feeds/terrible-thanks-for-asking/itunes/rss",
	      "image":"",
	      "name":"Terrible, Thanks For Asking"
	   },
	   r'(?i)That.+not.+metal':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:172452163/sounds.rss",
	      "image":"",
	      "name":"That's Not Metal"
	   },
	   r'(?i)film(>|)cast':{
	      "stream":"http://feeds.feedburner.com/filmcast",
	      "image":"",
	      "name":"The /Filmcast"
	   },
	   r'(?i)ask(.|)gary':{
	      "stream":"http://askgaryvee.garyvee.libsynpro.com/rss",
	      "image":"",
	      "name":"The #AskGaryVee Show"
	   },
	   r'(?i)three.fifty.nine|(3.59)|three.hund.+fifty.+nine':{
	      "stream":"http://feed.cnet.com/feed/podcast/359-podcast-audio.xml",
	      "image":"",
	      "name":"The 3:59"
	   },
	   r'(?i)(five|5).(AM|A.M.) miracle|Jeff Sanders':{
	      "stream":"http://feedpress.me/jeffsanders",
	      "image":"",
	      "name":"The 5 AM Miracle with Jeff Sanders: Healthy Habits | Personal Development | Rockin' Productivity"
	   },
	   r'(?i)(adam.+drew)':{
	      "stream":"http://feeds.feedburner.com/TheAdamAndDrewShow",
	      "image":"",
	      "name":"The Adam and Dr. Drew Show"
	   },
	   r'(?i)(Adam Carolla)':{
	      "stream":"http://feeds.feedburner.com/TheAdamCarollaPodcast",
	      "image":"",
	      "name":"The Adam Carolla Show"
	   },
	   r'(?i)(Alien Adventures)|Finn Caspian':{
	      "stream":"http://finncaspian.libsyn.com/rss",
	      "image":"",
	      "name":"The Alien Adventures of Finn Caspian: Science Fiction for Kids"
	   },
	   r'(?i)(lusionist)':{
	      "stream":"http://feeds.theallusionist.org/Allusionist",
	      "image":"",
	      "name":"The Allusionist"
	   },
	   r'(?i)(alternative)':{
	      "stream":"http://www.oneplace.com/ministries/the-alternative/subscribe/podcast.xml",
	      "image":"",
	      "name":"The Alternative on OnePlace.com"
	   },
	   r'(?i)(Alton Brown)':{
	      "stream":"http://altonbrown.com/feed/podcast/",
	      "image":"",
	      "name":"The Alton Browncast"
	   },
	   r'(?i)(Amaz.+Seller)':{
	      "stream":"http://theamazingseller.com/feed/podcast/",
	      "image":"",
	      "name":"The Amazing Seller Podcast"
	   },
	   r'(?i)(angry.+chick)':{
	      "stream":"http://feeds.feedburner.com/theangrychicken",
	      "image":"",
	      "name":"The Angry Chicken: A Hearthstone Podcast"
	   },
	   r'(?i)(Anjunadeep Edition)':{
	      "stream":"http://static.anjunadeep.com/edition/podcast.xml",
	      "image":"",
	      "name":"The Anjunadeep Edition"
	   },
	   r'(?i)(Anna.+susan)':{
	      "stream":"http://www.blogtalkradio.com/hahasforhoohaspodcast/podcast",
	      "image":"",
	      "name":"The Anna and Susannah Show"
	   },
	   r'(?i)(Anxiety.+Coach)':{
	      "stream":"http://anxietycoaches.libsyn.com/anxietycoaches",
	      "image":"",
	      "name":"The Anxiety Coaches Podcast - Relief from Anxiety, Panic, and PTSD"
	   },
	   r'(?i)(Baby.+Sitter)':{
	      "stream":"http://babysittersclubclub.libsyn.com/rss",
	      "image":"",
	      "name":"The Baby-Sitters Club Club"
	   },
	   r'(?i)(Bad(.|)christ)':{
	      "stream":"http://bcpod.libsyn.com/rss",
	      "image":"",
	      "name":"The BadChristian Podcast"
	   },
	   r'(?i)(Basement.+Yard)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:169150534/sounds.rss",
	      "image":"",
	      "name":"The Basement Yard"
	   },
	   r'(?i)(bible.+project)':{
	      "stream":"https://simplecast.com/podcasts/1434/rss",
	      "image":"",
	      "name":"The Bible Project"
	   },
	   r'(?i)(big.+listen)':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510314",
	      "image":"",
	      "name":"The Big Listen"
	   },
	   r'(?i)(big.podcast)|shaq':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=779",
	      "image":"",
	      "name":"The Big Podcast With Shaq"
	   },
	   r'(?i)(bill simmon)':{
	      "stream":"http://feeds.feedburner.com/TheBillSimmonsPodcast",
	      "image":"",
	      "name":"The Bill Simmons Podcast"
	   },
	   r'(?i)(birth hour)':{
	      "stream":"http://birthhour.libsyn.com/rss",
	      "image":"",
	      "name":"The Birth Hour"
	   },
	   r'(?i)(birth(.|)ful)':{
	      "stream":"http://birthful.libsyn.com/rss",
	      "image":"",
	      "name":"The Birthful Podcast | Talking with Pregnancy, Birth, Breastfeeding, Postpartum & Parenting Pros to Inform Your Intuition"
	   },
	   r'(?i)(black.+tape)':{
	      "stream":"http://theblacktapes.libsyn.com/rss",
	      "image":"",
	      "name":"The Black Tapes"
	   },
	   r'(?i)(book.+review)':{
	      "stream":"https://feeds.podtrac.com/hyqg9sb75nOH",
	      "image":"",
	      "name":"The Book Review"
	   },
	   r'(?i)(Born.+Yesterday)':{
	      "stream":"http://bornyesterday.libsyn.com/rss",
	      "image":"",
	      "name":"The Born Yesterday Podcast"
	   },
	   r'(?i)(Bowery Boys)':{
	      "stream":"http://boweryboys.libsyn.com/rss",
	      "image":"",
	      "name":"The Bowery Boys: New York City History"
	   },
	   r'(?i)(Brain.+Warrior)':{
	      "stream":"http://amenclinics.libsyn.com/rss",
	      "image":"",
	      "name":"The Brain Warrior's Way Podcast"
	   },
	   r'(?i)(bright session)':{
	      "stream":"http://thebrightsessions.libsyn.com/rss",
	      "image":"",
	      "name":"The Bright Sessions"
	   },
	   r'(?i)(Brilliant idiot)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud%3Ausers%3A88794716/sounds.rss",
	      "image":"",
	      "name":"The Brilliant Idiots"
	   },
	   r'(?i)(british history)':{
	      "stream":"http://feeds.feedburner.com/TheBritishHistoryPodcast",
	      "image":"",
	      "name":"The British History Podcast"
	   },
	   r'(?i)(broad.+exper)':{
	      "stream":"http://rss.acast.com/thebroadexperience",
	      "image":"",
	      "name":"The Broad Experience"
	   },
	   r'(?i)(Brook.+cafeteria)':{
	      "stream":"http://brookingscafeteriapodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Brookings Cafeteria"
	   },
	   r'(?i)(Brutal.+Truth.+About.+Sales)':{
	      "stream":"http://briangburns.podhoster.com/rss/2402/",
	      "image":"",
	      "name":"The Brutal Truth About Sales & Selling - B2B Social LinkedIn SaaS Startup Cold Calling Email Advanced Skills"
	   },
	   r'(?i)canon':{
	      "stream":"http://feeds.feedburner.com/TheCanonPodcast",
	      "image":"",
	      "name":"The Canon"
	   },
	   r'(?i)(carey.+leader)|(Carey Nieuwhof)':{
	      "stream":"http://feeds.feedburner.com/cnlpodcast",
	      "image":"",
	      "name":"The Carey Nieuwhof Leadership Podcast"
	   },
	   r'(?i)(casey.+crew)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:259238942/sounds.rss",
	      "image":"",
	      "name":"The Casey Crew"
	   },
	   r'(?i)(Chalene Show)':{
	      "stream":"http://turbochargedlife.libsyn.com/rss",
	      "image":"",
	      "name":"The Chalene Show | Motivation | Leadership | Confidence | Family | Fitness and Life coaching with Chalene Johnson"
	   },
	   r'(?i)(Change(.|)log)':{
	      "stream":"https://changelog.com/podcast/feed",
	      "image":"",
	      "name":"The Changelog"
	   },
	   r'(?i)(Charged Life)|Brendon Burchard':{
	      "stream":"http://brendonburchard.libsyn.com/rss",
	      "image":"",
	      "name":"The Charged Life with Brendon Burchard"
	   },
	   r'(?i)(Chase Jarvis)':{
	      "stream":"http://chasejarvislive.libsyn.com/itunes",
	      "image":"",
	      "name":"The Chase Jarvis LIVE Show"
	   },
	   r'(?i)(Chief.+(shawn|sean|shaun))':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:120714189/sounds.rss",
	      "image":"",
	      "name":"The Chief and Shawn Show"
	   },
	   r'(?i)(Child.+corn)':{
	      "stream":"http://www.halleycomm.net/podcast/halleycomm_podcast.xml",
	      "image":"",
	      "name":"The Children's Corner"
	   },
	   r'(?i)(christmas.+stock)':{
	      "stream":"http://feeds.feedburner.com/ChristmasStockingPodcast",
	      "image":"",
	      "name":"The Christmas Stocking"
	   },
	   r'(?i)joey.+diaz|What.+Happening.+Now':{
	      "stream":"http://thechurchofwhatshappeningnow.libsyn.com/rss",
	      "image":"",
	      "name":"The Church of What's Happening Now: With Joey Coco Diaz"
	   },
	   r'(?i)cinnamon.+bear':{
	      "stream":"http://cinnamonbear.org.s3.amazonaws.com/podcast.xml",
	      "image":"",
	      "name":"The Cinnamon Bear"
	   },
	   r'(?i)city church.+judah.+smith':{
	      "stream":"http://thecity.org/feeds/audio",
	      "image":"",
	      "name":"The City Church with Judah Smith (Audio)"
	   },
	   r'(?i)clark howard':{
	      "stream":"http://feeds.feedburner.com/ClarkHowardPodcast",
	      "image":"",
	      "name":"The Clark Howard Podcast"
	   },
	   r'(?i)Cleansed':{
	      "stream":"http://feeds.feedburner.com/TheCleansed",
	      "image":"",
	      "name":"The Cleansed: A Post-Apocalyptic Saga"
	   },
	   r'(?i)Co(.|)optional':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:35042463/sounds.rss",
	      "image":"",
	      "name":"The Co-optional Podcast"
	   },
	   r'(?i)College Info Geek':{
	      "stream":"https://simplecast.com/podcasts/98/rss",
	      "image":"",
	      "name":"The College Info Geek Podcast: Study Tips & Advice for Students"
	   },
	   r'(?i)combat.+jack':{
	      "stream":"http://feeds.feedburner.com/TheCombatJackShow",
	      "image":"",
	      "name":"The Combat Jack Show"
	   },
	   r'(?i)comedy.+button':{
	      "stream":"http://comedybutton.libsyn.com/rss",
	      "image":"",
	      "name":"The Comedy Button"
	   },
	   r'(?i)command.+zone':{
	      "stream":"http://feeds.feedburner.com/rocketjump/commandzone",
	      "image":"",
	      "name":"The Command Zone"
	   },
	   r'(?i)cracked':{
	      "stream":"http://rss.earwolf.com/the-cracked-podcast",
	      "image":"",
	      "name":"The Cracked Podcast"
	   },
	   r'(?i)Crown After':{
	      "stream":"http://www.afterbuzztv.com/aftershows/the-crown-afterbuzz-tv-aftershow/feed/",
	      "image":"",
	      "name":"The Crown After Show"
	   },
	   r'(?i)C[uo]lt.+Peda':{
	      "stream":"http://cultofpedagogy.libsyn.com/rss",
	      "image":"",
	      "name":"The Cult of Pedagogy Podcast"
	   },
	   r'(?i)C[ou]lt(.|)cast':{
	      "stream":"http://thecultcast.libsyn.com/rss",
	      "image":"",
	      "name":"The CultCast"
	   },
	   r'(?i)the cure':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:179032792/sounds.rss",
	      "image":"",
	      "name":"The Cure"
	   },
	   r'(?i)Cyber(.|)Wire':{
	      "stream":"http://thecyberwire.libsyn.com/rss",
	      "image":"",
	      "name":"The CyberWire - Your cyber security news connection."
	   },
	   r'(?i)Daily.+Boost':{
	      "stream":"http://dailyboost.motivationtomove.com/rss",
	      "image":"",
	      "name":"The Daily Boost: Best Daily Motivation | Life | Career | Goal Setting | Health | Law of Attraction | Network Marketing"
	   },
	   r'(?i)Daily Fantasy Football Edge':{
	      "stream":"http://dailyfantasyfootballedge.libsyn.com/rss",
	      "image":"",
	      "name":"The Daily Fantasy Football Edge"
	   },
	   r'(?i)Dan.+tard':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=9941853",
	      "image":"",
	      "name":"The Dan Le Batard Show with Stugotz"
	   },
	   r'(?i)Dan Patrick':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=588",
	      "image":"",
	      "name":"The Dan Patrick Show on PodcastOne"
	   },
	   r'(?i)Dave.+Port':{
	      "stream":"http://feeds.feedburner.com/podcastone/njuD",
	      "image":"",
	      "name":"The Dave Portnoy Show"
	   },
	   r'(?i)(DC|D.c).+(Rain(.|)maker)':{
	      "stream":"http://dcrainmaker.libsyn.com/rss",
	      "image":"",
	      "name":"The DC Rainmaker Podcast"
	   },
	   r'(?i)(deep.+vault)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:243532459/sounds.rss",
	      "image":"",
	      "name":"The Deep Vault"
	   },
	   r'(?i)(dice.+tower)':{
	      "stream":"http://dicetower.libsyn.com/rss",
	      "image":"",
	      "name":"The Dice Tower"
	   },
	   r'(?i)(dirt(.|)bag).+(diar)':{
	      "stream":"http://thedirtbag.libsyn.com/rss",
	      "image":"",
	      "name":"The Dirtbag Diaries"
	   },
	   r'(?i)(Discipline.+Investor)':{
	      "stream":"http://feeds.feedburner.com/tdicasts",
	      "image":"",
	      "name":"The Disciplined Investor"
	   },
	   r'(?i)(Disconnect.+dad)':{
	      "stream":"http://sethdahl.libsyn.com/rss",
	      "image":"",
	      "name":"The Disconnected Dad"
	   },
	   r'(?i)(Division)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:102930714/sounds.rss",
	      "image":"",
	      "name":"The Division Podcast"
	   },
	   r'(?i)(The Documentary)':{
	      "stream":"http://www.bbc.co.uk/programmes/p02nq0lx/episodes/downloads.rss",
	      "image":"",
	      "name":"The Documentary"
	   },
	   r'(?i)Dog Trainer':{
	      "stream":"http://www.quickanddirtytips.com/xml/dogtrainer.xml",
	      "image":"",
	      "name":"The Dog Trainer's Quick and Dirty Tips for Teaching and Caring for Your Pet"
	   },
	   r'(?i)(Doug Stan(.+|)hope)':{
	      "stream":"http://stanhope.libsyn.com/rss",
	      "image":"",
	      "name":"The Doug Stanhope Podcast"
	   },
	   r'(?i)(Down.+dirty)':{
	      "stream":"http://www.spreaker.com/user/6543245/episodes/feed",
	      "image":"",
	      "name":"The Down and Dirty Radio Show"
	   },
	   r'(?i)(Dr|doctor).+Drew.+pod':{
	      "stream":"http://feeds.feedburner.com/TheDrDrewPodcast",
	      "image":"",
	      "name":"The Dr. Drew Podcast"
	   },
	   r'(?i)(Dr|doctor).+Laura':{
	      "stream":"http://www.drlaura.com/podcast",
	      "image":"",
	      "name":"The Dr. Laura Program Highlights"
	   },
	   r'(?i)(Dumb(.|)bell)':{
	      "stream":"http://www.spreaker.com/show/2005313/episodes/feed",
	      "image":"",
	      "name":"The Dumbbells"
	   },
	   r'(?i)(Dusty.+life)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:197878231/sounds.rss",
	      "image":"",
	      "name":"The Dusty Life Podcast"
	   },
	   r'(?i)(easy.+allie)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:214104572/sounds.rss",
	      "image":"",
	      "name":"The Easy Allies Podcast"
	   },
	   r'(?i)(ed.+trunk)':{
	      "stream":"http://feeds.feedburner.com/TheEddieTrunkPodcast",
	      "image":"",
	      "name":"The Eddie Trunk Podcast"
	   },
	   r'(?i)(emp.+film)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:13178752/sounds.rss",
	      "image":"",
	      "name":"The Empire Film Podcast"
	   },
	   r'(?i)(energy.+gang)':{
	      "stream":"http://feeds.feedburner.com/theenergygang",
	      "image":"",
	      "name":"The Energy Gang"
	   },
	   r'(?i)(energy.+heal)':{
	      "stream":"http://theenergyhealingpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Energy Healing Podcast"
	   },
	   r'(?i)(English.+We.+Speak)':{
	      "stream":"http://www.bbc.co.uk/programmes/p02pc9zn/episodes/downloads.rss",
	      "image":"",
	      "name":"The English We Speak"
	   },
	   r'(?i)(Enormo|inner mo|irmo)(.|)cast':{
	      "stream":"http://enormocast.com/?feed=podcast",
	      "image":"",
	      "name":"The Enormocast: a climbing podcast"
	   },
	   r'(?i)(Ent).+leadership':{
	      "stream":"http://entreleadershippodcast.ramsey.libsynpro.com/rss",
	      "image":"",
	      "name":"The EntreLeadership Podcast"
	   },
	   r'(?i)Fall.+Rome':{
	      "stream":"https://rss.art19.com/the-fall-of-rome-podcast",
	      "image":"",
	      "name":"The Fall of Rome Podcast"
	   },
	   r'(?i)(Fat.+Burn.+Man)|Abel James':{
	      "stream":"http://fatburningman.com/feed/podcast/",
	      "image":"",
	      "name":"The Fat-Burning Man Show by Abel James. Paleo Nutrition, Ancestral Health & Primal Fitness"
	   },
	   r'(?i)(Fight.+kid)':{
	      "stream":"http://thefighterandthekid.tfatk.libsynpro.com/rss",
	      "image":"",
	      "name":"The Fighter and The Kid"
	   },
	   r'(?i)(film.+vault)':{
	      "stream":"http://feeds.feedburner.com/TheFilmVault",
	      "image":"",
	      "name":"The Film Vault"
	   },
	   r'(?i)(first).+(40|forty).+mile':{
	      "stream":"http://www.thefirst40miles.com/feed/",
	      "image":"",
	      "name":"The First forty Miles: Hiking and Backpacking Podcast"
	   },
	   r'(?i)(the).+(flash)':{
	      "stream":"http://theflashpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Flash Podcast"
	   },
	   r'(?i)(flop).+(house)':{
	      "stream":"http://theflophouse.libsyn.com/rss",
	      "image":"",
	      "name":"The Flop House"
	   },
	   r'(?i)(the forward)':{
	      "stream":"http://theforwardpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Forward"
	   },
	   r'(?i)(friend.+zone)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:167300167/sounds.rss",
	      "image":"",
	      "name":"The Friend Zone"
	   },
	   r'(?i)(front.+porch)':{
	      "stream":"http://wvpublic.org/podcasts/29182/rss.xml",
	      "image":"",
	      "name":"The Front Porch"
	   },
	   r'(?i)(gadget.+lab)':{
	      "stream":"https://www.wired.com/feed/podcast/gadget-lab",
	      "image":"",
	      "name":"The Gadget Lab Podcast"
	   },
	   r'(?i)(game.+info)':{
	      "stream":"http://feeds.feedburner.com/gameinformershow",
	      "image":"",
	      "name":"The Game Informer Show"
	   },
	   r'(?i)(Garbage.+Time)|Katie Nolan':{
	      "stream":"http://feeds.feedburner.com/GarbageTimePodcast",
	      "image":"",
	      "name":"The Garbage Time Podcast with Katie Nolan"
	   },
	   r'(?i)(Gary Neville)':{
	      "stream":"http://rss.acast.com/garynevillepodcast",
	      "image":"",
	      "name":"The Gary Neville Podcast - Sky Sports"
	   },
	   r'(?i)(gen.+why)':{
	      "stream":"http://thegenerationwhypodcast.com/feed/category/podcast",
	      "image":"",
	      "name":"The Generation Why Podcast"
	   },
	   r'(?i)(giant.+beast)':{
	      "stream":"http://www.giantbomb.com/podcast-xml/beastcast/",
	      "image":"",
	      "name":"The Giant Beastcast"
	   },
	   r'(?i)(girl.+who)':{
	      "stream":"http://rss.acast.com/thegirlswholived",
	      "image":"",
	      "name":"The Girls Who Lived"
	   },
	   r'(?i)((goal|gold).+digger)':{
	      "stream":"http://goaldiggerpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Goal Digger Podcast"
	   },
	   r'(?i)((good.+dad).+proj)':{
	      "stream":"http://gooddadproject.libsyn.com/rss",
	      "image":"",
	      "name":"The Good Dad Project"
	   },
	   r'(?i)(Gospel.+Coal)':{
	      "stream":"https://www.thegospelcoalition.org/media/The_Gospel_Coalition",
	      "image":"",
	      "name":"The Gospel Coalition (TGC)"
	   },
	   r'(?i)guardian.+sci.+week':{
	      "stream":"https://www.theguardian.com/science/series/science/podcast.xml",
	      "image":"",
	      "name":"The Guardian's Science Weekly"
	   },
	   r'(?i)(h.p.|HP).+love(.|)craft':{
	      "stream":"http://hppodcraft.com/feed/podcast/",
	      "image":"",
	      "name":"The H.P. Lovecraft Literary Podcast"
	   },
	   r'(?i)(Jamie Iv(e|)y)':{
	      "stream":"http://jamieivey.libsyn.com/rss",
	      "image":"",
	      "name":"The Happy Hour with Jamie Ivey"
	   },
	   r'(?i)(The Heart)':{
	      "stream":"http://feeds.theheartradio.org/TheHeartRadio",
	      "image":"",
	      "name":"The Heart"
	   },
	   r'(?i)(Colin (Cowherd|coward))|(the herd)':{
	      "stream":"http://foxsportsradio.iheart.com/podcast/itunes/The_Herd_Hours_itunes.xml",
	      "image":"",
	      "name":"The Herd with Colin Cowherd"
	   },
	   r'(?i)(Hermetic Hour)':{
	      "stream":"http://www.blogtalkradio.com/the-hermetic-hour/podcast",
	      "image":"",
	      "name":"The Hermetic Hour"
	   },
	   r'(?i)(Hilar.+World.+depress)':{
	      "stream":"https://feeds.publicradio.org/public_feeds/the-hilarious-world-of-depression/itunes/rss",
	      "image":"",
	      "name":"The Hilarious World of Depression"
	   },
	   r'(?i)(Hine.+ward)':{
	      "stream":"http://hineswardshow.com/feed/podcast/",
	      "image":"",
	      "name":"The Hines Ward Show"
	   },
	   r'(?i)(History.+Chick)':{
	      "stream":"http://feeds.feedburner.com/TheHistoryChicks",
	      "image":"",
	      "name":"The History Chicks"
	   },
	   r'(?i)(Home(.|)making.+Found)':{
	      "stream":"https://youngwifesguide.com/feed/podcast/",
	      "image":"",
	      "name":"The Homemaking Foundations Podcast"
	   },
	   r'(?i)(Idealist)':{
	      "stream":"http://feeds.feedburner.com/idealistpodcasts",
	      "image":"",
	      "name":"The Idealist.org Podcasts"
	   },
	   r'(?i)(Indoor Kids)|Kumail Nanjiani|Emily.+Gordon':{
	      "stream":"http://theindoorkids.libsyn.com/rss",
	      "image":"",
	      "name":"The Indoor Kids with Kumail Nanjiani and Emily V. Gordon"
	   },
	   r'(?i)(Infin.+Monk.+cage)':{
	      "stream":"http://www.bbc.co.uk/programmes/b00snr0w/episodes/downloads.rss",
	      "image":"",
	      "name":"The Infinite Monkey Cage"
	   },
	   r'(?i)(The Instance)':{
	      "stream":"http://feeds.frogpants.com/theinstance_feed.xml",
	      "image":"",
	      "name":"The Instance: The Podcast for Lovers of Blizzard Games"
	   },
	   r'(?i)(Internet of Things)':{
	      "stream":"http://iotpodcast.com/feed/podcast/",
	      "image":"",
	      "name":"The Internet of Things podcast"
	   },
	   r'(?i)(Jack Benny)':{
	      "stream":"http://jackbenny.libsyn.com/rss",
	      "image":"",
	      "name":"The Jack Benny Show"
	   },
	   r'(?i)(James Altucher)':{
	      "stream":"http://altucher.stansberry.libsynpro.com/rss",
	      "image":"",
	      "name":"The James Altucher Show"
	   },
	   r'(?i)(jill.+Mich)':{
	      "stream":"http://rss.art19.com/jillian-michaels",
	      "image":"",
	      "name":"The Jillian Michaels Show"
	   },
	   r'(?i)(Keto Diet)':{
	      "stream":"http://thenosugarcoatingpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Keto Diet Podcast"
	   },
	   r'(?i)(Ketovangelist)':{
	      "stream":"https://www.ketovangelist.com/category/podcast/feed/",
	      "image":"",
	      "name":"The Ketovangelist Podcast"
	   },
	   r'(?i)(Ki[bd].+Fin)':{
	      "stream":"http://www.themusclecarplace.com/category/kibbe-and-finnegan/feed",
	      "image":"",
	      "name":"The Kibbe and Finnegan Show"
	   },
	   r'(?i)(Korea.+Society)':{
	      "stream":"http://feeds.koreasociety.org/tkspodcasts",
	      "image":"",
	      "name":"The Korea Society"
	   },
	   r'(?i)(Leviathan.+Chronic)':{
	      "stream":"http://feeds.feedburner.com/TheLeviathanChroniclesPodcasts",
	      "image":"",
	      "name":"The Leviathan Chronicles"
	   },
	   r'(?i)(Brooke Castillo)|Life Coach School':{
	      "stream":"http://thelifecoachschool.libsyn.com/rss",
	      "image":"",
	      "name":"The Life Coach School Podcast with Brooke Castillo"
	   },
	   r'(?i)(Life(.|)time Cash Flow)':{
	      "stream":"http://lifetimecashflowpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Lifetime Cash Flow Through Real Estate Investing Podcast"
	   },
	   r'(?i)(Liturgists|liturgy)':{
	      "stream":"http://theliturgists.podbean.com/feed/",
	      "image":"",
	      "name":"The Liturgists Podcast"
	   },
	   r'(?i)(Lively.+Show)':{
	      "stream":"http://d2grjfi36hr26b.cloudfront.net/podcast.xml",
	      "image":"",
	      "name":"The Lively Show"
	   },
	   r'(?i)(Livin.+Vida.+Low.+carb)':{
	      "stream":"http://llvlcshow.libsyn.com/rss",
	      "image":"",
	      "name":"The Livin' La Vida Low-Carb Show With Jimmy Moore"
	   },
	   r'(?i)(long.+short.+time)':{
	      "stream":"http://rss.earwolf.com/the-longest-shortest-time",
	      "image":"",
	      "name":"The Longest Shortest Time"
	   },
	   r'(?i)(look.+sound.+lead)':{
	      "stream":"http://essentialcomm.libsyn.com/rss",
	      "image":"",
	      "name":"The Look and Sound of Leadership"
	   },
	   r'(?i)(Love Bomb)|Nico Tortorella':{
	      "stream":"http://thelovebomb.libsyn.com/rss",
	      "image":"",
	      "name":"The Love Bomb with Nico Tortorella"
	   },
	   r'(?i)(Low.+Post)':{
	      "stream":"http://www.espn.com/espnradio/feeds/rss/podcast.xml?id=10528553",
	      "image":"",
	      "name":"The Lowe Post"
	   },
	   r'(?i)(Majority Report|Sam Seder)':{
	      "stream":"http://feeds.feedburner.com/MajorityReport",
	      "image":"",
	      "name":"The Majority Report with Sam Seder"
	   },
	   r'(?i)(Ben Vaughn)':{
	      "stream":"http://z1077fm.com/benvaughn.xml",
	      "image":"",
	      "name":"The Many Moods of Ben Vaughn hosted by Ben Vaughn"
	   },
	   r'(?i)(Marriage.+Smart)':{
	      "stream":"http://www.onlyyouforever.com/feed/podcast/",
	      "image":"",
	      "name":"The Marriage Podcast for Smart People | from OnlyYouForever | Because Marriage Should Be Forever"
	   },
	   r'(?i)(Math Dude)':{
	      "stream":"http://www.quickanddirtytips.com/xml/mathdude.xml",
	      "image":"",
	      "name":"The Math Dude Quick and Dirty Tips to Make Math Easier"
	   },

	   r'(?i)Memory Palace':{
	      "stream":"http://feeds.feedburner.com/thememorypalace",
	      "image":"",
	      "name":"The Memory Palace"
	   },
	   r'(?i)Might.+Mom.+parent':{
	      "stream":"http://www.quickanddirtytips.com/mommy.xml",
	      "image":"",
	      "name":"The Mighty Mommy's Quick and Dirty Tips for Practical Parenting"
	   },
	   r'(?i)Milo Yiannopoulos':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=863",
	      "image":"",
	      "name":"The Milo Yiannopoulos Show"
	   },
	   r'(?i)Minimalists':{
	      "stream":"http://theminimalists.libsyn.com/rss",
	      "image":"",
	      "name":"The Minimalists Podcast"
	   },
	   r'(?i)Ariel Helwani|((MMA|M.M.A).+Hour)':{
	      "stream":"http://feeds.feedburner.com/aol/fanhouse/mmahour/audio",
	      "image":"",
	      "name":"The MMA Hour with Ariel Helwani"
	   },
	   r'(?i)Model Health':{
	      "stream":"http://themodelhealthshow.libsyn.com/rss",
	      "image":"",
	      "name":"The Model Health Show: Nutrition | Exercise | Fitness | Health | Lifestyle"
	   },
	   r'(?i)Mom Hour|Me(a|)gan Francis|Sarah Powers':{
	      "stream":"http://lifelistened.com/feed/the-mom-hour/",
	      "image":"",
	      "name":"The Mom Hour with Meagan Francis and Sarah Powers"
	   },
	   r'(?i)Brian Koppelman|the moment':{
	      "stream":"http://feeds.feedburner.com/the-moment",
	      "image":"",
	      "name":"The Moment with Brian Koppelman"
	   },
	   r'(?i)Mortified':{
	      "stream":"http://feeds.getmortified.com/MortifiedPod",
	      "image":"",
	      "name":"The Mortified Podcast"
	   },
	   r'(?i)Naked.+Scien':{
	      "stream":"http://rss.acast.com/naked_scientists_podcast",
	      "image":"",
	      "name":"The Naked Scientists Podcast"
	   },
	   r'(?i)Nat.+Archive':{
	      "stream":"http://feeds.feedburner.com/TheNationalArchivesPodcastSeries",
	      "image":"",
	      "name":"The National Archives Podcast Series"
	   },
	   r'(?i)New York Public Library':{
	      "stream":"http://newyorkpubliclibrary.libsyn.com/rss",
	      "image":"",
	      "name":"The New York Public Library Podcast"
	   },
	   r'(?i)New Yorker.+Fiction':{
	      "stream":"http://feeds.wnyc.org/tnyfiction",
	      "image":"",
	      "name":"The New Yorker: Fiction"
	   },
	   r'(?i)Writer.+Voice':{
	      "stream":"http://feeds.wnyc.org/tnyauthorsvoice",
	      "image":"",
	      "name":"The New Yorker: The Writer's Voice"
	   },
	   r'(?i)Next picture':{
	      "stream":"http://feeds.megaphone.fm/FLM2375047009",
	      "image":"",
	      "name":"The Next Picture Show"
	   },
	   r'(?i)No film school':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:189059907/sounds.rss",
	      "image":"",
	      "name":"The No Film School Podcast"
	   },
	   r'(?i)no(.|)sleep':{
	      "stream":"http://rss.art19.com/nosleep",
	      "image":"",
	      "name":"The NoSleep Podcast"
	   },
	   r'(?i)Nutrition Diva':{
	      "stream":"http://www.quickanddirtytips.com/xml/nutrition.xml",
	      "image":"",
	      "name":"The Nutrition Diva's Quick and Dirty Tips for Eating Well and Feeling Fabulous"
	   },
	   r'(?i)Adventure.+odyssey':{
	      "stream":"http://feeds.feedburner.com/focus-on-the-family/adventures-in-odyssey-podcast",
	      "image":"",
	      "name":"The Official Adventures in Odyssey Podcast"
	   },
	   r'(?i)Red.+Chip.+Poker':{
	      "stream":"http://redchippoker.libsyn.com/rss",
	      "image":"",
	      "name":"The Official Red Chip Poker Podcast"
	   },
	   r'(?i)One.+You.+Feed':{
	      "stream":"http://oneyoufeed.libsyn.com/rss",
	      "image":"",
	      "name":"The One You Feed"
	   },
	   r'(?i)Orbit.+Human.+circus':{
	      "stream":"http://orbitinghumancircus.libsyn.com/rss",
	      "image":"",
	      "name":"The Orbiting Human Circus (of the Air)"
	   },
	   r'(?i)Overwhelmed Brain':{
	      "stream":"http://theoverwhelmedbrain.libsyn.com/rss",
	      "image":"",
	      "name":"The Overwhelmed Brain"
	   },
	   r'(?i)Paleo Women':{
	      "stream":"http://coconutsandkettlebells.com/feed/podcast/",
	      "image":"",
	      "name":"The Paleo Women Podcast: Health | Nutrition | Fitness | Hormones"
	   },
	   r'(?i)Partial.+Examine.+Life':{
	      "stream":"http://feeds2.feedburner.com/ThePartiallyExaminedLife",
	      "image":"",
	      "name":"The Partially Examined Life Philosophy Podcast"
	   },
	   r'(?i)The Patch':{
	      "stream":"http://theknow.roosterteeth.com/show/the-patch/feed/mp3",
	      "image":"",
	      "name":"The Patch"
	   },
	   r'(?i)People.+Pharmacy':{
	      "stream":"http://feeds.feedburner.com/ThePeoplesPharmacy",
	      "image":"",
	      "name":"The People's Pharmacy"
	   },
	   r'(?i)Perfect.+Wife':{
	      "stream":"http://theperfectwife.libsyn.com/rss",
	      "image":"",
	      "name":"The Perfect Wife"
	   },
	   r'(?i)Peter Schiff':{
	      "stream":"http://www.schiffradio.com/feed/podcast/",
	      "image":"",
	      "name":"The Peter Schiff Show Podcast"
	   },
	   r'(?i)pod(.|)father':{
	      "stream":"http://feeds.feedburner.com/ThePodfathers",
	      "image":"",
	      "name":"The Podfathers"
	   },
	   r'(?i)Politic.+Guy':{
	      "stream":"http://politicsguys.com/feed/podcast/",
	      "image":"",
	      "name":"The Politics Guys"
	   },
	   r'(?i)Knox.+Jamie':{
	      "stream":"http://thepopcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Popcast With Knox and Jamie"
	   },
	   r'(?i)Posit.+head':{
	      "stream":"http://positivehead.libsyn.com/rss",
	      "image":"",
	      "name":"The Positive Head Podcast"
	   },
	   r'(?i)potter.+touch':{
	      "stream":"http://www.oneplace.com/ministries/the-potters-touch/subscribe/podcast.xml",
	      "image":"",
	      "name":"The Potter's Touch"
	   },
	   r'(?i)(Pre(.|)med.+year)':{
	      "stream":"http://medicalschoolhq.libsyn.com/rss",
	      "image":"",
	      "name":"The Premed Years"
	   },
	   r'(?i)(Psychology Podcast)':{
	      "stream":"http://psychologypodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Psychology Podcast"
	   },
	   r'(?i)(Pulse)':{
	      "stream":"http://feeds.feedburner.com/newsworks/ThePulse",
	      "image":"",
	      "name":"The Pulse"
	   },
	   r'(?i)(Jeff Goldsmith)':{
	      "stream":"http://feeds.feedburner.com/TheQaWithJeffGoldsmith",
	      "image":"",
	      "name":"The Q&A with Jeff Goldsmith"
	   },
	   r'(?i)(quote.+day)':{
	      "stream":"http://quoteofthedayshow.libsyn.com/rss",
	      "image":"",
	      "name":"The Quote of the Day Show"
	   },
	   r'(?i)(adventur).+(El).+(amp)':{
	      "stream":"http://feeds.feedburner.com/TheRadioAdventuresOfEleanorAmplified",
	      "image":"",
	      "name":"The Radio Adventures of Eleanor Amplified"
	   },
	   r'(?i)(Real Estate Guys)':{
	      "stream":"https://realestateguysradio.com/wp-content/themes/real_estate_guys_10/feed/index2.php",
	      "image":"",
	      "name":"The Real Estate Guys Radio Show"
	   },
	   r'(?i)(Ric.+Flair)':{
	      "stream":"https://audioboom.com/channels/4769828.rss",
	      "image":"",
	      "name":"The Ric Flair Show"
	   },
	   r'(?i)(Rich Roll)':{
	      "stream":"http://www.richroll.com/feed/podcast/",
	      "image":"",
	      "name":"The Rich Roll Podcast"
	   },
	   r'(?i)(Bomani Jones)|Right Time':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=12563086",
	      "image":"",
	      "name":"The Right Time with Bomani Jones"
	   },
	   r'(?i)(Ringer.+(MLB|M.l.b))':{
	      "stream":"http://feeds.feedburner.com/ringermlbshow",
	      "image":"",
	      "name":"The Ringer MLB Show"
	   },
	   r'(?i)(Ringer.+(NBA|n.b.a))':{
	      "stream":"http://feeds.feedburner.com/RingerNBAShow",
	      "image":"",
	      "name":"The Ringer NBA Show"
	   },
	   r'(?i)(Ringer.+(NFL|n.f.l))':{
	      "stream":"http://feeds.feedburner.com/ringernflshow",
	      "image":"",
	      "name":"The Ringer NFL Show"
	   },
	   r'(?i)(Risk.+taker)':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:254359729/sounds.rss",
	      "image":"",
	      "name":"The Risk Takers"
	   },
	   r'(?i)(Road.+Back.+You)':{
	      "stream":"http://Theroadbacktoyou.podbean.com/feed/",
	      "image":"",
	      "name":"The Road Back to You"
	   },
	   r'(?i)(Rob(.|)Cast)':{
	      "stream":"http://robbell.podbean.com/feed/",
	      "image":"",
	      "name":"The RobCast"
	   },
	   r'(?i)(Rob.+(Sharma|charm))':{
	      "stream":"http://robinsharma.libsyn.com/rss",
	      "image":"",
	      "name":"The Robin Sharma Mastery Sessions"
	   },
	   r'(?i)(Ross Report)':{
	      "stream":"http://www.podcastone.com/podcast?categoryID2=619",
	      "image":"",
	      "name":"The Ross Report"
	   },
	   r'(?i)(round.+gentle)':{
	      "stream":"http://feeds.feedburner.com/TheRoundTableOfGentlemen",
	      "image":"",
	      "name":"The Roundtable of Gentlemen"
	   },
	   r'(?i)(Runner.+world)':{
	      "stream":"http://feeds.feedburner.com/TheRunnersWorldShow",
	      "image":"",
	      "name":"The Runner's World Show"
	   },
	   r'(?i)(scare(.|)cast)|(creepy.+pasta)':{
	      "stream":"http://maddmike.libsyn.com/rss",
	      "image":"",
	      "name":"The Scarecast - Scary Stories and Creepypasta"
	   },
	   r'(?i)Scathing Atheist':{
	      "stream":"https://audioboom.com/channels/4829847.rss",
	      "image":"",
	      "name":"The Scathing Atheist"
	   },
	   r'(?i)School of Greatness|Lewis Howes':{
	      "stream":"http://lewishowes.com/feed/podcast/",
	      "image":"",
	      "name":"The School of Greatness with Lewis Howes"
	   },
	   r'(?i)Science of Success':{
	      "stream":"http://redorbit.podbean.com/feed/",
	      "image":"",
	      "name":"The Science of Success"
	   },
	   r'(?i)(Big Jay Oakerson|Ralph Sutton|Sex.+Drugs.+Rock)':{
	      "stream":"http://thesdrshow.libsyn.com/rss",
	      "image":"",
	      "name":"The SDR Show (Sex, Drugs, and Rock-n-Roll Show) w/ Big Jay Oakerson & Ralph Sutton"
	   },
	   r'(?i)(Secret To Success)|Eric Thomas|CJ Thomas':{
	      "stream":"http://secrettosuccess.libsyn.com/rss",
	      "image":"",
	      "name":"The Secret To Success with CJ & Eric Thomas"
	   },
	   r'(?i)(Serial Killer)':{
	      "stream":"http://theserialkillerpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Serial Killer Podcast"
	   },
	   r'(?i)(Seth Davis)':{
	      "stream":"http://feeds.feedburner.com/seth-davis",
	      "image":"",
	      "name":"The Seth Davis Podcast"
	   },
	   r'(?i)(Shameless Mom)':{
	      "stream":"http://selfishmomacademy.libsyn.com/rss",
	      "image":"",
	      "name":"The Shameless Mom Academy"
	   },
	   r'(?i)(Side Hustle show)':{
	      "stream":"http://www.sidehustlenation.com/feed/podcast/",
	      "image":"",
	      "name":"The Side Hustle Show"
	   },
	   r'(?i)(Simpl.+Scary)':{
	      "stream":"http://simplyscarypodcast.com/feed/podcast",
	      "image":"",
	      "name":"The Simply Scary Podcast"
	   },
	   r'(?i)(Skeptic.+guide)':{
	      "stream":"http://www.theskepticsguide.org/feed/sgu",
	      "image":"",
	      "name":"The Skeptics' Guide to the Universe"
	   },
	   r'(?i)(Smart.+Passive.+Income)|Pat Flynn':{
	      "stream":"http://feeds.feedburner.com/spipodcast",
	      "image":"",
	      "name":"The Smart Passive Income Podcast"
	   },
	   r'(?i)(Smartest.+Man.+world)|greg proop':{
	      "stream":"http://feeds.feedburner.com/TheSmartest",
	      "image":"",
	      "name":"The Smartest Man in the World"
	   },
	   r'(?i)(Smith(.|)Squad)':{
	      "stream":"http://thesmithplays.podbean.com/feed/",
	      "image":"",
	      "name":"The SmithSquad Podcast"
	   },
	   r'(?i)(Smok.+Tire)':{
	      "stream":"http://shoutengine.com/TheSmokingTire.xml",
	      "image":"",
	      "name":"The Smoking Tire"
	   },
	   r'(?i)(Social.+Work)':{
	      "stream":"http://www.socialworkpodcast.com/socialworkpodcast.xml",
	      "image":"",
	      "name":"The Social Work Podcast"
	   },
	   r'(?i)(Solid.+Verbal)':{
	      "stream":"http://feeds.feedburner.com/solidverbal",
	      "image":"",
	      "name":"The Solid Verbal: Living College Football"
	   },
	   r'(?i)(Splend.+Table)':{
	      "stream":"https://www.splendidtable.org/feeds/podcast/itunes",
	      "image":"",
	      "name":"The Splendid Table"
	   },
	   r'(?i)(Spork)':{
	      "stream":"http://feeds.feedburner.com/sporkful",
	      "image":"",
	      "name":"The Sporkful"
	   },
	   r'(?i)(Luke.+Jed)|Sports.+Drag.+Rac':{
	      "stream":"http://sportsmandragracingpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Sportsman Drag Racing Podcast w/ Luke and Jed"
	   },
	   r'(?i)(Starters)':{
	      "stream":"http://feeds.adknit.com/app-search/nba/the-starters/all/720/200/",
	      "image":"",
	      "name":"The Starters"
	   },
	   r'(?i)(Story.+Collide)':{
	      "stream":"http://feeds.feedburner.com/TheStoryCollider",
	      "image":"",
	      "name":"The Story Collider"
	   },
	   r'(?i)(Story Home)':{
	      "stream":"http://feeds.feedburner.com/thestoryhome",
	      "image":"",
	      "name":"The Story Home Children's Audio Stories"
	   },
	   r'(?i)(John Gruber)|the talk show':{
	      "stream":"http://daringfireball.net/thetalkshow/rss",
	      "image":"",
	      "name":"The Talk Show With John Gruber"
	   },
	   r'(?i)(Tech Guy)':{
	      "stream":"http://feeds.twit.tv/kfi.xml",
	      "image":"",
	      "name":"The Tech Guy (MP3)"
	   },
	   r'(?i)(Tony Kornheiser)':{
	      "stream":"http://feeds.feedburner.com/kornheiser",
	      "image":"",
	      "name":"The Tony Kornheiser Show"
	   },
	   r'(?i)(The Torch)':{
	      "stream":"http://podcasts.teach12.com/thetorch.xml",
	      "image":"",
	      "name":"The Torch: The Great Courses Podcast"
	   },
	   r'(?i)Ultimate Health':{
	      "stream":"http://ultimatehealthpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"The Ultimate Health Podcast: Wellness, Nutrition, Fitness, & Exercise"
	   },
	   r'(?i)beatable Mind|Mark Divine':{
	      "stream":"http://sealfit.libsyn.com/rss",
	      "image":"",
	      "name":"The Unbeatable Mind Podcast with Mark Divine"
	   },
	   r'(?i)Unexplain.+disappear|Mars Patel':{
	      "stream":"http://pruittprep.com/feed/podcast/",
	      "image":"",
	      "name":"The Unexplainable Disappearance of Mars Patel"
	   },
	   r'(?i)UUrban Farm|Greg Peterson':{
	      "stream":"http://urbanfarm.libsyn.com/rss",
	      "image":"",
	      "name":"The Urban Farm Podcast with Greg Peterson"
	   },
	   r'(?i)verge':{
	      "stream":"http://feeds.feedburner.com/ThisIsMyNextPodcast",
	      "image":"",
	      "name":"The Vergecast"
	   },
	   r'(?i)Vertical.+J.+Red':{
	      "stream":"http://feeds.feedburner.com/Vertical-JJ",
	      "image":"",
	      "name":"The Vertical Podcast with JJ Redick"
	   },
	   r'(?i)Vertical.+with.+W':{
	      "stream":"http://feeds.feedburner.com/VerticalPodcast",
	      "image":"",
	      "name":"The Vertical Podcast with Woj"
	   },
	   r'(?i)Village Church.+culture':{
	      "stream":"http://feeds.thevillagechurch.net/culture-matters",
	      "image":"",
	      "name":"The Village Church - Culture Matters"
	   },
	   r'(?i)Village Church.+Sermon':{
	      "stream":"http://feeds.thevillagechurch.net/sermons",
	      "image":"",
	      "name":"The Village Church - Sermons"
	   },
	   r'(?i)Von.+Doctrine':{
	      "stream":"http://rss-cmg.streamguys1.com/atlanta/atl750/the-eric-von-heassle.xml",
	      "image":"",
	      "name":"The Von Haessler Doctrine"
	   },
	   r'(?i)The Watch':{
	      "stream":"http://feeds.feedburner.com/thewatchpod",
	      "image":"",
	      "name":"The Watch"
	   },
	   r'(?i)We(e|)b(.|)cast':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:116406291/sounds.rss",
	      "image":"",
	      "name":"The Weebcast"
	   },
	   r'(?i)Week.+Health.+Law':{
	      "stream":"http://twihl.podbean.com/feed/",
	      "image":"",
	      "name":"The Week in Health Law"
	   },
	   r'(?i)Week.+Planet':{
	      "stream":"http://weeklyplanetpod.libsyn.com/rss",
	      "image":"",
	      "name":"The Weekly Planet"
	   },
	   r'(?i)Week.+standard':{
	      "stream":"http://weeklysubstandard.weeklystandard.libsynpro.com/rss",
	      "image":"",
	      "name":"The Weekly Substandard"
	   },
	   r'(?i)West.+Wing.+Week':{
	      "stream":"http://westwingweekly.libsyn.com/feed",
	      "image":"",
	      "name":"The West Wing Weekly"
	   },
	   r'(?i)Wood(.|)work':{
	      "stream":"http://www.thewoodworkingpodcast.com/feed/",
	      "image":"",
	      "name":"The Woodworking Podcast"
	   },
	   r'(?i)Word.+Fire':{
	      "stream":"http://wordonfire.libsyn.com/rss",
	      "image":"",
	      "name":"The Word on Fire Show"
	   },
	   r'(?i)Writer.+alm|Garrison Keillor':{
	      "stream":"http://feeds.americanpublicmedia.org/writersalmanac",
	      "image":"",
	      "name":"The Writer's Almanac with Garrison Keillor"
	   },
	   r'(?i)Writer.+panel':{
	      "stream":"http://nerdistwriters.libsyn.com/rss",
	      "image":"",
	      "name":"The Writers Panel"
	   },
	   r'(?i)Ziglar|ziggler':{
	      "stream":"http://zigziglar.libsyn.com/rss",
	      "image":"",
	      "name":"The Ziglar Show"
	   },
	   r'(?i)Therapy Chat':{
	      "stream":"http://baltimoreannapolispsychotherapypodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Therapy Chat"
	   },
	   r'(?i)Think.+atheist':{
	      "stream":"http://www.blogtalkradio.com/thethinkingatheist/podcast",
	      "image":"",
	      "name":"TheThinkingAtheist"
	   },
	   r'(?i)Think.+(allow|out loud)':{
	      "stream":"http://www.bbc.co.uk/programmes/b006qy05/episodes/downloads.rss",
	      "image":"",
	      "name":"Thinking Allowed"
	   },
	   r'(?i)Think.+(side)':{
	      "stream":"http://thinkingsidewayspodcast.libsyn.com/rss",
	      "image":"",
	      "name":"Thinking Sideways Podcast"
	   },
	   r'(?i)This Is Your Life|Michael Hyatt':{
	      "stream":"http://feeds.feedburner.com/TIYL",
	      "image":"",
	      "name":"This Is Your Life with Michael Hyatt"
	   },
	   r'(?i)This Morning|Gordon Deal':{
	      "stream":"http://feeds.feedburner.com/thismorningamericasfirstnews",
	      "image":"",
	      "name":"This Morning With Gordon Deal"
	   },
	   r'(?i)This Week I Learned':{
	      "stream":"https://simplecast.com/podcasts/2095/rss",
	      "image":"",
	      "name":"This Week I Learned"
	   },
	   r'(?i)This Week in Googl':{
	      "stream":"http://feeds.twit.tv/twig.xml",
	      "image":"",
	      "name":"This Week in Google (MP3)"
	   },
	   r'(?i)This Week in law':{
	      "stream":"http://feeds.twit.tv/twil.xml",
	      "image":"",
	      "name":"This Week in Law (MP3)"
	   },
	   r'(?i)This Week in machine learn':{
	      "stream":"http://feeds.feedburner.com/twimlai",
	      "image":"",
	      "name":"This Week in Machine Learning & AI Podcast"
	   },
	   r'(?i)This Week in marvel':{
	      "stream":"http://marvel.com/podcasts/10/this_week_in_marvel/rss",
	      "image":"",
	      "name":"This Week in Marvel"
	   },
	   r'(?i)This Week in tech':{
	      "stream":"http://feeds.twit.tv/twit.xml",
	      "image":"",
	      "name":"This Week in Tech (MP3)"
	   },
	   r'(?i)Thriller.+radio':{
	      "stream":"http://thrillersotr.rnn.libsynpro.com/rss",
	      "image":"",
	      "name":"Thrillers Old Time Radio"
	   },
	   r'(?i)Thrill.+adventure':{
	      "stream":"http://feeds.feedburner.com/ThrillingAdventureHour",
	      "image":"",
	      "name":"Thrilling Adventure Hour"
	   },
	   r'(?i)throw.+shade':{
	      "stream":"http://throwingshade.libsyn.com/rss",
	      "image":"",
	      "name":"Throwing Shade"
	   },
	   r'(?i)Til.+Death.+blart':{
	      "stream":"http://blart.libsyn.com/rss",
	      "image":"",
	      "name":"Til Death Do Us Blart"
	   },
	   r'(?i)Timothy Keller':{
	      "stream":"https://ginl-podcast.s3.amazonaws.com/0_Resources/Timothy_Keller_Podcasts.xml",
	      "image":"",
	      "name":"Timothy Keller Sermons Podcast by Gospel in Life"
	   },
	   r'(?i)Tiny Desk Concert':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510306",
	      "image":"",
	      "name":"Tiny Desk Concerts - Audio"
	   },
	   r'(?i)Todd White':{
	      "stream":"http://toddwhite.libsyn.com/toddwhite",
	      "image":"",
	      "name":"Todd White Podcast"
	   },
	   r'(?i)Embarrassed':{
	      "stream":"http://feeds.feedburner.com/Recode-TETA",
	      "image":"",
	      "name":"Too Embarrassed to Ask"
	   },
	   r'(?i)Total Human':{
	      "stream":"http://onnit.libsyn.com/rss",
	      "image":"",
	      "name":"Total Human Optimization"
	   },
	   r'(?i)Total.+marr':{
	      "stream":"http://totallymarried.libsyn.com/rss",
	      "image":"",
	      "name":"Totally Married"
	   },
	   r'(?i)True.+murder':{
	      "stream":"http://www.blogtalkradio.com/dan-zupansky1/podcast",
	      "image":"",
	      "name":"True Murder"
	   },
	   r'(?i)True(.|)hoop':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=12426375",
	      "image":"",
	      "name":"TrueHoop"
	   },
	   r'(?i)Trust.+Believe':{
	      "stream":"https://shauntfitness.com/feed/podcast/",
	      "image":"",
	      "name":"Trust and Believe with Shaun T"
	   },
	   r'(?i)Truth.+(Iliza|elisa)':{
	      "stream":"http://feeds.sideshownetwork.tv/Truth&Iliza",
	      "image":"",
	      "name":"Truth and Iliza"
	   },
	   r'(?i)Truth.+(life)':{
	      "stream":"http://feeds.feedburner.com/TruthForLife",
	      "image":"",
	      "name":"Truth For Life Broadcasts"
	   },
	   r'(?i)Tumble Science':{
	      "stream":"https://rss.art19.com/tumble",
	      "image":"",
	      "name":"Tumble Science Podcast for Kids"
	   },
	   r'(?i)Turned.Out.+Punk':{
	      "stream":"https://audioboom.com/channels/3081610.rss",
	      "image":"",
	      "name":"Turned Out A Punk"
	   },
	   r'(?i)(Twenty Thousand|20000).+her':{
	      "stream":"http://20khz.libsyn.com/rss",
	      "image":"",
	      "name":"Twenty Thousand Hertz"
	   },
	   r'(?i)(U.S|US).+President':{
	      "stream":"http://feeds.feedburner.com/USPresidentsPodcast",
	      "image":"",
	      "name":"U.S. Presidents Podcast"
	   },
	   r'(?i)(U.S|US).+Supreme Court.+announce':{
	      "stream":"https://api.oyez.org/podcasts/opinion-announcements/2014",
	      "image":"",
	      "name":"U.S. Supreme Court Opinion Announcements"
	   },
	   r'(?i)(U.S|US).+Supreme Court.+argu':{
	      "stream":"https://api.oyez.org/podcasts/oral-arguments/2015",
	      "image":"",
	      "name":"U.S. Supreme Court Oral Arguments"
	   },
	   r'(?i)Jim Norton.+Matt Serra|(UFC|U.F.C) Unfiltered':{
	      "stream":"http://feeds.feedburner.com/ufc-unfiltered",
	      "image":"",
	      "name":"UFC Unfiltered with Jim Norton and Matt Serra"
	   },
	   r'(?i)Ultim.+Final.+Fantasy':{
	      "stream":"http://ultimafinalfantasy.libsyn.com/rss",
	      "image":"",
	      "name":"The Ultimate Final Fantasy Podcast"
	   },
	   r'(?i)Unbelievable':{
	      "stream":"http://unbelievable.podbean.com/feed/",
	      "image":"",
	      "name":"Unbelievable?"
	   },
	   r'(?i)Under The Hood':{
	      "stream":"http://www.underthehoodshow.com/rss/rss_1.xml",
	      "image":"",
	      "name":"Under The Hood"
	   },
	   r'(?i)Under The scale':{
	      "stream":"http://underthescales.libsyn.com/rss",
	      "image":"",
	      "name":"Under the Scales"
	   },
	   r'(?i)Understand.+Times':{
	      "stream":"http://www.oneplace.com/ministries/understanding-the-times/subscribe/podcast.xml",
	      "image":"",
	      "name":"Understanding the Times on OnePlace.com"
	   },
	   r'(?i)Unemployable|Brian Clark':{
	      "stream":"http://rainmaker.fm/series/unemployable/feed/",
	      "image":"",
	      "name":"Unemployable with Brian Clark"
	   },
	   r'(?i)Unexplained':{
	      "stream":"http://rss.acast.com/unexplained",
	      "image":"",
	      "name":"Unexplained"
	   },
	   r'(?i)Unprisoned|Stories From The System':{
	      "stream":"http://wwno.org/podcasts/90348/rss.xml",
	      "image":"",
	      "name":"Unprisoned: Stories From The System"
	   },
	   r'(?i)Unsolved Murders':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:224506341/sounds.rss",
	      "image":"",
	      "name":"Unsolved Murders: True Crime Stories"
	   },
	   r'(?i)UNspoiled':{
	      "stream":"http://www.spreaker.com/show/2043646/episodes/feed",
	      "image":"",
	      "name":"UNspoiled! Harry Potter"
	   },
	   r'(?i)UnStyled':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:261640883/sounds.rss",
	      "image":"",
	      "name":"UnStyled"
	   },
	   r'(?i)Up to date':{
	      "stream":"http://kcur.org/podcasts/20/rss.xml",
	      "image":"",
	      "name":"Up To Date"
	   },
	   r'(?i)Value Town':{
	      "stream":"http://feeds.feedburner.com/chanmanvtv/ValueTown",
	      "image":"",
	      "name":"Value Town - A Hearthstone Podcast"
	   },
	   r'(?i)Very(.|)pink':{
	      "stream":"http://verypink.libsyn.com/rss",
	      "image":"",
	      "name":"VeryPink Knits"
	   },
	   r'(?i)Chair(.|)borne.+Command':{
	      "stream":"http://feeds.feedburner.com/ChairborneCommandos",
	      "image":"",
	      "name":"Chairborne Commandos"
	   },
	   r'(?i)Wanted.+(FBI|F.b.i)':{
	      "stream":"https://www.fbi.gov/feeds/wanted-by-the-fbi-podcast/itunes.xml",
	      "image":"",
	      "name":"Wanted by the FBI podcast"
	   },
	   r'(?i)Warm Regards':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:235660424/sounds.rss",
	      "image":"",
	      "name":"Warm Regards"
	   },
	   r'(?i)(Watch What)':{
	      "stream":"http://feeds.sideshownetwork.tv/WatchWhatCrappens",
	      "image":"",
	      "name":"Watch What Crappens"
	   },
	   r'(?i)Watching Dead':{
	      "stream":"http://baldmove.com/feed/watching-dead/",
	      "image":"",
	      "name":"Watching Dead - Walking Dead Podcast"
	   },
	   r'(?i)Watching Westworld':{
	      "stream":"http://baldmove.com/feed/westworld",
	      "image":"",
	      "name":"Watching Westworld"
	   },
	   r'(?i)Porch Channel':{
	      "stream":"http://feeds.feedburner.com/WatermarkRadioPorchChannel",
	      "image":"",
	      "name":"Watermark Audio: The Porch Channel"
	   },
	   r'(?i)Way(.|)point Radio':{
	      "stream":"http://vicegamingnew.vice-media.libsynpro.com/rss",
	      "image":"",
	      "name":"Waypoint Radio"
	   },
	   r'(?i)We.+Hate.+Movie':{
	      "stream":"http://whmpodcast.libsyn.com/rss",
	      "image":"",
	      "name":"We Hate Movies"
	   },
	   r'(?i)We Study Billion':{
	      "stream":"http://theinvestorspodcast.libsyn.com/rss",
	      "image":"",
	      "name":"We Study Billionaires"
	   },
	   r'(?i)We.+See You.+Hell':{
	      "stream":"http://wellseeyouinhellpod.libsyn.com/rss",
	      "image":"",
	      "name":"We'll See You In Hell"
	   },
	   r'(?i)We.+re Alive':{
	      "stream":"http://rss.art19.com/were-alive-lockdown",
	      "image":"",
	      "name":"We're Alive: Lockdown"
	   },
	   r'(?i)Cliff Mass':{
	      "stream":"http://knkx.org/podcasts/term/2766/rss.xml",
	      "image":"",
	      "name":"Weather With Cliff Mass"
	   },
	   r'(?i)Week In Review':{
	      "stream":"http://kuow.org/podcasts/19654/rss.xml",
	      "image":"",
	      "name":"Week In Review"
	   },
	   r'(?i)Weekend Observation':{
	      "stream":"http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=17492726",
	      "image":"",
	      "name":"Weekend Observations with Stu & Jr."
	   },
	   r'(?i)Weekly Infusion':{
	      "stream":"http://weeklyinfusion.libsyn.com/rss",
	      "image":"",
	      "name":"Weekly Infusion"
	   },
	   r'(?i)What Should.+Read':{
	      "stream":"http://whatshouldireadnext.libsyn.com/rss",
	      "image":"",
	      "name":"What Should I Read Next?"
	   },
	   r'(?i)White House Press Briefing':{
	      "stream":"https://www.whitehouse.gov/podcast/audio/press-briefings/rss.xml",
	      "image":"",
	      "name":"White House Press Briefings (Audio)"
	   },
	   r'(?i)White House Speech':{
	      "stream":"https://www.whitehouse.gov/podcast/audio/speeches/rss.xml",
	      "image":"",
	      "name":"White House Speeches (Audio)"
	   },
	   r'(?i)Why Oh Why':{
	      "stream":"https://wfmu.org/podcast/LK.xml",
	      "image":"",
	      "name":"Why Oh Why"
	   },
	   r'(?i)Windows Weekly':{
	      "stream":"http://feeds.twit.tv/ww.xml",
	      "image":"",
	      "name":"Windows Weekly (MP3)"
	   },
	   r'(?i)Within.+Wires':{
	      "stream":"http://withinthewires.libsyn.com/rss",
	      "image":"",
	      "name":"Within the Wires"
	   },
	   r'(?i)W\.N\.P\.R|(WNPR)':{
	      "stream":"http://wnpr.org/podcasts",
	      "image":"",
	      "name":"WNPR"
	   },
	   r'(?i)Wolf(.|)(359|three fifty(.|)nine|three hundred fifty(.|)nine)':{
	      "stream":"http://wolf359radio.libsyn.com/rss",
	      "image":"",
	      "name":"Wolf 359"
	   },
	   r'(?i)Wom[ea]n.+Marvel':{
	      "stream":"http://marvel.com/podcasts/12/women_of_marvel_podcast/rss",
	      "image":"",
	      "name":"Women of Marvel Podcast"
	   },
	   r'(?i)Wood(.|)talk':{
	      "stream":"http://www.woodtalkshow.com/episodes/feed/",
	      "image":"",
	      "name":"Wood Talk"
	   },
	   r'(?i)Wood.+over':{
	      "stream":"http://feeds.podtrac.com/0YNYgrtCGEXR",
	      "image":"",
	      "name":"Wooden Overcoats"
	   },
	   r'(?i)Wool':{
	      "stream":"http://woolful.com/feed/podcast/",
	      "image":"",
	      "name":"Woolful"
	   },
	   r'(?i)Working.+Master(.|)plan':{
	      "stream":"http://workingonamasterplan.com/feed/podcast/",
	      "image":"",
	      "name":"Working On A Masterplan: Dating Up"
	   },
	   r'(?i)World Bank':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:81949595/sounds.rss",
	      "image":"",
	      "name":"World Bank Podcasts"
	   },
	   r'(?i)World Cafe':{
	      "stream":"http://www.npr.org/rss/podcast.php?id=510008",
	      "image":"",
	      "name":"World Cafe Words and Music from WXPN"
	   },
	   r'(?i)Wors.+Idea.+Time':{
	      "stream":"http://www.omnycontent.com/d/playlist/6e2a797b-0cc4-4c0b-a44d-a51e0019bc3c/3a51dc1f-d696-44f5-8bce-a51e0019f127/9af689bf-e634-4070-a49d-a51e001acb75/podcast.rss",
	      "image":"",
	      "name":"Worst Idea Of All Time Podcast"
	   },
	   r'(?i)Wrestl.+soup':{
	      "stream":"http://wrestlingsoup.com/ws/feed.xml",
	      "image":"",
	      "name":"WRESTLING SOUP"
	   },
	   r'(?i)Writ.+Excuse':{
	      "stream":"http://www.writingexcuses.com/feed/podcast/",
	      "image":"",
	      "name":"Writing Excuses"
	   },
	   r'(?i)Money(.|)Beat':{
	      "stream":"http://feeds.wsjonline.com/wsj/podcast_moneybeat",
	      "image":"",
	      "name":"WSJ MoneyBeat"
	   },
	   r'(?i)(WSJ|wall(.|)street).+Tech New':{
	      "stream":"http://feeds.wsjonline.com/wsj/podcast_wall_street_journal_tech_news_briefing",
	      "image":"",
	      "name":"WSJ Tech News Briefing"
	   },
	   r'(?i)(WSJ|wall(.|)street).+what.+new':{
	      "stream":"http://feeds.wsjonline.com/wsj/podcast_wall_street_journal_whats_news",
	      "image":"",
	      "name":"WSJ What's News"
	   },
	   r'(?i)your money matter':{
	      "stream":"http://feeds.wsjonline.com/wsj/podcast_your_money_matters",
	      "image":"",
	      "name":"WSJ Your Money Matters"
	   },
	   r'(?i)(Yer|you(.|)re) A Wizard Harry':{
	      "stream":"http://feeds.feedburner.com/potterpod",
	      "image":"",
	      "name":"Yer A Wizard Harry: The Harry Potter Bookclub"
	   },
	   r'(?i)you.+Not So Smart':{
	      "stream":"http://feeds.soundcloud.com/users/soundcloud:users:16745745/sounds.rss",
	      "image":"",
	      "name":"You Are Not So Smart"
	   },
	   r'(?i)Made It Weird|pete (holmes|homes)':{
	      "stream":"http://feeds.feedburner.com/YouMadeItWeird",
	      "image":"",
	      "name":"You Made It Weird with Pete Holmes"
	   },
	   r'(?i)You Must Remember This':{
	      "stream":"http://feeds.feedburner.com/MustRememberThis",
	      "image":"",
	      "name":"You Must Remember This"
	   },
	   r'(?i)You Need.+Budget':{
	      "stream":"http://youneedabudget.libsyn.com/rss",
	      "image":"",
	      "name":"You Need A Budget (YNAB)"
	   },
	   r'(?i)Chael Sonnen|you(.are|.re).+welcome':{
	      "stream":"http://feeds.feedburner.com/YoureWelcomeWithChaelSonnen",
	      "image":"",
	      "name":"You're Welcome! With Chael Sonnen"
	   },
	   r'(?i)Young House Love':{
	      "stream":"http://younghouselove.libsyn.com/rss",
	      "image":"",
	      "name":"Young House Love Has A Podcast"
	   },
	   r'(?i)Your Call':{
	      "stream":"http://kalw.org/podcasts/2094/rss.xml",
	      "image":"",
	      "name":"Your Call"
	   },
	   r'(?i)High Vibration':{
	      "stream":"http://greensmoothiegirl.com/feed/podcast/",
	      "image":"",
	      "name":"Your High Vibration Life"
	   },
	   r'(?i)Your Mom.+House':{
	      "stream":"http://feeds.feedburner.com/YourMomsHouseWithChristinaPazsitzkyAndTomSegura",
	      "image":"",
	      "name":"Your Mom's House with Christina Pazsitzky and Tom Segura"
	   },
	   r'(?i)Your Move|Andy Stanley':{
	      "stream":"http://feeds.feedburner.com/npm",
	      "image":"",
	      "name":"Your Move with Andy Stanley Podcast"
	   },
	   r'(?i)Your parent.+mojo':{
	      "stream":"http://yourparentingmojo.com/feed/podcast",
	      "image":"",
	      "name":"Your Parenting Mojo - Respectful, research-based parenting ideas to help kids thrive"
	   },
	   r'(?i)Week.+Radio.+Address.+President.+elect':{
	      "stream":"http://otrans.3cdn.net/6bfaeaf9e7cab15b8c_z6omv24jz.xml",
	      "image":"",
	      "name":"Your Weekly Radio Address from the President-elect"
	   },
	   r'(?i)Zen Parenting':{
	      "stream":"http://feeds.feedburner.com/ZenParentingRadio",
	      "image":"",
	      "name":"Zen Parenting Radio"
	   },
	   r'(?i)Zero Blog':{
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
		try:
			if re.search(re.compile(k),text):
				return  v
				break
		except:
			print(k)
	return response	
