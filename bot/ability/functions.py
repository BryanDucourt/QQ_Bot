import json

import requests

def on_jiba(uid,gid):
    resp = {'group_id': gid, 'message': f'[CQ:at,qq={uid}]爬啊你个寄吧'}
    r = requests.post("http://127.0.0.1:5700/send_group_msg", data=resp)

def on_idea(uid,gid,message):
    with open('ideas.txt','a') as f:
        f.write(f"user:{uid}; group:{gid}; idea:{message}\n")
        f.close()
    resp = {'group_id':gid,'message':f"[CQ:at,qq={uid}]听到了听到了，两个耳朵都听到了[CQ:face,id=187]"}
    r = requests.post("http://127.0.0.1:5700/send_group_msg", data=resp)

def on_empty(uid,gid):
    r = requests.post('http://127.0.0.1:5700/send_group_msg', data={'group_id':gid,'message':f"[CQ:at,qq={uid}]你在狗叫什么？"})