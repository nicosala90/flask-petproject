from flask import Flask, request, jsonify
from pymongo import MongoClient
#from flask_pymongo import PyMongo

app = Flask(__name__)

client = MongoClient('localhost', 27017)
app.config['MONGO_URI'] = 'mongodb://localhost:27017'
#mongo = PyMongo(app)
db = client.todos_db
collection = db.todos

@app.get('/api/all-todos')
def get_all_todos():
    data = db['todo_manager'].find()
    data_list = list(data)
    return jsonify(data_list)

@app.post('/api/add-todo')
def post_todo():
        todo = request.form['todo']
        degree = request.form['degree']
        db.insert_one({'todo': todo, 'degree': degree})

@app.route('/add_data', methods=['POST'])
def add_data():
    # Get data from request
    data = request.json
  
    # Insert data into MongoDB
    collection.insert_one(data)
  
    return 'Data added to MongoDB'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)