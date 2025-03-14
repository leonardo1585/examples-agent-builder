from weni import Skill
from weni.context import Context
from weni.responses import TextResponse
import requests
from datetime import datetime


class GetBooks(Skill):
    def execute(self, context: Context) -> TextResponse:
        apiKey = context.credentials.get("apiKey")
        
        book_title = context.parameters.get("book_title", "")
        books_response = self.get_books_by_title(title=book_title)
        
        # Format the response
        items = books_response.get("items", [])
        if not items:
            return TextResponse(data="Desculpe, não encontrei informações sobre este livro.")
        
        response_data = {
            "status": "success",
            "totalResults": len(items[:5]),
            "books": []
        }
        
        for book in items[:5]:
            volume_info = book.get("volumeInfo", {})
            book_data = {
                "id": book.get("id"),
                "title": volume_info.get("title"),
                "authors": volume_info.get("authors", []),
                "publisher": volume_info.get("publisher"),
                "publishedDate": volume_info.get("publishedDate"),
                "description": volume_info.get("description", ""),
                "pageCount": volume_info.get("pageCount"),
                "categories": volume_info.get("categories", []),
                "averageRating": volume_info.get("averageRating"),
                "ratingsCount": volume_info.get("ratingsCount"),
                "imageLinks": volume_info.get("imageLinks", {}),
                "language": volume_info.get("language"),
                "previewLink": volume_info.get("previewLink"),
                "infoLink": volume_info.get("infoLink")
            }
            response_data["books"].append(book_data)
            
        return TextResponse(data=response_data)

    def get_books_by_title(self, title):
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": title
        }
        response = requests.get(url, params=params)
        return response.json()
