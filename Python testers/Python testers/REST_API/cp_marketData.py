# importing the requests library
import requests
from time import sleep

# This disables insecure server warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# defining the api-endpoint
ACCOUNTS = "https://localhost:5000/v1/api/iserver/accounts"
CONTRACT = "https://localhost:5000/v1/api/iserver/contract/265598/info-and-rules"
MARKETDATA = "https://localhost:5000/v1/api/iserver/marketdata/snapshot?conids=265598&fields=31,84,86,6509"


accountDetails = requests.get(url = ACCOUNTS, verify=False)
accountResponse = accountDetails.text
print(f"ACCOUNTS Response: {accountResponse}\n")

sleep(1)

contractDetails = requests.get(url = CONTRACT, verify=False)
contractResponse = contractDetails.text
print(f"CONTRACT Response: {contractResponse}\n")

sleep(1)

mdDetails = requests.get(url = MARKETDATA, verify=False)
mdResponse = mdDetails.text
print(f"MD Response: {mdResponse}\n")