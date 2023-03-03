from django.shortcuts import render
import json
from django.http import JsonResponse
# Create your views here.
def test(request):
    resp ={}

    param = json.loads(request.body)
    print(param['post_type'])
    if param['post_type'] == 'message':
        if param['message_type']=='group':
            gid = param['group_id']
            uid = param['sender']['user_id']
            message = param['raw_message']
            resp['group_id'] = gid
            resp['message'] = message
            return JsonResponse(resp)
    else:
        return JsonResponse(resp)