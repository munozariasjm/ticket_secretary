import pymongo
from datetime import datetime


class MongoDataManager:
    def __init__(self, db_url, db_name):
        self.client = pymongo.MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db["user_flights"]

    def store_flight_data(self, username, route, price, flight_duration):
        record = {
            "username": username,
            "route": route,
            "price": price,
            "flight_duration": flight_duration,
            "timestamp": datetime.now(),
        }
        self.collection.insert_one(record)

    def get_flight_data(self, username):
        return list(self.collection.find({"username": username}))
