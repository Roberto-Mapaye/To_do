from application import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    complete = db.Column(db.String(10))
    task = db.Column(db.String(200))
