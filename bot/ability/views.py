from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
from functions import on_idea,on_jiba,on_empty
# Create your views here.
def test(request):
    param = json.loads(request.body)
    if param['post_type'] == 'message':
        if param['message_type']=='group':
            gid = param['group_id']
            raw_message = param['raw_message']
            uid = param['sender']['user_id']
            message = raw_message.split()

            code = message[0]
            if code=='/jiba':
                on_jiba(uid,gid)
            elif code == '/idea':
                if len(message)==1:
                    on_empty(uid,gid)
                else:
                    on_idea(uid,gid,message[1])
    return JsonResponse({})