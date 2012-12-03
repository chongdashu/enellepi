from bs4 import BeautifulSoup
import enellepi

data = []

filename = "1_com.rovio.angrybirdsstarwars.ads.iap.html";
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
	data.append(datum)
	i = i+1