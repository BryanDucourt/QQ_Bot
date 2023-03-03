from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
# Create your views here.
def test(request):
    resp ={}

    param = json.loads(request.body)
    if param['post_type'] == 'message':
        if param['message_type']=='group':
            print(param)
            gid = param['group_id']
            uid = param['sender']['user_id']
            resp['group_id'] = gid
            resp['message'] = f'[CQ:at,qq={uid}]爬啊你个寄吧'
            r = requests.post("http://127.0.0.1:5700/send_group_msg",data=resp)
    return JsonResponse({})