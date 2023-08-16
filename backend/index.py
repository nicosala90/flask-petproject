from flask import Flask, request, jsonify
from pymongo import MongoClient
#from flask_pymongo import PyMongo
from bson.json_util import dumps
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost', 27017)
app.config['MONGO_URI'] = 'mongodb://localhost:27017'
#mongo = PyMongo(app)
db = client.todos_db
collection = db.todos

@app.get('/api/all-todos')
def get_all_todos():
    data = collection.find()
    data_list = list(data)
    serialized_data = dumps(data_list)  # Convert ObjectId to string representation
    return serialized_data, 200, {'Content-Type': 'application/json'}


@app.route('/add_data', methods=['POST'])
def add_data():
    # Get data from request
    data = request.json
    # Insert data into MongoDB
    collection.insert_one(data)
  
    return 'Data added to MongoDB'


""" @app.post('/api/add-todo')
def post_todo():
        todo = request.form['todo']
        degree = request.form['degree']
        db.insert_one({'todo': todo, 'degree': degree}) """

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)