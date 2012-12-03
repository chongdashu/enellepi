from bs4 import BeautifulSoup

class EnellepiEntry(object):
	def __init__(self, rawTitle, rawRating, rawText):
		self.rawTitle = rawTitle
		self.rawRating = rawRating
		self.rawText = rawText

data = []

filename = "1_com.rovio.angrybirdsstarwars.ads.iap.html";
file = open(filename)
soup = BeautifulSoup(file)

#review_texts = soup.find_all("p", "review-text")
#ratings = [t['title'] for t in soup.find_all("div", { "title": True })]

reviews = soup.find_all("div", "review-body-column goog-inline-block")
i = 0
for a_review in reviews:
	print str(i) + '\n'
	#a_review = reviews[0]
	title = a_review.find("h4").text
	rating = a_review.find_all("div", {"title" : True})[1]['title']
	text = a_review.find("p", "review-text").text
	datum = EnellepiEntry(title, rating, text)
	data.append(datum)
	i = i+1
