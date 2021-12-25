#usr/bin/ python3

import json
from types import resolve_bases
import requests
from colorama import Fore, Back, Style

greynoise_api_url = "https://api.greynoise.io/v3/community/"
greynoise_api = "DROP YOUR API KEY HERE"


#Scan IP and print response

def greynoise_scan():

    greynoise_headers = {"Accept": "application/json", 
    "key": greynoise_api}

    ip = input("Enter IP: ")
    print("")

    #Sending request to greynoise API 
    response = requests.request("GET", greynoise_api_url+ip, headers=greynoise_headers)

    #Printing response
    if response.status_code == 200:
        r = response.json()
        
        for i in response.json():

            if r['classification'] == "malicious":
                print(Fore.RED + i + ": " + str(response.json()[i]) + Style.RESET_ALL)
            elif r['classification'] == "benign":
                print(Fore.GREEN + i + ": " + str(response.json()[i]) + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + i + ": " + str(response.json()[i]) + Style.RESET_ALL)

    elif response.status_code == 400:
        print(Fore.RED + "Error: Request is not a valid routable IPv4 address : Error Code :  ", response.status_code)
    elif response.status_code == 401:
        print(Fore.RED + "Error: Authentication failed : Error Code :  ", response.status_code)
    elif response.status_code == 404:
        print(Fore.RED + "Error: IP not found in GreyNoise: Error Code :  ", response.status_code)
    elif response.status_code == 429:
        print(Fore.RED + "Error: Daily Rate-Limit Exceeded : Error Code :  ", response.status_code)
    elif response.status_code == 500:
        print(Fore.RED + "Error: Internal Server Error : Error Code :  ", response.status_code)

greynoise_scan()



    