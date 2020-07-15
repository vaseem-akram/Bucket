#!/usr/bin/python3


from threading import *
from socket import *
import optparse


print('-'*30,end='')
print('scanning ports and services using sockets',end='')
print('-'*30)

#returns the service version running on the port which is opened

def retbanner(tghost,port):
    s=socket.socket()
    s.connect(host,port)
    banner=s.recv(1024)
    if banner:
        return banner
    else:
        return None
#scans the host with given ports

def scan(tghost,port):
    sock=socket(AF_INET,SOCK_STREAM)
    try:
        if sock.connect((tghost,port)):
            
            print('{} is open'.format(port),end='')
            banner=retbanner(tghost,port)
            print(banner)
        else:
            print('{} is closed'.format(port))
    except Exception as e:
        print('oops '+str(e))

#funtion to provide option parsing and usuage of the program

def main():
    parser=optparse.OptionParser('usuage: <filename.py> -H <hostip> -P <portnumbers>')
    parser.add_option('-H',type='string',dest='tghost',help='specify host address')
    parser.add_option('-P',dest='tgport',type='string',help='specify ports seperated by comma')
    (options,args)=parser.parse_args()
    tghost=options.tghost
    tgports=str(options.tgport).split(',')
    if (tghost==None) | (tgports[0]==None):
        print(parser.usage)
        exit(0)
    for port in tgports:
        t=Thread(target=scan,args=(tghost,int(port)))
        t.start()
main()










