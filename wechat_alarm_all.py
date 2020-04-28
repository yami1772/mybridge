# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:05:40 2020

@author: ZanWei
"""

import requests
import json
import time



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

# https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=
# ""
# "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=F73YZKH2PKkJhkEp6YxLJu9OghOUUO7ASSUXbw-yHEziw1zO8Ovx_vFnoR65HMjzt6_hgcpgjrpRWeHkje_ybbLeYIdF6D8V2UAb92xt3i7sJ9MTL_aYVQwe5Uio2IJWHYtbyIocllOdqaiFPQwksqDfdB8QvN2U0VI6vDJ8mvyY0xRMQhT1q77xI9AyeUDLjvdNilqHU8yp-_eMsQTiuw"
def send_msg():
    # url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=g_DPhvS0QJ83AH5JxkZ8g4XXszpjkSin43dAYqUAr1O170NDZBIcw4t4m4d-_lVSR7lOtNCHEsBkqokY_FiQnqVzC9qj2oqJHm0-OBqa1G2xwrEiVoaTJW0ZCLit6prH3DwekSNhSpl31j68HXqlJSgewxtKSG2GENml9lNlfZs6KoLW6uk_g9cFwSZ8rHHyPig_r9bJFMTDkoume0bQqA" 
    # + get_token()

    
    url ="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + get_token()
    values = {
   "touser" : "@all",
   "msgtype" : "text",
   "agentid" : '1000004',
   "text" : {
       "content" : "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
       },
   "safe":'0',
   }
    
    data = json.loads(values)
    req = requests.post(url, values)

if __name__ == '__main__':
    send_msg()


# values = """{"touser" : "ZanWei|17805426853","msgtype":"text","agentid":"1000002","text":{"content": "%s"},"safe":"0"}""" %(str("hhhhh"))
