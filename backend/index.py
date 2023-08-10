from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask(__name__)

client = MongoClient('localhost', 27017, username='username', password='password')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/todos_db'
mongo = PyMongo(app)
db = client.todos

@app.get('/api/all-todos')
def get_all-todos():
    data = db['todo_manager'].find()
    data_list = list(data)
    return jsonify(data_list)

@app.post('/api/add-todo')
def post_todo():
        todo = request.form['todo']
        degree = request.form['degree']
        db.insert_one({'todo': todo, 'degree': degree})
        

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)