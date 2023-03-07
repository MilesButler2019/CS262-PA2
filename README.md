# CS262-PA2

# What didn't work

Throughout this assignment we first attempted to use subprocess similar to what varun mentioned in the lab on friday although we had issues trying to differentiate the machines (know what machine sent what). After a while we decided to stick to what we knew and just use threads and seperate files. Upon do this we were fine and made a consumer thread for each machine and were a bit confused on how to initalize all the machines and have them connect to eachother so we manually connected them which is less than ideal although we wanted to save time and do what worked. After this we were a bit confused on the the clockspeed but after looking on ed there were some similar question ands some nice classmates.


# Hypothesis

We hypothesized that machines that had lower clock speeds would expirience more drift than machines with higher clock speeds and thus have larger queues

# Expiriements

### Run Number 1
<img width="1135" alt="Screen Shot 2023-03-07 at 4 07 35 PM" src="https://user-images.githubusercontent.com/47306315/223552943-9c56dfac-00de-4d76-a12c-539349ffe787.png">


### Run Number 2
<img width="1135" alt="Screen Shot 2023-03-07 at 4 09 01 PM" src="https://user-images.githubusercontent.com/47306315/223553249-61c637ae-9f8d-46a2-95da-edcbebfea825.png">

### Run Number 3
<img width="1135" alt="Screen Shot 2023-03-07 at 4 11 39 PM" src="https://user-images.githubusercontent.com/47306315/223553767-63a661b4-1203-4c87-a781-b29439f39c7d.png">

### Run Number 4
<img width="1135" alt="Screen Shot 2023-03-07 at 4 16 39 PM" src="https://user-images.githubusercontent.com/47306315/223554814-25d4ce25-1191-40f6-867e-55a533cdfeb8.png">

### Run Number 5
<img width="1135" alt="Screen Shot 2023-03-07 at 4 20 45 PM" src="https://user-images.githubusercontent.com/47306315/223555546-646088cf-b436-4f60-8f0f-513c00b23840.png">


### Expiriement with reducing the clock speed variation and lowering the probability of a internal event to 50\%
<img width="1135" alt="Screen Shot 2023-03-07 at 4 28 27 PM" src="https://user-images.githubusercontent.com/47306315/223556943-0f1d5d35-129a-4638-8456-09d636492b0a.png">
