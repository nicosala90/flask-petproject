from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/users")
def home():
    obj = [
        {"name": "Béla",
        "age": 56},
        {"name": "Józsi",
        "age": 80}
        ]
    return render_template('users.html', obj=obj)

if __name__ == "__main__":
    app.run(debug=True)