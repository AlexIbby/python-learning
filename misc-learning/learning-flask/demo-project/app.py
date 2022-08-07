from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'


######DATABASE ITEMS #######

#Initialize the database 

db = SQLAlchemy(app)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

#Create a function to return a string when we add something 

def __repr__(self):
    return '<Name %r>' % self.id 

# add some shit to the database

from app import db
db.create_all()

from app import Movies

the_avengers = Movies(
    movie_title = "The Avengers",
    genre = "Action",
    release_date = "2007"
)

jurassic_park = Movies(
    movie_title = "Jurassic Park",
    genre = "Adventure",
    release_date = "1994"
)

db.session.add(the_avengers)
db.session.add(jurassic_park)
db.session.commit()



######DATABASE ITEMS END #######



@app.route('/')
def index():
    title = "Home Page"
    all_movies = Movies.query.all()
    return render_template("index.html", title=title, all_movies=all_movies)

