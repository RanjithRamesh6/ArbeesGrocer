# web_order.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webOrder', methods=['POST'])
def web_order():
    data = request.get_json()
    # Process the order data here
    return jsonify({"message": "Order Received", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
