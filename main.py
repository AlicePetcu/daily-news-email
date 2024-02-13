import requests
from send_email import send_email

topic = "tesla"
api_key = "b6c84b9bd7f94625a3786f3edbf17de4"
url = (f"https://newsapi.org/v2/everything?q={topic}&from=2024-01-12&"
       "sortBy=publishedAt&apiKey=b6c84b9bd7f94625a3786f3edbf17de4&language=en")

# Make request
request = requests.get(url, verify=False)

# Get a dictionary with data
content = request.json()
message = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if article["title"] and article["description"] is not None:
        message = message + article["title"] \
                  + "\n" + article["description"] \
                  + "\n" + article["url"] + 2*"\n"

message = message.encode("utf-8")
send_email(message)

