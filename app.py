from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from questions import random_questions 

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

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

num_questions = 5

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == "bootcamp":
             return render_template("quiz.html")     
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/quiz")
def quiz():
    random_selection = random_questions(num_questions)
    return render_template("quiz.html", data=random_selection, num=num_questions)    

@app.route("/results", methods=["GET", "POST"])
def quiz_results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)



