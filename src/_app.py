from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.flask_pymongo

collection = db.test_collection
