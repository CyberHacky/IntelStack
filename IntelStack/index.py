#!/usr/bin/env python3

import requests 
import urllib.request
import json                                # To use request package in current program 
import sys
import os
import csv
from urllib.parse import urlparse
import threading
from datetime import datetime



#Title print

logo = ('''

██╗███╗  ██╗████████╗███████╗██╗      ██████╗████████╗ █████╗ █████╗  ██╗  ██╗
██║████╗ ██║╚══██╔══╝██╔════╝██║     ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║ ██╔╝
██║██╔██╗██║   ██║   █████╗  ██║     ╚█████╗    ██║   ███████║██║  ╚═╝█████═╝
██║██║╚████║   ██║   ██╔══╝  ██║     ╚═══██╗    ██║   ██╔══██║██║  ██╗██╔═██╗
██║██║ ╚███║   ██║   ███████╗███████╗██████╔╝   ██║   ██║  ██║╚█████╔╝██║  ╚██╗
╚═╝╚═╝ ╚══╝   ╚═╝   ╚══════╝╚══════╝╚═════╝    ╚═╝   ╚═╝   ╚═╝ ╚════╝ ╚═╝   ╚═╝
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[!] This Tool Must Run As ROOT [!]         Created By : SecFirm Team\n\n

Note : Configure Threat Intelligence Platforms API in Json File ''')



# Provide Custom Browser headers
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

# Print Logo on startup
print(logo)


#Main Menu

def mainmenu():
    print ("""
   {1}--IP Analysis
   {2}--Domain Analysis
   {3}--File Analysis
   {0}--Exit
 """)
    choice = input("IntelStack~# ")
    if choice == "1":
        ipmenu()
    elif choice == "2":
        domainmenu()
    elif choice == "3":
        filemenu()
    elif choice == "0":
        print("Thanks for Using IntelStack")
        os.system('cls'), sys.exit()
    elif choice == "":
        print(logo)
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        mainmenu()
    else:
        print(logo)
        mainmenu()

# Run Website Pentesting HERE



def ipmenu():

    print ("""
   {1}--GreyNoise
   {2}--AbuseIP
   {3}--OTX
   {4}--VirusTotal
   {5}--ALL TI PLATFORMS
   {0}--Back to Main Menu
   {99}--Exit
 """)
    choice = input("IntelStack~# ")
    if choice == "1":
        greynoise()
    elif choice == "2":
        abuseip()
    elif choice == "3":
        otx()
    elif choice == "4":
        virustotal()
    elif choice == "5":
        allti()
    elif choice == "0":
        os.system('cls')
        print(logo)
        mainmenu()
    elif choice == "99":
        print("Thanks for Using IntelStack")
        os.system('clear'), sys.exit()
    elif choice == "":
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        webmenu()
    else:
        print(logo)
        webmenu()

mainmenu()