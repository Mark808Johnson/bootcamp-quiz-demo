from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, Integer, DateTime)
import datetime

Base = declarative_base()

class Leaderboard(Base):
    __tablename__ = 'leaderboard'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    score = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    time = Column(DateTime, default=datetime.time)

    def __repr__(self):
        return "<Leaderboard(name='%s', score='%s', date='%s', time='%s')>" % (self.name, self.score, self.date, self.time)

