from bs4 import BeautifulSoup
import enellepi
import pickle

#data = []
data_free = []
data_paid = []

def parse_file(filename, list):
	# filename = "1_com.rovio.angrybirdsstarwars.ads.iap.html";
	file = open(filename)
	soup = BeautifulSoup(file)

	reviews = soup.find_all("div", "review-body-column goog-inline-block")
	i = 0
	for a_review in reviews:
		print str(i) + '\n'
		#a_review = reviews[0]
		title = a_review.find("h4").text
		rating = a_review.find_all("div", {"title" : True})[1]['title']
		
		if a_review.find("p", "review-text") is not None:
			text = a_review.find("p", "review-text").text 
		else:
			text = ""
		datum = enellepi.EnellepiEntry(title, rating, text)
		# data.append(datum)
		list.append( { "title" : datum.title, "rating" : datum.rating, "text" : datum.text})
		i = i+1

	file.close()

filenames = [	
	"1_com.rovio.angrybirdsstarwars.ads.iap.html", 
	"2_com.imangi.templerun.html",
	"3_com.fingersoft.hillclimb.html"
]

filenames2 = [
	"1_com.disney.wreckitralph.html",
	"2_com.ea.monopolymillionaire_na.html",
	"3_com.mojang.minecraftpe.html",
	"4_air.ClearVision17.html",
	"5_com.disney.WMW.html",
	"6_com.rockstar.gta3.html"
]

for filename in filenames:
	parse_file('raw-reviews/'+filename, data_free)

for filename in filenames2:
	parse_file('raw-reviews/'+filename, data_paid)

file = open("topfree.dat", 'w')
pickle.dump(data_free, file)
file.close()

file = open("toppaid.dat", 'w')
pickle.dump(data_paid, file)
file.close()
