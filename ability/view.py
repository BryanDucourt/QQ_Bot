from django.http import JsonResponse
import json

def test(request):
    resp ={}

    param = json.loads(request.body)
    if param['message_type'] == 'group':
        gid = param['group_id']
        uid = param['sender']['user_id']
        message = param['raw_message']
        resp['group_id'] = gid
        resp['message'] = message
        return JsonResponse(resp)