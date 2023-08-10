from flask import jsonify

class Todo(db.Document):
    todo = db.StringField()

    def to_json(param):
        return {"todo": param.todo,
                "degree": param.degree}