# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:51:03 2020

author: ZanWei
"""
import requests
import json
import time
from threading import Timer

global token
token = 'tempstring'

def get_token():
    url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
    values = {
        'corpid':'ww715cb08e09d162c1',
        'corpsecret':'M0gRcLJYT1p04NcGIHNyLWjFLEv6zuQWJhsTYM17A9U',
        }
    req = requests.post(url, params=values) 
    data = json.loads(req.text)
    return data["access_token"]


def send_msg():
    global token
    url ="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token
    values = """{
        "touser" : "@all",
        "msgtype":"text",
        "agentid":"1000004",
        "text":{
            "content": "%s"
        },
        }""" %(str("schedule msg"))
    req = requests.post(url, values)

def update_token():
    global token
    token = get_token()
    
def timer1():
    print('timer1:',time.asctime())
    
def timer2():
    print('timer2:',time.asctime())    
    
# if __name__ == '__main__':
    # update_token()
    # Timer(5, send_msg).start()
    # Timer(5, lambda:print(time.asctime())).start()
    # Timer(7200, update_token).start()
    # Timer(2, lambda:print('timer1:',time.asctime())).start()
    # Timer(3, lambda:print('timer1:',time.asctime())).start()
    

t1 = Timer(2, timer1)
t1.start()
# Timer(3, timer2).start()
    
