ip=input('Enter the ip:  ') #ip address = 192.168.1.2
first=(ip.split('.')[0])   #192 first octet
second=(ip.split('.')[1])  #168 second octet
third=(ip.split('.')[2])   #1   thrid octet
fourth=(ip.split('.')[3])  #2   fourth 0ctet

#class A check
if '1'<=first<='126':    
    print('class A\n network starting address: '+first+'.0.0.0\n Broadcast address: '+first+'.255.255.255\n subnet mask: 255.0.0.0')
    print('Networks=126\nHosts=16,777,214')
elif int(first)=='0':
    print("doesn't starts with zero")


#local host check
elif first =='127': 
    print("local host address")
    
# NAT address check
elif  first=='192' and second=='168':
    print('private NAT addresses')
    print('Network starting address: '+first+'.'+second+'.'+third+'.'+'0\n' +'Broadcast address: '+first+'.'+second+'.'+third+'.'+'255')
    print('Networks=1\nHosts=254')
    
#class B check
elif '128'<=first<='192':
    print('class B\n'+'Network starting address: '+first+'.'+second+'.0.0')
    print('Broadcast address :'+first+'.'+second+'.255.255\n subnet mask: 255.255.0.0')
    print('Networks=16,384\nHosts=65,534')


#class C check
elif '193'<=first<='223':
    print('class C\n'+'Network starting address :'+first+'.'+second+'.'+third+'.0')
    print('broadcast address: '+first+'.'+second+'.'+third+'.'+ '255\n subnet mask: 255.255.255.0')
    print('Networks= 20,97,152\n Hosts=254')
#reserved class
elif first>='223':
    print('Reserved class undefined networks and hosts' )