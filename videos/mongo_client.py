from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["video_uploader_db"]
videos_collection = db["videos"]