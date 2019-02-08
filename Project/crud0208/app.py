from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.init_app(app)

class Movie(db.Model):
    __tablename__ = "movies"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable = False, unique=True) #영화명
    title_en = db.Column(db.String, nullable = False) #영화명 영문
    audience = db.Column(db.Integer, nullable = False) # 누적 관객수
    open_date = db.Column(db.String, nullable = False) # 개봉일
    genre = db.Column(db.String, nullable = False) #장르
    watch_grade = db.Column(db.String, nullable = False) #관람등급
    score = db.Column(db.Float, nullable = False) #평점
    poster_url = db.Column(db.String, nullable = False) #포스터 이미지 url
    description = db.Column(db.String, nullable = False) #영화소개
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)

    
db.create_all()

@app.route('/')
def nothing():
    return redirect('/movies/')
    
@app.route('/movies/')
def base():
    m_list = Movie.query.all()
    
    return render_template('base.html', m_list = m_list)
    
@app.route('/movies/new')
def new():
    return render_template('new.html')
    
@app.route('/movies/create')
def create():
    title = request.args.get('title')
    title_en = request.args.get('title_en')
    audience = request.args.get('audience')
    open_date = request.args.get('open_date')
    genre = request.args.get('genre')
    watch_grade = request.args.get('watch_grade')
    score = request.args.get('score')
    poster_url = request.args.get('poster_url')
    description = request.args.get('description')
    
    movie = Movie(title=title, title_en=title_en, audience=audience,open_date=open_date, genre=genre, watch_grade=watch_grade,score=score, poster_url=poster_url, description=description, year=open_date[0:4], month=open_date[4:6], day=open_date[6:8])
    db.session.add(movie)
    db.session.commit()
    
    return redirect('/movies')

@app.route('/movies/<int:mov_id>')
def detail(mov_id):
    tempdate = datetime.datetime.now()
    movie = Movie.query.get(mov_id)
    datemsg = ""
    if movie.year != tempdate.year:
        datemsg = "{} 년 전".format(tempdate.year-movie.year)
    elif movie.month != tempdate.month:
        datemsg = "{} 개월 전".format(tempdate.month-movie.month)
    elif movie.day != tempdate.day:
        datemsg = "{} 일 전".format(tempdate.day-movie.day)
    else:
        datemsg = "오늘"
    return render_template('detail.html', movie=movie, datemsg = datemsg)
    
@app.route('/movies/<int:mov_id>/edit')
def edit(mov_id):
    movie = Movie.query.get(mov_id)
    return render_template('edit.html', movie=movie)
    
@app.route('/movies/<int:mov_id>/update')
def update(mov_id):
    title = request.args.get('title')
    title_en = request.args.get('title_en')
    audience = request.args.get('audience')
    open_date = request.args.get('open_date')
    genre = request.args.get('genre')
    watch_grade = request.args.get('watch_grade')
    score = request.args.get('score')
    poster_url = request.args.get('poster_url')
    description = request.args.get('description')
    
    movie = Movie.query.get(mov_id)
    movie.title = title
    movie.title_en = title_en
    movie.audience = audience
    movie.open_date = open_date
    movie.genre = genre
    movie.watch_grade = watch_grade
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    
    db.session.commit()
    return redirect('/movies')
    
@app.route('/movies/<int:mov_id>/delete')
def delete(mov_id):
    movie = Movie.query.get(mov_id)
    db.session.delete(movie)
    db.session.commit()
    
    return redirect('/movies')