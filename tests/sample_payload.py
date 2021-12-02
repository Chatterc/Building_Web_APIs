import requests
import json

# add review
review = "Star Wars the rise of skywalker was the biggest piece of trash ever brought to life in the franchise"
headers =  {"Content-Type": "application/json"}
payload = json.dumps({"review": review})

response = requests.post("http://127.0.0.1:8000/predict/",
                         headers=headers,
                         data = payload
                        )
print("Headers ", response.headers)
print("Status Code ", response.status_code)
print("Text ", response.text)

results = response.json()
print(results["prediction"])
print(results["probability"])
