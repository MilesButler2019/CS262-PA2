import subprocess
import concurrent.futures
import time

# set a timeout of 100 seconds
timeout = 10



files = ['test.py','test.py','test.py']


def run_file(filename,val):
    subprocess.run(['python', filename,val])


start_time = time.time()

processes = []

# start a separate process for each script
count = 1 
for script in files:
    process = subprocess.Popen(['python', script, str(count)])
    count += 1
    processes.append(process)


time.sleep(90)

for i in processes:
    i.kill()