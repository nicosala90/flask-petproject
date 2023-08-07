from flask import Flask, render_template, redirect, request
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

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('client.html', result=result)
    return render_template('signup.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)