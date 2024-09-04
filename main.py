import requests
from my_email import send_email

topic = "tesla"
api_key = "edf0fb3d23e04c0389fd023a6555b668"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-08-04&sortBy=publishedAt&apiKey=edf0fb3d23e04c0389fd023a6555b668&language=en"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"][:20]:
    body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + str(article["description"]) + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)