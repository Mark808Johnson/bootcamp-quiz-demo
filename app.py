from sqlite3 import Time
from unicodedata import name
from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, time
from questions import selected_quiz, num_questions
from sqlalchemy import (Column, String, Integer, DateTime)
import time

app = Flask(__name__)
app.config["SECRET_KEY"] = 'bootcamp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Leaderboard(db.Model):
    __tablename__ = 'leaderboard'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    score = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return "<Leaderboard(name='%s', score='%s', date='%s')>" % (self.name, self.score, self.datetime)

# class Quiz(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question = db.Column(db.String(400), nullable=False)
#     option_a = db.Column(db.String(100), nullable=False)
#     option_b = db.Column(db.String(100), nullable=False)
#     option_c = db.Column(db.String(100), nullable=False)
#     answer = db.Column(db.String(100), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.id


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('login.html')
    
@app.route("/quiz", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        typed_password = request.form["password"]
        if typed_password == "bootcamp":
            session['logged in'] = True
            return render_template("quiz.html", selected_quiz=selected_quiz, num_questions=num_questions)
        else:
            # return render_template('login.html')
            flash("wrong password, please try again")
            return redirect(request.referrer)

# @app.route("/quiz", methods=["GET"])
# def quiz():
#     return render_template("quiz.html", selected_quiz=selected_quiz, num_questions=num_questions)    

@app.route("/results", methods=["GET", "POST"])
# def quiz_results():
#     correct_answers = 0
#     if request.method == "POST":
#         for item in selected_quiz:
#             answer = request.form.get(f"{item['q_id']}")
#             if answer == item["answer"]:
#                 correct_answers += 1
#     player_name = request.form["name"]
#     return render_template("results.html",correct_answers=correct_answers, num_questions=num_questions, name=player_name)


def quiz_results():
    correct_answers = 0
    if request.method == "POST":
        for item in selected_quiz:
            answer = request.form.get(f"{item['q_id']}")
            if answer == item["answer"]:
                correct_answers += 1
        player_name = request.form["name"]
        print(player_name)
        new_player = Leaderboard(name=player_name, score=correct_answers)
        db.session.add(new_player)
        db.session.commit()
        leaders = Leaderboard.query.order_by(Leaderboard.score.desc()).limit(5).all()
        return render_template("results.html",correct_answers=correct_answers, num_questions=num_questions, name=player_name, leaders=leaders)

if __name__ == "__main__":
    app.run(debug=True)

