from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/your-endpoint')
def analyze_text():
    input_text = request.args.get('input')
    num_words = len(input_text.split())
    return jsonify(result=f'The input contains {num_words} words.')

# Add a new route for handling validations
@app.route('/validate-result', methods=['POST'])
def validate_result():
    data = request.get_json()
    validation_type = data.get('validationType')
    # Here you would process the validation result, e.g., store it in a database
    print(f'Received validation: {validation_type}')
    return jsonify(status='success')
