import requests

url = "http://127.0.0.1:8000/login-user/"
headers = {'Content-Type': 'application/json'}

for i in range(55):
    response = requests.get(url, headers=headers)
    print(f"Request {i + 1}: Status Code {response.status_code}")
    if response.status_code == 429:
        print("Throttling is working: Too Many Requests")
        break
