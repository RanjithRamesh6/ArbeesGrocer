# order_confirmation.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/orderConfirmation', methods=['POST'])
def order_confirmation():
    data = request.get_json()
    # Process the confirmation data here
    return jsonify({"message": "Order Confirmed", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
