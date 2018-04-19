import app
from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'library'
db = MongoAlchemy(app)

class Author(db.Document):
    name = db.StringField()

class Book(db.Document):
    title = db.StringField()
    author = db.DocumentField(Author)
    year = db.IntField()