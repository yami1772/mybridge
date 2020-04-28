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
global stoptime
global alarmcode

token = 'tempstring'
stoptime = 1588051718.6343422
alarmcode = 0

def switch(code):
    if code == '0':
        return '正常'
    elif code == '1':
        return 'error A '
    elif code == '2':
        return 'error B '
    elif code == '3':
        return 'error C'
    else:
        return 'unknown code'

def get_token():
    url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
    values = {
        'corpid':'ww715cb08e09d162c1',
        'corpsecret':'M0gRcLJYT1p04NcGIHNyLWjFLEv6zuQWJhsTYM17A9U',
        }
    req = requests.post(url, params=values) 
    data = json.loads(req.text)
    return data["access_token"]


def send_msg(sendstr):
    global token
    url ="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token
    values = """{
        "touser" : "@all",
        "msgtype":"text",
        "agentid":"1000004",
        "text":{
            "content": "%s"
        },
        }""" %(sendstr)
    req = requests.post(url, values)


def update_token():
    global token
    global stoptime
    token = get_token()
    if(time.time() < stoptime):
         Timer(7200, update_token).start()
    
def alarm():
    global stoptime
    global alarmcode
    with open('alarm_state.txt', 'r') as f:
        raw = f.read()
        alarmcode = raw[-1]
        zh_date = raw[:4]+'-'+raw[4:6]+'-'+raw[6:8]+'-'+raw[8:10]+'-'+raw[10:12]+'-'
    
    if(alarmcode !='0'):
        send_msg(zh_date + switch(alarmcode))
        
    if(time.time() < stoptime):
        Timer(5, alarm).start()
        
   
    
if __name__ == '__main__':
    update_token()
    alarm()
    
 
