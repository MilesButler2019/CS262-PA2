from multiprocessing import Process
import os
import socket
from _thread import *
import threading
import time
from threading import Thread
import random
import sys


clock = 0
LOG = -1
HOST = "127.0.0.1" # Being run on local host
PORTS = {1: 60000, 2: 60001, 3: 60002} # Ports for each machine
sockets = {}
connections = [(1,2),(1,3),(2,3)]


msg_queue=[]
que_lock = threading.Lock()

def consumer(conn):
    global msg_queue
    while True:
        data = conn.recv(1024)
        if not data:
            return
        try:
            receiving_time = int(data.decode())
            que_lock.acquire()
            msg_queue.append(receiving_time)
            que_lock.release()
        except ValueError:
            print("ValueError: Non-numeric message sent: " + data)


def tick(s1, s2,log_file):
    global msg_queue, clock, LOG
    if msg_queue:
        msg = msg_queue.pop(0)
        clock = max(msg, clock) + 1
        action = "recieved message"
    else:
        code = random.randint(1, 10)
        if code == 1:
            # TODO: Have some identification of s1 and s2 for logging
            action = "sent message to first"
            s1.sendall(str(clock).encode())
        elif code == 2:
            action = "sent message to second"
            s2.sendall(str(clock).encode())
        elif code == 3:
            action = "sent message to both"
            s1.sendall(str(clock).encode())
            s2.sendall(str(clock).encode())
        else:
            action = "sleep"
        clock += 1
    # print(time.strftime('%H:%M:%S', time.localtime()) + " / " + str(clock) + ": " + action)
    log_file.write(time.strftime('%H:%M:%S', time.localtime()) + ", " + str(clock) + ", " + action + ", " + str(len(msg_queue)) + "\n")
    # LOG.write(time.strftime('%H:%M:%S', time.localtime()) + " / " + str(clock) + ": " + action + "\n")
 


def connect_machine(machine_id,sockets):
        while True:
            err, s1 = get_socket(machine_id)
            if err == 0:
                break
        start_new_thread(consumer, (s1,))
        sockets.append(s1)

def bind_machine(sockets,machine_id,num_conns):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORTS[machine_id]))
    s.listen()
    conns = 0
    while conns < num_conns:
            conn, addr = s.accept()
            print('Connected to: ' + addr[0] + ':' + str(addr[1]))
            start_new_thread(consumer, (conn,))
            sockets.append(conn)
            conns += 1


def initialize(machine_id):
    log_txt = open("logs/log-" + str(machine_id) +".csv", "w")
    sockets = []

    # machine 1 waits for 2 connections
    if machine_id == 1:
        bind_machine(sockets,machine_id,2)

    # connect to machine 1
    elif machine_id == 2:
        bind_machine(sockets,machine_id,1)
        connect_machine(1,sockets)

    # connect to machine 1 + 2
    elif machine_id == 3:
        connect_machine(1,sockets)
        connect_machine(2,sockets)


    #Set random clock speed       
    clock_speed = random.randint(1, 6)
    start = time.time()
    period = 1.0 / clock_speed
    log_txt.write("Initialization Completed, Clock Speed " + str(clock_speed) + "\n")
    try:
        # time.sleep(machine_id / 100)
        while True:
            if (time.time() - start) > period:
                start += period
                tick(sockets[0], sockets[1],log_txt)
    finally:
        log_txt.close()

def get_socket(id):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORTS[id]))
        return 0, s
    except ConnectionRefusedError:
        return 1, "Connection Refused Error"
    except TimeoutError:
        return 1, "Timeout Error"
    except:
        return 2, "Server Connection Error"



def main():
    machine_id = int(sys.argv[1])
    if machine_id in [1, 2, 3]:
        initialize(machine_id)
    else:
        print("Must provide a valid process_id argument: 1, 2, 3")
        exit()

main()
