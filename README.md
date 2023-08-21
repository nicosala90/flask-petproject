# TODO Application
This is a simple Todo application built using Flask (Python) for the backend and React.js for the frontend and it is connected to a Mongodb database. It allows you to create, delete, and mark tasks as completed.

# Installation
## Install Dependencies
Navigate to the project directory:
```
cd todo-app
```
 - Install the Python dependencies using pip:
```
pip install Flask
pip install pymongo
pip install flask-cors
```
- Install the JavaScript/React dependencies using npm:
```
npm install
```
- MongoDB Configuration
Ensure that you have MongoDB installed and running locally.
You can configure the MongoDB connection in the Flask app or provide environment variables for remote database connection.

# Run the Application

Start the Flask server:
```
python index.py
``` 
Start the React development server:
```
npm start
```

# Access the Application

Open your web browser and go to http://localhost:3000 to access the Todo app.
Usage
Create a new task by entering it in the input field and pressing Enter.
Mark a task as completed by clicking the checkbox.
Delete a task by clicking the delete icon.
Your tasks are stored in the MongoDB database.

# Additional Notes
The project has some issues with the delete and marks as completed the todos, the endpoints are working  some problem with the _id's in the frontend.
