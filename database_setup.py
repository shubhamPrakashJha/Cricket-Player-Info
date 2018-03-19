# Configuration file
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250), nullable=False)


# Class
class Team(Base):
    # Table info
    __tablename__ = 'team'

    # Mapper
    name = Column(String(250), nullable=False)
    image_url = Column(String(500))
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'image_url': self.image_url
        }


class Player(Base):
    # Table info
    __tablename__ = 'player'

    # mapper
    name = Column(String(120), nullable=False)
    id = Column(Integer, primary_key=True)
    role = Column(String(30))
    match = Column(String(30))
    runs = Column(String(30))
    high_score = Column(String(30))
    avg = Column(String(30))
    century = Column(String(30))
    fifty = Column(String(30))
    wickets = Column(String(30))
    bbm = Column(String(30))
    image_url = Column(String(500))
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship(Team)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'role': self.role,
            'match': self.match,
            'runs': self.runs,
            'high_score': self.high_score,
            'avg': self.avg,
            'century': self.century,
            'fifty': self.fifty,
            'wickets': self.wickets,
            'bbm': self.bbm,
            'image_url': self.image_url
        }


# configuration(end of file)

engine = create_engine('sqlite:///teamplayer.db')
Base.metadata.create_all(engine)
