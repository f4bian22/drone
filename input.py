import socket
import time
import threading



#adres van tello - altijd hetzelfde
tello = ('192.168.10.1', 8889)

#adres van locale pc - altijd hetzelfde
local = ('0.0.0.0',9010)

def init_drone():
 
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


 
def info(s):

    print('-----------Information------------')
    
    s.sendto("battery?".encode(), tello)
    response, ip_address = s.recvfrom(128)

    print('Battery: ',  response.decode(encoding='utf-8'))

#Snelheid
def snelheid(s):
    s.sendto('speed 80'.encode(), tello)
    

#Stijgen
def takeoff(s):
    s.sendto('takeoff'.encode(), tello)
    time.sleep(10)

#Hoogte
def omhoog(s):
    s.sendto('up 20'.encode(), tello)
    time.sleep(5)

def omlaag(s):
    s.sendto('down 20'.encode(), tello)
    time.sleep(5)

#RichtingBewegen
def links(s):
    s.sendto('left 20'.encode(), tello)
    time.sleep(5)

def rechts(s):
    s.sendto('right 20'.encode(), tello)
    time.sleep(5)

def vooruit(s):
    s.sendto('forward 20'.encode(), tello)
    time.sleep(5)

def achteruit(s):
    s.sendto('back 20'.encode(), tello)
    time.sleep(5)

#RondjeDraaien
def rondjeRechts(s):
    s.sendto('cw 360'.encode(), tello)

def rondjeLinks(s):
    s.sendto('ccw 360'.encode(), tello)

#Salto
def saltoLinksom(s):
    s.sendto('flip l'.encode(), tello)
    time.sleep(3)

def saltoRechtsom(s):
    s.sendto('flip r'.encode(), tello)
    time.sleep(3)

def saltoVooruit(s):
    s.sendto('flip f'.encode(), tello)
    time.sleep(3)

def saltoAchteruit(s):
    s.sendto('flip b'.encode(), tello)
    time.sleep(3)

#StilStaan
    s.sendto('stop'.encode(),tello)
    time.sleep(5)

#Landen
def land(s):
    s.sendto('land'.encode(), tello)
    time.sleep(5)




#invoer
def invoer(s):
    stop = False
    print('send in your command in apostrophes')
    while stop = False
        I1 = input()
        if I1 == "stop" :
            stop = True

        s.sendto(I1.encode(), tello)
        time.sleep(2)
    
    



#LichaamTest
 
def main():
    s = init_drone()

    takeoff(s)
    invoer(s)
    land(s)


 
if __name__ == '__main__':
    main()
   
    
