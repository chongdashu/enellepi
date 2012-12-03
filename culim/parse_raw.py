from bs4 import BeautifulSoup

class EnellepiEntry(object):
	def __init__(self, rawTitle, rawRating, rawText):
		self.rawTitle = rawTitle
		self.rawRating = rawRating
		self.rawText = rawText

		self.title = rawTitle
		self.rating = float(rawRating.split()[1])
		self.text = rawText

	def __repr__(self):
		return  self.title + " (" + str(self.rating) + ")\n" + self.text
	def __str__(self):
		return  self.title + " (" + str(self.rating) + ")\n" + self.text

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
	
	if a_review.find("p", "review-text") is not None:
		text = a_review.find("p", "review-text").text 
	else:
		text = ""
	datum = EnellepiEntry(title, rating, text)
	data.append(datum)
	i = i+1
