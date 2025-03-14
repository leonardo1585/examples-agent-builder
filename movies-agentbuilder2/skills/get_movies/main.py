from weni import Skill
from weni.context import Context
from weni.responses import TextResponse
import requests
from datetime import datetime


class GetMovies(Skill):
    def execute(self, context: Context) -> TextResponse:
        apiKey = context.credentials.get("movies_api_key")
        print("apikey", apiKey)
        
        movie_title = context.parameters.get("movie_title", "")
        movie_response = self.get_movie_by_title(title=movie_title, apiKey=apiKey)
        
        # Format the response
        results = movie_response.get("results", [])
        if not results:
            return TextResponse(data="Desculpe, não encontrei informações sobre este filme.")
        
        response_data = {
            "status": "success",
            "totalResults": len(results[:5]),
            "movies": []
        }
        
        # Get only the first 5 movies
        for movie in results[:5]:
            movie_data = {
                "id": movie.get("id"),
                "title": movie.get("title"),
                "original_title": movie.get("original_title"),
                "overview": movie.get("overview", ""),
                "release_date": movie.get("release_date"),
                "vote_average": movie.get("vote_average"),
                "poster_path": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get("poster_path") else None,
                "backdrop_path": f"https://image.tmdb.org/t/p/original{movie.get('backdrop_path')}" if movie.get("backdrop_path") else None
            }
            response_data["movies"].append(movie_data)
            
        return TextResponse(data=response_data)

    def get_movie_by_title(self, title, apiKey):
        url = f"https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": apiKey,
            "query": title
        }
        response = requests.get(url, params=params)
        return response.json() 