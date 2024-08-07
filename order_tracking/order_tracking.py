# order_tracking.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orderTracking', methods=['GET'])
def order_tracking():
    # Dummy tracking data
    tracking_data = {
        "order_id": "12345",
        "status": "In Transit"
    }
    return jsonify({"message": "Order Tracking", "data": tracking_data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
