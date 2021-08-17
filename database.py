from pymongo import MongoClient
mongoport = 27017
database_name = "house_price"
uri = f"mongodb://localhost:{mongoport}/{database_name}"
client = MongoClient(uri)
db = client[database_name]
house_detail = db['house_detail']

