from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.flask_pymongo

collection = db.test_collection




from flask import Flask, jsonify
from json import dumps,loads

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"




@app.route("/post")
def post_something():
	product = {"name":"Labtop", "price":50}
	products = db.products
	inserted_product = products.insert_one(product)
	# print(inserted_product, flush=True)
	# print(type(inserted_product), flush=True)
	print(inserted_product.inserted_id, flush=True)
	
	return jsonify({"success":True})






app.run(debug=True)
