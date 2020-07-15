from socket import *
import requests
import json
#Enter the target website name
inp=input('Enter the target webiste for information gathering:  ')
hostname=gethostbyaddr(inp)
hostip=gethostbyname(inp)

req=requests.get("https://"+inp)
#
try:
    if req.status_code==200:
        print("live")
except:
    print('error :'+req.status_code)
    exit(0)

#ipinfo.io -> API for info gathering
try:
    resp = requests.get("https://ipinfo.io/"+hostip+"/json")
except:
    print('invalid address might be')
    
#loads the information in dictionary format
resp2=json.loads(resp.text)

#prints the information side by side
for key,values in resp2.items():
    print(key+' :'+values)