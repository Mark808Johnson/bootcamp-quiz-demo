
from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from questions import selected_quiz, num_questions
from sqlalchemy import (Column, String, Integer, DateTime)

app = Flask(__name__)
app.config["SECRET_KEY"] = 'bootcamp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://scxgcphq:4dxxCFEVio2WToybGrb37Az42bbDi5YW@hattie.db.elephantsql.com/scxgcphq'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class leaderboard(db.Model):
    __tablename__ = 'leaderboard'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    score = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return "<leaderboard(name='%s', score='%s', date='%s')>" % (self.name, self.score, self.datetime)

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
            flash("wrong password, please try again")
            return redirect(request.referrer)

@app.route("/results", methods=["GET", "POST"])
def quiz_results():
    correct_answers = 0
    if request.method == "POST":
        for item in selected_quiz:
            answer = request.form.get(f"{item['q_id']}")
            if answer == item["answer"]:
                correct_answers += 1
        player_name = request.form["name"]
        new_player = leaderboard(name=player_name, score=correct_answers)
        db.session.add(new_player)
        db.session.commit()
        leaders = leaderboard.query.order_by(leaderboard.score.desc()).limit(5).all()
        return render_template("results.html",correct_answers=correct_answers, num_questions=num_questions, name=player_name, leaders=leaders)
        
if __name__ == "__main__":
    app.run(debug=True)

