def podcast_map(key):

	podcast_map = {
		"dlm" : "http://feeds.feedburner.com/DougLovesMovies",
		"jericho" : "http://www.podcastone.com/podcast?categoryID2=593",
		"stonecold" : "http://www.podcastone.com/podcast?categoryID2=436",
		"snap" : "http://feeds.wnyc.org/snapjudgment-wnyc"
	}
	return  podcast_map[key]

def podcast_img(img):
	podcast_map = {
		"dlm" : "https://cdn-radiotime-logos.tunein.com/p207738g.png",
		"jericho" : "http://webveeguide.com/wp-content/uploads/2016/01/talk-is-jericho.jpeg",
		"stonecold" : "https://www.podcastonesales.com/images/podcast/steveaustinunleashed1400x1400.jpg",
		"snap" : "https://media2.wnyc.org/i/1400/1400/l/80/1/wn16_wnycstudios_SnapJudgement.png"
	}
	return  podcast_map[img]
