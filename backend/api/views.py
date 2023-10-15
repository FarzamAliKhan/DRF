from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    print(request.GET)   #echo params which are https://128.0.1.8000/?arg=value  last parts are query params
    print(request.POST)     #echo forms/post
    body = request.body      #byte string of JSON data
    data = {}               #converting byte string into python dictionary
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    #print(request.headers)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse(data)