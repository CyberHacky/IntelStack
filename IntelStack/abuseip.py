import requests
import json
from colorama import Fore, Back, Style

# Defining the api-endpoint

abuseip_url = 'https://api.abuseipdb.com/api/v2/check'
abuseip_api = "DROP YOUR API KEY HERE"


def abuseip_scan(): 
    
    headers = {
    'Accept': 'application/json',
    'Key': abuseip_api
    }

    ip = input("\nEnter IP: ")
    print("")

    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '365',
        'verbose': 'true'
    }

    #Sending request to greynoise API 
    response = requests.request(method='GET', url=abuseip_url, headers=headers, params=querystring)
    decodedResponse = json.loads(response.text)

    if response.status_code == 200:

        for i in decodedResponse:
                
                if decodedResponse['data']['isWhitelisted'] == True:
                    print(Fore.GREEN + i + ": " + str(decodedResponse[i]) + Style.RESET_ALL)
                elif decodedResponse['data']['isWhitelisted'] == False:
                    print(Fore.RED + i + ": " + str(decodedResponse[i]) + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + i + ": " + str(decodedResponse[i]) + Style.RESET_ALL)

    else:
        print(Fore.BLUE + "\n[!] Error Code : " + str(response.status_code) + Style.RESET_ALL)

        errors = decodedResponse.get('errors')
        for error in errors:
            print(Fore.RED + "{}".format(error.get('detail')) + Style.RESET_ALL)

        abuseip_scan()

abuseip_scan()






