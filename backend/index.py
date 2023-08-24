from flask import Flask, request, jsonify
from pymongo import MongoClient

from bson.json_util import dumps
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost', 27017)
app.config['MONGO_URI'] = 'mongodb://localhost:27017'

db = client.todos_db
collection = db.todos

@app.get('/all-todos')
def get_all_todos():
    data = collection.find()
    data_list = list(data)
    serialized_data = dumps(data_list)  # Convert ObjectId to string representation
    return serialized_data, 200, {'Content-Type': 'application/json'}


@app.post('/add-data')
def add_data():
   
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"_id": str(result.inserted_id)}), 201


@app.patch('/update-todo-status/<string:todo_id>')
def update_todo_complete_status(todo_id):
    updated_todo_iscompleted = collection.find_one({"_id": ObjectId(todo_id)})
   
    myquery = {"_id": ObjectId(todo_id)}
    newvalues = { "$set": { "isCompleted": True } }
    collection.update_one(myquery, newvalues)

    return "Todo has benn updated to is completed"

@app.delete('/delete/<string:todo_id>')
def delete_todo(todo_id):
    print(todo_id)
    collection.delete_one({"_id": ObjectId(todo_id)})
    return "Todo has been deleted"


if __name__ == "__main__":
    app.run(debug=True)