import requests

api_key = "b6c84b9bd7f94625a3786f3edbf17de4"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-09&sortBy" \
      "=publishedAt&apiKey=b6c84b9bd7f94625a3786f3edbf17de4"

# Make request
request = requests.get(url, verify=False)

# Get a dictionary with data
content = request.json()

# Access article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
