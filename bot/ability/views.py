from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
# Create your views here.
def test(request):
    resp ={}

    param = json.loads(request.body)
    print(param['post_type'])
    if param['post_type'] == 'message':
        print(param['message_type'])
        if param['message_type']=='group':
            gid = param['group_id']
            uid = param['sender']['user_id']
            message = param['raw_message']
            resp['group_id'] = gid
            resp['message'] = message
            requests.post("http://127.0.0.1:5700/send_group_message",data=resp)
    return JsonResponse({})