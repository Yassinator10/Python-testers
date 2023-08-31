# importing the requests library
import requests
from time import sleep

# This disables insecure server warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# defining the api-endpoint
PLACE_ORDER = "https://localhost:5000/v1/api/iserver/account/DU5240685/orders"
ORDER_STATUS = "https://localhost:5000/v1/api/iserver/account/orders"
DELETE_ORDER = "https://localhost:5000/v1/api/iserver/account/DU5240685/order/"

oidList = []
for i in range(4):
    # your source code here
    placeOrder = {
    "orders": [
        {
        "acctId": "DU5240685",
        "conid": 265598,
        "orderType": "LMT",
        "price":100,
        "quantity": 1,
        "side": "BUY",
        "tif":"DAY"
        }
    ]
    }

    # sending post request and saving response as response object
    orderRequest = requests.post(url = PLACE_ORDER, verify=False, json=placeOrder)

    # extracting response text
    postResponse = orderRequest.text
    orderId = postResponse.split(',')[0].split('"')[3]
    oidList.append(orderId)

# Order Status
orderStatus1 = requests.get(url = ORDER_STATUS, verify=False)
splitText = orderStatus1.text.split('},{')
for orderBracket in splitText:
    for oid in oidList:
        if oid in orderBracket:
            print(f"Order Retrieved: {orderBracket}")

# Cancel Order
for delOID in oidList:
    cancelOrder = DELETE_ORDER + delOID
    cancelRequest = requests.delete(url = cancelOrder, verify=False)

# Order Status 2
orderStatus2 = requests.get(url = ORDER_STATUS, verify=False)
splitText = orderStatus2.text.split('},{')
for orderBracket in splitText:
    for oid in oidList:
        if oid in orderBracket:
            print(f"Order Retrieved: {orderBracket}")