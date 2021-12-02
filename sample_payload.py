import requests
import json

# add review
review = "Star Wars the rise of skywalker was the biggest piece of trash ever brought to life in the franchise \
    I wish this movie never existed and that no one ever pays to see this movie in real life. Its was horrible \
    and ghastly. The acting was terrible, the story line awful, and there were so many plot holes \
    My one friend really loved it though..."
    
headers =  {"Content-Type": "application/json"}
payload = json.dumps({"review": review})

response = requests.post("http://127.0.0.1:8000/predict/",
                         headers=headers,
                         data = payload
                        )
print("Headers ", response.headers)
print("Status Code ", response.status_code)
print("Text ", response.text)
