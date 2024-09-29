from urllib.request import urlopen
import json

# Open and load the JSON file
print("Loading JSON file...")
with open("filtered_attraction_reviews.json", "r") as fp:
    reviews = json.load(fp)  # Load the JSON data into a Python list
print("Loaded JSON file successfully.")

# Iterate over each review item
for index, item in enumerate(reviews):
    print(f"Processing review {index + 1} of {len(reviews)}...")
    # Extract the "details" URL
    extracted_link = item.get("details")
    
    if extracted_link:  # Ensure the "details" key exists
        try:
            # Fetch the details from the URL
            print(f"Fetching details from: {extracted_link}")
            response = urlopen(extracted_link).read()
            review_details = json.loads(response)

            # Extract the place ID and add it to the item
            place_id = review_details['place']['id']
            item['place_id'] = place_id  # Add the place_id to the current review item
            
            print(f"Place ID for review {index + 1}: {place_id}")
        
        except Exception as e:
            print(f"Failed to fetch details for {extracted_link}: {e}")
            item['place_id'] = None  # Optionally set place_id to None if the fetch fails

# Write the updated data to a new JSON file
print("Writing updated data to the new JSON file (test_file.json)...")
with open("test_file2.json", "w") as fp:
    json.dump(reviews, fp, indent=4)  # Write the updated data with pretty formatting
print("Updated data written successfully to test_file.json.")

