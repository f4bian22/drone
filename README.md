# drone

#Drone-flying-extravaganza

python 3.8 32-bit

base code below anything else is added.
Read documentation for further explanation on added code. Code not found in base nor documentation added in extdoc.txt

Code is created and used by u/f4bian22 & u/?


#import socket
#import time
#import threading

#adres van tello - altijd hetzelfde
#tello = ('192.168.10.1', 8889)

#adres van locale pc - altijd hetzelfde
#local = ('0.0.0.0',9010)

#def init_drone():
 
    # create upd client on PC
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as err:
        print(err)
        exit()
        
   #kopppelen
    s.bind(local)
   
    try:
        # send command om in de juiste modus te zetten
        s.sendto("command".encode(), tello)
        print('command')
        response, ip_address = s.recvfrom(128)
        print(response.decode(encoding='utf-8'))
        
        time.sleep(2)
        
    except socket.error as err:
        print(err)
 
    return s


 
#def info(s):

    print('-----------Informaiton------------')
    
    s.sendto("battery?".encode(), tello)
    response, ip_address = s.recvfrom(128)

    print('Battery: ',  response.decode(encoding='utf-8'))
   
 
#def takeoff(s):
    s.sendto('takeoff'.encode(), tello)
    time.sleep(10)
 
#def land(s):
    s.sendto('land'.encode(), tello)
    time.sleep(5)
 
#def main():
    s = init_drone()

    takeoff(s)
    info(s)
    land(s)


 
#if __name__ == '__main__':
    main()
