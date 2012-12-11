from yahoo.search.news import NewsSearch
srch = NewsSearch('YahooDemo', query='kittens')
info = srch.parse_results()
info.total_results_available