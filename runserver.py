from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Will connect to mongodb running on localhost
mdb = MongoClient()

# app routes with accompanying methods go here

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 5555

    app.run(HOST, PORT, debug=True)
