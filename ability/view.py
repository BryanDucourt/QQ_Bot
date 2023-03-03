from django.http import JsonResponse
import json

def test(request):
    resp ={}

    param = json.loads(request.body)
    if param['message_type'] == 'group':
        gid = param['group_id']
        uid = param