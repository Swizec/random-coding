# Create your views here.

from django.http import HttpResponse

import json, redis

r = redis.Redis(host='localhost', port=6379, db=0)

def bench(request):
    data = json.loads(request.raw_post_data)
    value = r.get(data['key'])
    r.set(data['key'], data['value'])
    
    return HttpResponse(value)
