from flask import Flask, jsonify
from flask_restx import Resource
app = Flask(__name__)

@app.route('/test')
def get():
    return jsonify(response='Hello, World!')

@app.route('/banners')
def getBanners():
    banners = [{'customer_id': 1, 'banner_url': "blabla", 'banner_id' : 1} , {'customer_id': 1, 'banner_url': "abracadabra", 'banner_id' : 2}]
    return jsonify(response= banners)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8090', debug=True)