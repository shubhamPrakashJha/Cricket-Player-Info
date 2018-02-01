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