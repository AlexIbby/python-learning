from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from getMovies import getMovie
import urllib.request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///themovies.db'


######DATABASE ITEMS #######

#Initialize the database 

db = SQLAlchemy(app)

class TheMovies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_title = db.Column(db.String(200), nullable=False)
    movie_overview = db.Column(db.String(200), nullable=False)
    cast = db.Column(db.String(200), nullable=False)
    director = db.Column(db.String(200), nullable=False)
    tmdb_id = db.Column(db.Integer, nullable=False)
    poster_path = db.Column(db.String(200), nullable=False)
    back_drop = db.Column(db.String(200), nullable=True)
    release_date = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

#Create a function to return a string when we add something 

def __repr__(self):
    return '<Name %r>' % self.id 

# add some shit to the database

from app import db
db.create_all()

from app import TheMovies

@app.route('/')
def index():
    title = "Home Page"
    all_movies = TheMovies.query.all()
    return render_template("index.html", title=title, all_movies=all_movies)

@app.route("/movie_added", methods=["POST"])
def movie_added():

    movie_add = request.form.get("movie_add")
    search_year = int(request.form.get("search_year"))

    #Getting Movie Data
    movie_result = getMovie(movie_add, search_year)

    xx_original_title = movie_result['original_title'] 
    xx_movie_overview = movie_result['movie_overview'] 
    xx_tmdb_id = movie_result['tmdb_id'] 
    xx_poster_path = movie_result['poster_path'] 
    xx_back_drop = movie_result['backdrop_path'] 
    xx_release_date = movie_result['release_date'] 
    xx_cast = movie_result['cast'] 
    xx_director = movie_result['director']

    #adding Movie to Database
    insert_movie = TheMovies(
    original_title = xx_original_title,
    movie_overview = xx_movie_overview,
    tmdb_id = xx_tmdb_id,
    poster_path = xx_poster_path,
    back_drop = xx_back_drop,
    release_date = xx_release_date,
    cast = xx_cast,
    director = xx_director)


    #Commit to Database
    db.session.add(insert_movie)
    db.session.commit()

    poster_file_name = str(movie_result['poster_path'])
    poster_file_name = poster_file_name.replace("/","")
    poster_file_name = "static"+"\\"+"images" + "\\" + poster_file_name
    posterUrl = "https://image.tmdb.org/t/p/w780"+ str(movie_result['poster_path'])
    urllib.request.urlretrieve(posterUrl, poster_file_name)



    title = "Movie Added!"
    return render_template("movie_added.html", 
    title=title, 
    movie_add=movie_add,
    movie_result = movie_result)