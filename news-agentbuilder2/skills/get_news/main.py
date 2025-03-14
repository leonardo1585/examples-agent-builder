from weni import Skill
from weni.context import Context
from weni.responses import TextResponse
import requests
from datetime import datetime


class GetNews(Skill):
    def execute(self, context: Context) -> TextResponse:
        apiKey = context.credentials.get("apiKey")
        
        topic = context.parameters.get("topic", "")
        news_response = self.get_news_by_topic(topic=topic, apiKey=apiKey)
        
        # Format the response
        articles = news_response.get("articles", [])
        if not articles:
            return TextResponse(data="Desculpe, não encontrei notícias sobre este assunto.")
        
        response_data = {
            "status": news_response.get("status"),
            "totalResults": len(articles[:10]),
            "articles": []
        }
        
        # Get only the first 10 articles
        for article in articles[:10]:
            article_data = {
                "source": article.get("source", {}),
                "author": article.get("author"),
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "urlToImage": article.get("urlToImage"),
                "publishedAt": article.get("publishedAt"),
                "content": article.get("content")
            }
            response_data["articles"].append(article_data)
            
        return TextResponse(data=response_data)

    def get_news_by_topic(self, topic, apiKey):
        url = f"https://newsapi.org/v2/everything"
        params = {
            "q": topic,
            "sortBy": "popularity",
            "apiKey": apiKey,
            "language": "pt"
        }
        response = requests.get(url, params=params)
        return response.json() 