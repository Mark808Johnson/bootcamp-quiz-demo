from flask import Flask, render_template, request, url_for, redirect
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

@app.route("/")
def quiz():
    random_selection = random_questions()
    for item in random_selection:
    return render_template("index.html")    
        
@app.route("/results", methods=["POST"]


if __name__ == "__main__":
    app.run(debug=True)



