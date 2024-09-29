import json

# Load the JSON data from the input file
with open('merged_attractions_pretty.json', 'r') as infile:
    # Load the entire content as a list of dictionaries
    attractions = json.load(infile)

# Dictionary to store unique attractions by id
unique_attractions = {}

# Iterate through each attraction
for attraction in attractions:
    attraction_id = attraction.get('id')
    
    # Check if the id is already in the dictionary
    if attraction_id not in unique_attractions:
        # Keep only the required fields
        unique_attractions[attraction_id] = {
            'name': attraction.get('name'),
            'address': attraction.get('address'),
            'id': attraction_id,
            'lat': attraction.get('lat'),
            'lng': attraction.get('lng')
        }

# Convert the unique attractions dictionary back to a list
processed_attractions = list(unique_attractions.values())

# Write the processed data to a new JSON file
with open('filtered_attractions_processed.json', 'w') as outfile:
    json.dump(processed_attractions, outfile, indent=4)

print("Processed attractions have been written to 'filtered_attractions_processed.json'")