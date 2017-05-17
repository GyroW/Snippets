import subprocess
import time
import os
occupant = ["Pi"]
address = ["b8:27:eb:cf:0e:a9"]


def scanner():
  while True:
    print("starting loop")
    output = subprocess.check_output("sudo arp-scan -l", shell=True)
  
    print ("starting scan")
    for i in range (len(address)):
      if address[i] in output:
        print(address[i])
        print(occupant[i])
 
      if "b8:27:eb:cf:0e:a9"  in output:
        print("") #do something
        #Person 1 MAC address
    time.sleep(60)
#os.system("sudo arp-scan -l")
scanner()
