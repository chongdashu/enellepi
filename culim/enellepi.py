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

