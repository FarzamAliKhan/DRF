from django.http import JsonResponse
import json
from products.models import Product
from products.serializers import ProductSerializer


from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    # print(request.GET)   #echo params which are https://128.0.1.8000/?arg=value  last parts are query params
    # print(request.POST)     #echo forms/post
    # body = request.body      #byte string of JSON data
    # data = {}               #converting byte string into python dictionary
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # print(request.headers)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # print(data)
    """
    DRF VIEW
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #serialization -> converting django model
        # into python dict and returning json to client

        # data = model_to_dict(instance, fields= ['id','title','price','sale_price'])
        data = ProductSerializer(instance).data

    return Response(data)