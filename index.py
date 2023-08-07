from flask import Flask, render_template
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "password"

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

@app.route("/users/<user_id>")
def user_id(user_id):
    return "This user id is: " + user_id

@app.route("/signup")
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)