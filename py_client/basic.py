import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/"
   
get_Request = requests.get(endpoint)
print(get_Request.text)
print(get_Request.status_code)
