from django.shortcuts import render
from .utils import *


# Create your views here.

def home(request):
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0c538b2e9e96474e85040466bb495e1e"
    get_news_from_api(url)

    return render(request, "home.html", context={'articles': Articles.objects.all()})
