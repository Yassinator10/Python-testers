# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "https://localhost:5000/v1/api/portfolio/DU5240685/summary"

# sending post request and saving response as response object
r = requests.get(url = API_ENDPOINT, verify=False)

# extracting response text
getResponse = r.text
print(f"Response: {getResponse}")
