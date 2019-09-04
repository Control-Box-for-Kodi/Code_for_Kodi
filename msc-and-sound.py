#!/usr/bin/python
import httplib
import sys, argparse
import json
import time


time.sleep(10)

import serial
print("ROBIN INITI")
PI   = 'localhost'
PORT = 80
ser = serial.Serial('/dev/ttyUSB0', 115200)


version = 'v0.5.1'
headers = {"Content-type": "application/json", "Accept": "text/plain"}
#headers = {"Content-type": "application/json; charset=UTF-8"}
requ_obj = {"jsonrpc": "2.0", "id": 1, "method": "", "params":{}}
con = httplib.HTTPConnection(PI, PORT, timeout=5)


cmd = { "get_vol": {"method": "Application.GetProperties", "params": {"properties": ["volume"]}},
        "set_vol": {"method": "Application.SetVolume", "params": {"volume":100}},
        "mute": {"method": "Application.SetMute", "params":{"mute":"toggle"}},
        "pause": {"method": "Player.PlayPause", "params": { "playerid": 1 }},
        "stop": {"method": "Player.Stop", "params": { "playerid": 1 }},
        "pos": {"method": "Player.GetProperties", "params": {"properties": ["percentage"], "playerid": 1}},
        "home": {"method": "Input.home"},
        "back": {"method":"Input.Back"},
        "reboot": {"method":"System.Reboot"},
        "off": {"method":"System.Shutdown"}
        }

descr = {"get_vol": "returns actual volume",
        "set_vol": "set volume (0..100)",
        "mute": "toggle mute",
        "pause": "pause player",
        "stop": "stop playing",
        "pos": "show actual position in %",
        "home": "menu: returns to home screen",
        "back": "menu: one step back",
        "reboot": "reboot raspberry pi",
        "off": "shutdown raspberry pi"
        }

def send_request(req):
    req_par = requ_obj.copy()
    req_par.update(cmd[req])
    params = json.dumps(req_par)
    con.request("POST", "/jsonrpc", params, headers)
    resp = con.getresponse()

    if resp.status==200:
        ret = json.loads(resp.read())
        #print(ret)
        if ret['jsonrpc']==u'2.0':
            if ('return' in ret):
                print(ret['return'])
            if ('result' in ret):
                Value = ret['result']
                Next_status = str(Value)
                return Next_status
            if ('error' in ret):
                Value = "error"
                Next_status = str(Value)
                return Next_status
                print('!error:')
                print(ret['error'])
        else:
            print('!ERROR: no jsonrpc object.')
            print(ret)
    else:
        print(resp.status, resp.reason)
    



def main(): 
    Bike_watts= 0
    pause = "pause"
    isPlay = "{u'speed': 1}"
    isPause = "{u'speed': 0}"
    Error = "error"

    Status = send_request(pause)
    while(Status == Error):
        Status = send_request(pause)
    pass
    print(Status)
    send_request("set_vol")
    cmd['set_vol']['params']['volume']=40
    while (1):
         if(ser.in_waiting >0):
            line = ser.readline()
            Bike_watts = int(line)
            print(Bike_watts)
            
            if (Bike_watts < 40):
                if (Status == isPlay):
                    Status = send_request(pause)
                    send_request("set_vol")
                    cmd['set_vol']['params']['volume']=40

            if (Bike_watts >= 40) and (Bike_watts < 50): 
                if (Status == isPause):
                    Status = send_request(pause)
                if (Status == isPlay):
                    send_request("set_vol")
                    cmd['set_vol']['params']['volume']=50
                    print("ok 50")

            if (Bike_watts >= 50) and (Bike_watts < 60):
                if (Status == isPause):
                    Status = send_request(pause)
                if (Status == isPlay):
                    send_request("set_vol")
                    cmd['set_vol']['params']['volume']=60
                    print("ok 60")

            if (Bike_watts >= 60) and (Bike_watts < 70):
                if (Status == isPause):
                    Status = send_request(pause)
                if (Status == isPlay):
                    send_request("set_vol")
                    cmd['set_vol']['params']['volume']=70
                    print("ok 70")

            if (Bike_watts >= 70) and (Bike_watts < 80):
                if (Status == isPause):
                    Status = send_request(pause)
                if (Status == isPlay):
                    send_request("set_vol")
                    cmd['set_vol']['params']['volume']=80
                    print("ok 80")

            if (Bike_watts >= 80) and (Bike_watts < 90):
                if (Status == isPause):
                    Status = send_request(pause)
                if (Status == isPlay):
                    send_request("set_vol")
                    cmd['set_vol']['params']['volume']=90
                    print("ok 80")

            if (Bike_watts >= 90):
                if (Status == isPause):
                    Status = send_request(pause)
                if (Status == isPlay):
                    send_request("set_vol")
                    cmd['set_vol']['params']['volume']=100
                    print("ok 100")

            if (Status == Error):
                Status = send_request(pause)
    pass
   
    con.close()



if __name__ == '__main__':
    #sys.argv.extend(['get_vol','72'])
    main()
