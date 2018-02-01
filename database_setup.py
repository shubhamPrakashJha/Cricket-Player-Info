import os
import sys

# Configuration file
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Class
class Team(Base):
    # Table info
    __tablename__ = 'team'

    # Mapper
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)


class Player(Base):
    # Table info
    __tablename__ = 'player'

    # mapper
    name = Column(String(120), nullable=False)
    id = Column(Integer, primary_key=True)
    match = Column(Integer)
    runs = Column(Integer)
    high_score = Column(Integer)
    avg = Column(Integer)
    wickets = Column(Integer)
    century = Column(Integer)
    fifty = Column(Integer)
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship(Team)
