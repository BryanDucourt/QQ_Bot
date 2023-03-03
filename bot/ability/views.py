from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
# Create your views here.
def test(request):
    resp ={}

    param = json.loads(request.body)

    if param['post_type'] == 'message':
        r = requests.post("http://127.0.0.1:5700/get_msg", data={'message_id': param['message_id']})
        print(r.json())
        if param['message_type']=='group':
            gid = param['group_id']
            raw_message = param['raw_message']
            uid = param['sender']['user_id']
            message = raw_message.split()
            if len(message)!=1:
                code = message[0]
                if code=='/jiba':
                    resp['group_id'] = gid
                    resp['message'] = f'[CQ:at,qq={uid}]爬啊你个寄吧'
                    r = requests.post("http://127.0.0.1:5700/send_group_msg",data=resp)
    return JsonResponse({})