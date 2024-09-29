from flask import Flask, jsonify, render_template
import json
import os  # Import the os module to access environment variables

app = Flask(__name__)

# Load the JSON data once when the app starts
with open("attractions.json", "r") as file:
    attractions = json.load(file)

@app.route('/', methods=['GET'])  # Define a route for the homepage
def home():
    return render_template('index.html')  # Render the index.html file

@app.route('/api/getAttractions', methods=['GET'])
def get_attractions():
    return jsonify(attractions)  # Serve the data as JSON

if __name__ == '__main__':
    # Run the app on the host and port specified by the environment variables
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
