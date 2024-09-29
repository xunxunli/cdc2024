import requests
import json

category = "restaurant"
location = ""
name = ""

url = f"http://tour-pedia.org/api/getPlaces?category={category}&location={location}&name={name}"

headers = {"accept": "application/json"}

# Send the request and get the response
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response to a dictionary
    data = response.json()
    
    # Save the data to a JSON file
    with open('places.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)  # Pretty-print with indent=4
        print("Data has been saved to places.json")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

