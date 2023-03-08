# CS262-PA2
 CS262-PA2

# Overview
We start by initializing a simulation of a distributed system composed of three machines connected to each other over a network. The machines communicate with each other using sockets and exchange messages using a tick-based protocol.
The simulation is driven by a clock that determines the frequency of the ticks.
launches three separate Python processes, each running the same test.py script with a different argument val passed in as count. The subprocesses are started using subprocess.Popen() and the parent process waits for 20 seconds before killing them all.

The code is written in Python and uses the built-in socket library to create and manage sockets. The random and time libraries are also used to generate random clock speeds and to implement the clock, respectively.

# Requirements
To run the simulation, you will need Python 3 and the following libraries:

socket
random
time
threading

# Setup
Our script initializes three machines, each of which is assigned a unique ID (1, 2, or 3). Those machines are all connected to each other using sockets, and each machine runs a clock that maintains a global logical time across all the machines.

We first start by defining some global variables, including the clock time, the log file, the host IP, and the ports for each machine. We also initialize a message queue and a lock for synchronizing access to the queue.

The consumer function is a thread that receives messages from other machines and updates the message queue. 
Our main function is the tick function, which mainly advances the logical clock based on incoming messages or sends messages to other machines.

The connect_machine function is a thread that tries to connect to a specific machine until a successful connection is made. 

The bind_machine function binds to a specific port and accepts incoming connections until a specific number of connections are made. 

The initialize function initializes each machine by binding to the appropriate ports and connecting to the appropriate machines.

We defined a helper function, the get_socket function, to connect to a specific machine and returns an error code and socket object. Accordingly, our main function reads the machine ID from the command-line argument and initializes the appropriate machine.

# What didn't work

Throughout this assignment we first attempted to use subprocess similar to what varun mentioned in the lab on Friday although we had issues trying to differentiate the machines (know what machine sent what). After a while we decided to stick to what we knew and just use threads and seperate files. Upon do this we were fine and made a consumer thread for each machine and were a bit confused on how to initalize all the machines and have them connect to eachother so we manually connected them which is less than ideal although we wanted to save time and do what worked. After this we were a bit confused on the the clockspeed but after looking on ed there were some similar question ands some nice classmates.


# Hypothesis

We hypothesized that machines that had lower clock speeds would expirience a latger drift than machines with higher clock speeds and thus have larger queues. 

# Expiriements

### Run Number 1
<img width="1135" alt="Screen Shot 2023-03-07 at 4 07 35 PM" src="https://user-images.githubusercontent.com/47306315/223552943-9c56dfac-00de-4d76-a12c-539349ffe787.png">

Within this run we see that there are 2 machines with a much larger clock speed than machine 3. This appears to have filled up machine 3 queue and preventing it from sending messages or doing internal events and this preventing it from syconronizing its clock with the other machines causing a large drift in the left hand picture. While machines 1 and 2 appear to have their logical clocks synced quite well and no queue buildup. 

### Run Number 2
<img width="1135" alt="Screen Shot 2023-03-07 at 4 09 01 PM" src="https://user-images.githubusercontent.com/47306315/223553249-61c637ae-9f8d-46a2-95da-edcbebfea825.png">

Within this run it appears there was relativley low drift between the machines despite a decenet variation in clock speeds. The queue occasionally has a few messages for machine 2 which has the lowest clockspeed but utimetley clear the messages from the queue. This result goes against my hypothesis.


### Run Number 3
<img width="1135" alt="Screen Shot 2023-03-07 at 4 11 39 PM" src="https://user-images.githubusercontent.com/47306315/223553767-63a661b4-1203-4c87-a781-b29439f39c7d.png">

We see a large drift within machine 2 which there is an exterme clock difference between it and machines 1 and 3 which have speeds of 6 and 5 respectivley. It appears that machine 2's queue gets overflowed with messages and cannot keep up. 


### Run Number 4
<img width="1135" alt="Screen Shot 2023-03-07 at 4 16 39 PM" src="https://user-images.githubusercontent.com/47306315/223554814-25d4ce25-1191-40f6-867e-55a533cdfeb8.png">

Within this run it appears that machine 2 has a clockspeed of 1 and there exists some drift although not as much as in other cases. I think the reason is that there is a smaller variation of clock speeds and there isn't one machine thats significanlty different from the rest.


### Run Number 5
<img width="1135" alt="Screen Shot 2023-03-07 at 4 20 45 PM" src="https://user-images.githubusercontent.com/47306315/223555546-646088cf-b436-4f60-8f0f-513c00b23840.png">

Within this run there appears to be little to no drift occouring as all the machines have a relativley high clock speed and there is a smaller variation of clock speeds. 


### Expiriement with reducing the clock speed variation and lowering the probability of a internal event to 50\%
<img width="1135" alt="Screen Shot 2023-03-07 at 4 28 27 PM" src="https://user-images.githubusercontent.com/47306315/223556943-0f1d5d35-129a-4638-8456-09d636492b0a.png">


Within this expiriement we reduced the possible clock speeds from 1-3 rather than 1-6 and decreased the probabiity of an internal event from 70\% to 50\%. This resulted in relativley low drift but some buildup within the message queue. 




# Conclusion
We have concluded that our hypothsis was incorrect as drift doesn't depend on the low clock speeds but when there is high clock speed variations. To put this result in context of our class when running a distributed system it is important to use machines that have similar clock speeds or there will be issues with synchronization.

