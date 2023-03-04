from multiprocessing import Process
import os
import socket
from _thread import *
import threading
import time
from threading import Thread
import random
from clock import LambertClock

def consumer(conn,clock_speed):
    print("consumer accepted connection" + str(conn)+"\n")
    msg_queue=[]
    while True:
        time.sleep(clock_speed)
        data = conn.recv(1024)
        print("msg received\n")
        dataVal = data.decode('ascii')
        print("msg received:", dataVal)
        msg_queue.append(dataVal)
    

def producer(config):
    host= "127.0.0.1"
    port = int(config[2])
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sleepVal = 0.500
    #sema acquire
    try:
        s.connect((host,port))
        print("Client-side connection success to port val:" + str(config[2]) + "\n")

        while True:
            codeVal = str(code)
            time.sleep(sleepVal)
            s.send(codeVal.encode('ascii'))
            print("msg sent", codeVal)
            config[3].tick()
            print(config[3])

    except socket.error as e:
        print ("Error connecting producer: %s" % e)
 

def init_machine(config):
    HOST = str(config[0])
    PORT = int(config[1])
    print("starting server| port val:", PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    # print(config[-1])
    # print(config)
    config[-3].tick()
    while True:
        conn, addr = s.accept()
        start_new_thread(consumer, (conn,config[-2]))
 

def machine(config):
    config.append(os.getpid())
    global code
    #print(config)
    init_thread = Thread(target=init_machine, args=(config,))
    init_thread.start()
    #add delay to initialize the server-side logic on all processes
    time.sleep(5)
    # extensible to multiple producers
    prod_thread = Thread(target=producer, args=(config,))
    prod_thread.start()


    while True:
      code = random.randint(1,10)



localHost= "127.0.0.1"
 

if __name__ == '__main__':
    port1 = 2056
    port2 = 3056
    port3 = 4056

    clock_speed_1,clock_speed_2,clock_speed_3 = random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)
    clock1,clock2,clock3 = LambertClock("c1", "clock1_history.csv"),LambertClock("c2", "clock2_history.csv"),LambertClock("c3", "clock3_history.csv")
    config1=[localHost, port1, port2,clock1,clock_speed_1]
    p1 = Process(target=machine, args=(config1,))
    config2=[localHost, port2, port3,clock2,clock_speed_2]
    p2 = Process(target=machine, args=(config2,))
    config3=[localHost, port3, port1,clock3,clock_speed_3]
    p3 = Process(target=machine, args=(config3,))
    

    p1.start()
    p2.start()
    p3.start()
    

    p1.join()
    p2.join()
    p3.join()