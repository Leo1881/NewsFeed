import requests
from my_email import send_email

api_key = "edf0fb3d23e04c0389fd023a6555b668"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-08-04&sortBy=publishedAt&apiKey=edf0fb3d23e04c0389fd023a6555b668"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)