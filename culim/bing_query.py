from pybing import Bing

bing = Bing('e4871cbebc4845288001c70e2ef5dad0')

response = bing.search_web('"very annoying" excellent')
print response['SearchResponse']['Web']['Total']

results = response['SearchResponse']['Web']['Results']

for result in results[:3]:
	print repr(result['Title'])