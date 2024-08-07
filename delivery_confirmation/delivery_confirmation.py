# delivery_confirmation.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/deliveryConfirmation', methods=['POST'])
def delivery_confirmation():
    data = request.get_json()
    # Process the delivery confirmation here
    return jsonify({"message": "Delivery Complete", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
