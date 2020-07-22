#!/usr/bin/python3

import socket
from threading import *

#Function to grab the service running on that particular port
def retbanner(host,port):
    try:
        s=socket.socket()
        s.connect((host,port))
        banner=s.recv(5000)
        print('for port {} is  '.format(port)+banner.decode('utf-8'))
    except Exception as e:
        print(' for {}'.format(port)+'   '+str(e))
    




def main():
    
    host=input('Enter the Target ip:  ')
    print('the ip you entered'+host,end='')
    hostname=socket.gethostbyaddr(host)
    print(hostname)
    try:
        for port in range(20,50):
            t=Thread(target=retbanner,args=(host,port))
            t.start()
            t.join()
    except KeyboardInterrupt:
        print('----------keyboard interrupt------------')
    finally:
        print('--------------scan completed-------------')
main()
