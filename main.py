import requests

api_key = "edf0fb3d23e04c0389fd023a6555b668"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-08-04&sortBy=publishedAt&apiKey=edf0fb3d23e04c0389fd023a6555b668"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])