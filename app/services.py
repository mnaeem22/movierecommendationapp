import requests

class TMDBService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def search_movie(self, query):
        url = f"{self.base_url}/search/movie"
        params = {"api_key": self.api_key, "query": query}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json().get('results', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching movie search results: {e}")
            return []

    def get_movie_recommendations(self, movie_id):
        url = f"{self.base_url}/movie/{movie_id}/recommendations"
        params = {"api_key": self.api_key}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json().get('results', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching movie recommendations: {e}")
            return []
