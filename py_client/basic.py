import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"
   
get_Request = requests.get(endpoint, params={"abc":123}, json={"query":"hello world"})
#print(get_Request.text)
#print(get_Request.status_code)
print(get_Request.json())

