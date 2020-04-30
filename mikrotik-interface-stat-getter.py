#!/usr/bin/env python3
# Created by Constantine in 2020
# Details you can see here: https://infdots.blogspot.com/2020/04/mikrotik-mikrotik-api-telegraf-grafana.html (russian language)

import routeros_api
import time
import json
import sys

ip = '192.168.88.1'
user = 'apiuser'
password = 'StroNGp@5sW0rd!'
port = 8728

def getmetrics():
    try:
        connection = routeros_api.RouterOsApiPool(ip, port=port, username=user, password=password, plaintext_login=True)
        api = connection.get_api()

        listone = api.get_resource('/system/identity')
        listtwo = api.get_resource('/interface/')

        devicename = (listone.get()[0]['name'].replace(" ", ""))

        for i in listtwo.get():
            print ("mikrotik,device="+devicename+",interface="+i['name'].replace("<", "").replace(">", "")+\
            " rx-byte="+i['rx-byte']+" "+str(int(round(time.time() * 1000000000))))
            print ("mikrotik,device="+devicename+",interface="+i['name'].replace("<", "").replace(">", "")+\
            " tx-byte="+i['tx-byte']+" "+str(int(round(time.time() * 1000000000))))

        connection.disconnect()
    except:
        print ('Can not make connection onto router! Exit...')
        sys.exit(1)


if __name__ == "__main__":
    getmetrics()
