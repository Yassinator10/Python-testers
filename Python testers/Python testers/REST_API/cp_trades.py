# importing the requests library
import requests

# This disables insecure server warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# defining the api-endpoint
API_ENDPOINT = "https://localhost:5000/v1/api/iserver/account/trades"

# sending post request and saving response as response object
r = requests.get(url = API_ENDPOINT, verify=False)

# extracting response text
print(r.text)