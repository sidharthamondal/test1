from flask import Flask, request,jsonify

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Flask app!'

@app.route('/submit-form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        # Logic to handle the form data sent via POST request
        data = request.form
        return 'Form submitted!'
    else:
        # Show the form page to user
        return 'This is the form. Please submit your data.'
    
@app.route('/process-json', methods=['POST'])
def process_json():
    if request.method == 'POST':
        # Parse JSON data sent with the request
        data = request.get_json()  # or request.json

        # You can now use the 'data' variable which is a Python dictionary
        # Example: data = {"name": "John", "age": 30}

        # Perform operations with the received JSON data
        name = data.get('name')
        response_data = {
            "message": f"Hello, {name}! Your data was received.How are you today"
        }

        # Respond with JSON data
        return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)
