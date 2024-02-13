import requests
from send_email import send_email

api_key = "b6c84b9bd7f94625a3786f3edbf17de4"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-12&sortBy=publishedAt&apiKey=b6c84b9bd7f94625a3786f3edbf17de4"

# Make request
request = requests.get(url, verify=False)

# Get a dictionary with data
content = request.json()
message = ""
for article in content["articles"]:
    print(type(article["title"]), type(article["description"]))
    message = message + article["title"] + "\n" + article["description"] + 2*"\n"

message = message.encode("utf-8")
send_email(message)

