# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:51:03 2020

@author: ZanWei
"""
import requests
import json
# import time

def get_token():
    url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
    values = {
        'corpid':'ww715cb08e09d162c1',
        'corpsecret':'M0gRcLJYT1p04NcGIHNyLWjFLEv6zuQWJhsTYM17A9U',
        }
    req = requests.post(url, params=values) 
    data = json.loads(req.text)
    return data["access_token"]

# F73YZKH2PKkJhkEp6YxLJu9OghOUUO7ASSUXbw-yHEziw1zO8Ovx_vFnoR65HMjzt6_hgcpgjrpRWeHkje_ybbLeYIdF6D8V2UAb92xt3i7sJ9MTL_aYVQwe5Uio2IJWHYtbyIocllOdqaiFPQwksqDfdB8QvN2U0VI6vDJ8mvyY0xRMQhT1q77xI9AyeUDLjvdNilqHU8yp-_eMsQTiuw

def send_msg():
    url ="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + get_token()
    values = """{
        "touser" : "@all",
        "msgtype":"text",
        "agentid":"1000004",
        "text":{
            "content": "%s"
        },
        }""" %(str("test done"))
    
    # data = json.loads(values)
    req = requests.post(url, values)

if __name__ == '__main__':
    send_msg()


# values = """{"touser" : "ZanWei|17805426853","msgtype":"text","agentid":"1000002","text":{"content": "%s"},"safe":"0"}""" %(str("hhhhh"))
