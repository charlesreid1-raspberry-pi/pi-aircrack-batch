import subprocess, os, sys, time
from datetime import datetime

script_name = sys.argv[0]

# duration
Nseconds = 3600*2
 
# create a unique file prefix for this experiment
date_prefix = datetime.now().strftime('%Y-%m-%d_%H-%m')

# create a dir for this experiment
wifi = "/wifi/"+date_prefix

import socket
hostname = socket.gethostname()
file_prefix = hostname+'_'+date_prefix

print wifi
print ["mkdir","-p",wifi]
subprocess.call(["mkdir","-p",wifi])

print("[%s] About to put card in monitor mode."%(script_name) )
subprocess.call(['ifconfig','wlan0','down'])
subprocess.call(['iwconfig','wlan0','mode','managed'])
subprocess.call(['ifconfig','wlan0','up'])
print "Done."

time.sleep(5)

# construct the airodump command and pipe all its output to /dev/null so it doesn't blow up the syslog
FNULL = open(os.devnull,'w')
the_cmd = ['wifite','--all','--power','60','--mac','--quiet']

# call it
p = subprocess.Popen(the_cmd,
        stdout=FNULL, stderr=subprocess.STDOUT,
        cwd=wifi)

# wait for it
time.sleep(Nseconds)

# aaaaand bail 
p.kill()
 
print("[%s] Success!"%(script_name) )

