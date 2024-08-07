# wishlist.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/wishlist', methods=['POST'])
def wishlist():
    data = request.get_json()
    # Process the order data here
    return jsonify({"message": "Wishlist saved", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
