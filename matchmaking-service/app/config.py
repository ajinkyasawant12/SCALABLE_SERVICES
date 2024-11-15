import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/matchdb')
    USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://localhost:5000/users')