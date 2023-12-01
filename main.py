from src.gmaps import Gmaps
star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''

queries = ["coffee shops in san francisco"]
Gmaps.places(queries, max=100, min_reviews=5, max_reviews=100, has_phone=True, has_website=False, sort=[Gmaps.SORT_BY_REVIEWS_DESCENDING, Gmaps.SORT_BY_NOT_HAS_WEBSITE])
