# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "https://localhost:5000/v1/api/iserver/account/{YOUR ACCOUNT ID}/orders"

# your source code here
source_code = {
  "orders": [
    {
      "acctId": "{YOUR ACCOUNT ID}",
      "conid": 265598,
      "orderType": "MKT",
      "side": "BUY",
      "tif": "DAY",
      "quantity": 1
    }
  ]
}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, verify=False, json=source_code)

# extracting response text
postResponse = r.text
print(f"Response: {postResponse}")
