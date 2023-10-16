from pymongo import MongoClient


class DBconnect():
    def __init__(self):
        self.client = MongoClient(
            host = "mongodb:27017",
            serverSelectionTimeoutMS = 3000,
            username = "root",
            password = "password"
            )
        self.db = self.client["local"]
        self.collection = self.db["chatbot"]


    def vyhledat_intent(self, intent: str):
        document = self.collection.find_one({"intent": intent})
        return document["response_text"], document["is_action"], document["url"], document["url_text"], document["img_src"]


