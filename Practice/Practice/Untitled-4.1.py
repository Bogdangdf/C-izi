import requests

get_url = "https://httpbin.org/get"
get_response = requests.get(get_url)

print(get_response.status_code)
print(get_response.headers)
print(get_response.text)

post_url = "https://httpbin.org/post"
data = {
    "name": "test",
    "value": 123
}

post_response = requests.post(post_url, json=data)

print(post_response.status_code)
print(post_response.headers)
print(post_response.text)
