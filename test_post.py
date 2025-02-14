import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "variance": 2.3,
    "skewness": 1.5,
    "curtosis": 0.1,
    "entropy": -1.2
}

response = requests.post(url, json=data)
print(response.json())  # Print the API response
