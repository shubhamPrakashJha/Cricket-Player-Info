#!/usr/bin/env python2.7

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player, User

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
engine = create_engine('sqlite:///teamplayerwithuser.db')
Base.metadata.bind = engine

# create staging zone for objects  loaded into the database session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Shubham Prakash Jha", email="prakash.shubhamjha@gmail.com",
             picture='https://lh3.googleusercontent.com/-sUFh0NulfGk/'
                     'AAAAAAAAAAI/AAAAAAAAABw/vot7H1BUFeE/s120-p-rw-no/'
                     'photo.jpg')
session.add(User1)
session.commit()

# Players for Team India
team1 = Team(user_id=1,
             name="India",
             image_url="https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/800px-Flag_of_India.svg.png")
session.add(team1)
session.commit()

player1 = Player(user_id=1,
                 name="MS Dhoni",
                 role="Wicketkeeper batsman",
                 match="312",
                 runs="9898",
                 high_score="183*",
                 avg="51.55",
                 century="10",
                 fifty="67",
                 wickets="1",
                 bbm="1/14",
                 image_url="http://www.espncricinfo.com/inline/content/"
                           "image/1099927.html?alt=20",
                 team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1,
                 name="Virat Kohli",
                 role="Top-order batsman",
                 match="202",
                 runs="9030",
                 high_score="183",
                 avg="55.74",
                 century="32",
                 fifty="45",
                 wickets="4",
                 bbm="1/15",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099912.html?alt=20",
                 team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1,
                 name="Ravichandran Ashwin",
                 role="Bowling allrounder",
                 match="111",
                 runs="675",
                 high_score="65",
                 avg="16.07",
                 century="0",
                 fifty="1",
                 wickets="150",
                 bbm="4/25",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099922.html?alt=17",
                 team=team1)
session.add(player3)
session.commit()

player5 = Player(user_id=1,
                 name="Shikhar Dhawan",
                 role="Opening batsman",
                 match="96",
                 runs="4038",
                 high_score="137",
                 avg="44.86",
                 century="12",
                 fifty="23",
                 wickets="0",
                 bbm="0",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099915.html?alt=20",
                 team=team1)
session.add(player5)
session.commit()

player6 = Player(user_id=1,
                 name="Mohammed Shami Ahmed",
                 role="Bowler",
                 match="50",
                 runs="116",
                 high_score="25",
                 avg="10.54",
                 century="0",
                 fifty="0",
                 wickets="91",
                 bbm="4/35",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099933.html?alt=1",
                 team=team1)
session.add(player6)
session.commit()

# Players for Team Australia
team2 = Team(user_id=1,
             name="Australia",
             image_url="https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Flag_of_Australia.svg/800px-Flag_of_Australia.svg.png")
session.add(team1)
session.commit()

player1 = Player(user_id=1,
                 name="MJ Clarke",
                 role="Middle-order batsman",
                 match="245",
                 runs="7981",
                 high_score="130",
                 avg="44.58",
                 century="8",
                 fifty="58",
                 wickets="57",
                 bbm="5/35",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/817097.html?alt=1",
                 team=team2)
session.add(player1)
session.commit()

player2 = Player(user_id=1,
                 name="GJ Bailey",
                 role="Top-order batsman",
                 match="90",
                 runs="3044",
                 high_score="156",
                 avg="40.58",
                 century="3",
                 fifty="22",
                 wickets="0",
                 bbm="0",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/817087.html?alt=1",
                 team=team2)
session.add(player2)
session.commit()

player3 = Player(user_id=1,
                 name="PJ Cummins",
                 role="Bowler",
                 match="39",
                 runs="144",
                 high_score="36",
                 avg="12.00",
                 century="0",
                 fifty="0",
                 wickets="64",
                 bbm="4/24",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099509.html?alt=1",
                 team=team2)
session.add(player3)
session.commit()

player4 = Player(user_id=1,
                 name="JP Faulkner",
                 role="Bowling allrounder",
                 match="69",
                 runs="1032",
                 high_score="116",
                 avg="34.40",
                 century="1",
                 fifty="4",
                 wickets="96",
                 bbm="4/32",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1030005.html",
                 team=team2)
session.add(player4)
session.commit()

player5 = Player(user_id=1,
                 name="AJ Finch",
                 role="Top-order batsman",
                 match="33",
                 runs="1132",
                 high_score="156",
                 avg="37.73",
                 century="1",
                 fifty="7",
                 wickets="0",
                 bbm="0",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099503.html?alt=1",
                 team=team2)
session.add(player5)
session.commit()

# Players for Team England
team3 = Team(user_id=1,
             name="England",
             image_url="https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/800px-Flag_of_the_United_Kingdom.svg.png")
session.add(team3)
session.commit()

player1 = Player(user_id=1,
                 name="MM Ali",
                 role="Batting allrounder",
                 match="68",
                 runs="1395",
                 high_score="128",
                 avg="28.46",
                 century="3",
                 fifty="5",
                 wickets="54",
                 bbm="3/32",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/751925.html?alt=1",
                 team=team3)
session.add(player1)
session.commit()

player2 = Player(user_id=1,
                 name="JM Anderson",
                 role="Bowler",
                 match="194",
                 runs="273",
                 high_score="28",
                 avg="7.58",
                 century="0",
                 fifty="0",
                 wickets="269",
                 bbm="5/23",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1015875.html",
                 team=team3)
session.add(player2)
session.commit()

player3 = Player(user_id=1,
                 name="JM Bairstow",
                 role="Middle-order batsman",
                 match="37",
                 runs="1149",
                 high_score="141*",
                 avg="45.96",
                 century="2",
                 fifty="6",
                 wickets="0",
                 bbm="0",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1015877.html",
                 team=team3)
session.add(player3)
session.commit()

player4 = Player(user_id=1,
                 name="GS Ballance",
                 role="Middle-order batsman",
                 match="16",
                 runs="297",
                 high_score="79",
                 avg="21.21",
                 century="0",
                 fifty="2",
                 wickets="0",
                 bbm="0",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/818163.html?alt=1",
                 team=team3)
session.add(player4)
session.commit()

player5 = Player(user_id=1,
                 name="IR Bell",
                 role="Top-order batsman",
                 match="161",
                 runs="5416",
                 high_score="141",
                 avg="37.87",
                 century="4",
                 fifty="35",
                 wickets="6",
                 bbm="3/9",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/565721.html?alt=1",
                 team=team3)
session.add(player5)
session.commit()

# # Players for Team
# team4 = Team(user_id=1,
# name="")
# session.add(team4)
# session.commit()
#
# player1 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team4)
# session.add(player1)
# session.commit()
#
# player2 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team4)
# session.add(player2)
# session.commit()
#
# player3 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team4)
# session.add(player3)
# session.commit()
#
# player4 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team4)
# session.add(player4)
# session.commit()
#
# player5 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team4)
# session.add(player5)
# session.commit()
#
# # Players for Team
# team5 = Team(user_id=1,
# name="")
# session.add(team5)
# session.commit()
#
# player1 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team5)
# session.add(player1)
# session.commit()
#
# player2 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team5)
# session.add(player2)
# session.commit()
#
# player3 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team5)
# session.add(player3)
# session.commit()
#
# player4 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team5)
# session.add(player4)
# session.commit()
#
# player5 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team5)
# session.add(player5)
# session.commit()
