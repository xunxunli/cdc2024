from urllib.request import urlopen
import json

# Fetch the data from the API
url = 'http://tour-pedia.org/api/getReviewDetails?id=52a7393dae9eef5a5064019e'
response = urlopen(url).read()

# Decode the JSON response
data = json.loads(response)

# Access the "place" object and get the "id"
place_id = data['place']['id']

# Print the place id
print(f"Place ID: {place_id}")
