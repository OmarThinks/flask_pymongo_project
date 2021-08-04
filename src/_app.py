from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.flask_pymongo

collection = db.test_collection




from flask import Flask, jsonify
#from json import dumps,loads
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self, o)


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
	id = inserted_product.inserted_id
	p = products.find_one({"_id":id})
	#print(p, flush=True)
	#print(type(p), flush=True)
	#print(str(p),flush=True)
	#print(dumps(p), flush=True)
	encoded = JSONEncoder().encode(p)
	print(type(encoded))
	return json.loads(encoded)






app.run(debug=True)
