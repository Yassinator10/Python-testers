# Library Imports
import requests
import time
import urllib3
import json

# Ignore insecure error messages
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Customer wants to receive a list of positions as soon as possible for the order fill

def main():
  
    order_url = "https://localhost:5000/v1/api/iserver/account/orders"
    postResponse = requests.get(url = order_url, verify=False)
    response = json.dumps(postResponse.json(), indent=2)
    print(response)

    
    order_url = "".join(["https://localhost:5000/v1/api/iserver/account/DU6962427/orders"])
    source_code = {
        "orders": [
            {

            "conid": 265598,

            "cOID": "RAOUZ_TEST_2",

            "listingExchange": "SMART",

            "ticker": "AAPL",

            "outsideRTH": True,




            "orderType": "LMT",

            "price":192,

            "side": "SELL",

            "tif": "DAY",

            "quantity":3,

            }
        ]
    }
    postResponse = requests.post(url = order_url, verify=False, json=source_code, headers={"Content-Type":"application/json"})
    response = json.dumps(postResponse.json(), indent=2)
    print(response)

    order_url = "https://localhost:5000/v1/api/iserver/account/orders"
    postResponse = requests.get(url = order_url, verify=False)
    response = json.dumps(postResponse.json(), indent=2)
    print(response)
if __name__ == "__main__":
    main()