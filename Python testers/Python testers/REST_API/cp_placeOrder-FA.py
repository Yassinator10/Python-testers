# importing the requests library
import requests

# This disables insecure server warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# defining the api-endpoint
API_ENDPOINT = "https://localhost:5000/v1/api/iserver/account/Test_2/orders"

# your source code here
source_code = {
  "orders": [
    {
      "acctId": "DF74648",
      "conid": 575890378,
      "conidex": "conidex = 575890378",
      "secType": "secType = 575890378:STK",
      "cOID": "bulktrade_test_3_1",
      "price": 2.10,
      "side": "BUY",
      "ticker": "SNDL",
      "tif": "DAY",
      "quantity": 4,
      "useAdaptive": False,
      # "allocationMethod": "EqualQuantity",
      "isSingleGroup": False,
      "outsideRTH": False,
      "orderType": "MKT"
      }
  ]
}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, verify=False, json=source_code)

# extracting response text
postResponse = r.text
print(r)
print(f"Response: {postResponse}")
