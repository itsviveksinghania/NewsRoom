from .utils import *


def refresh():
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0c538b2e9e96474e85040466bb495e1e"
    get_news_from_api(url)
