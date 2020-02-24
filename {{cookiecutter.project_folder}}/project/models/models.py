import datetime
from sqlalchemy import Column, Integer, String, DateTime
from project.models.init_db import db


class ExampleModel(db.Model):
    """Example model"""
    __tablename__ = 'example_model'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.now)
