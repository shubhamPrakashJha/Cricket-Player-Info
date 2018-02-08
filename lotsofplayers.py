from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
engine = create_engine('sqlite:///teamplayer.db')
Base.metadata.bind = engine

# create staging zone for objects  loaded into the database session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Players for Team India
team1 = Team(name="India")
session.add(team1)
session.commit()

player1 = Player(name="MS Dhoni",
                 role="Wicketkeeper batsman",
                 match="312",
                 runs="9898",
                 high_score="183*",
                 avg="51.55",
                 century="10",
                 fifty="67",
                 wickets="1",
                 bbm = "1/14",
                 team=team1)
session.add(player1)
session.commit()

player2 = Player(name="Virat Kohli",
                 role="Top-order batsman",
                 match="202",
                 runs="9030",
                 high_score="183",
                 avg="55.74",
                 century="32",
                 fifty="45",
                 wickets="4",
                 bbm = "1/15",
                 team=team1)
session.add(player2)
session.commit()

player3 = Player(name="Ravichandran Ashwin",
                 role="Bowling allrounder",
                 match="111",
                 runs="675",
                 high_score="65",
                 avg="16.07",
                 century="0",
                 fifty="1",
                 wickets="150",
                 bbm = "4/25",
                 team=team1)
session.add(player3)
session.commit()

player5 = Player(name="Shikhar Dhawan",
                 role="Opening batsman",
                 match="96",
                 runs="4038",
                 high_score="137",
                 avg="44.86",
                 century="12",
                 fifty="23",
                 wickets="0",
                 bbm="0",
                 team=team1)
session.add(player5)
session.commit()

player6 = Player(name="Mohammed Shami Ahmed",
                 role="Bowler",
                 match="50",
                 runs="116",
                 high_score="25",
                 avg="10.54",
                 century="0",
                 fifty="0",
                 wickets="91",
                 bbm="4/35",
                 team=team1)
session.add(player6)
session.commit()

# Players for Team Australia
team2 = Team(name="Australia")
session.add(team1)
session.commit()

player1 = Player(name="MJ Clarke",
                 role="Middle-order batsman",
                 match="245",
                 runs="7981",
                 high_score="130",
                 avg="44.58",
                 century="8",
                 fifty="58",
                 wickets="57",
                 bbm = "5/35",
                 team=team2)
session.add(player1)
session.commit()

player2 = Player(name="GJ Bailey",
                 role="Top-order batsman",
                 match="90",
                 runs="3044",
                 high_score="156",
                 avg="40.58",
                 century="3",
                 fifty="22",
                 wickets="0",
                 bbm = "0",
                 team=team2)
session.add(player2)
session.commit()

player3 = Player(name="PJ Cummins",
                 role="Bowler",
                 match="39",
                 runs="144",
                 high_score="36",
                 avg="12.00",
                 century="0",
                 fifty="0",
                 wickets="64",
                 bbm = "4/24",
                 team=team2)
session.add(player3)
session.commit()

player4 = Player(name="JP Faulkner",
                 role="Bowling allrounder",
                 match="69",
                 runs="1032",
                 high_score="116",
                 avg="34.40",
                 century="1",
                 fifty="4",
                 wickets="96",
                 bbm = "4/32",
                 team=team2)
session.add(player4)
session.commit()

player5 = Player(name="AJ Finch",
                 role="Top-order batsman",
                 match="33",
                 runs="1132",
                 high_score="156",
                 avg="37.73",
                 century="1",
                 fifty="7",
                 wickets="0",
                 bbm = "0",
                 team=team2)
session.add(player5)
session.commit()

# Players for Team England
team3 = Team(name="England")
session.add(team3)
session.commit()

player1 = Player(name="MM Ali",
                 role="Batting allrounder",
                 match="68",
                 runs="1395",
                 high_score="128",
                 avg="28.46",
                 century="3",
                 fifty="5",
                 wickets="54",
                 bbm = "3/32",
                 team=team3)
session.add(player1)
session.commit()

player2 = Player(name="JM Anderson",
                 role="Bowler",
                 match="194",
                 runs="273",
                 high_score="28",
                 avg="7.58",
                 century="0",
                 fifty="0",
                 wickets="269",
                 bbm = "5/23",
                 team=team3)
session.add(player2)
session.commit()

player3 = Player(name="JM Bairstow",
                 role="Middle-order batsman",
                 match="37",
                 runs="1149",
                 high_score="141*",
                 avg="45.96",
                 century="2",
                 fifty="6",
                 wickets="0",
                 bbm = "0",
                 team=team3)
session.add(player3)
session.commit()

player4 = Player(name="GS Ballance",
                 role="Middle-order batsman",
                 match="16",
                 runs="297",
                 high_score="79",
                 avg="21.21",
                 century="0",
                 fifty="2",
                 wickets="0",
                 bbm = "0",
                 team=team3)
session.add(player4)
session.commit()

player5 = Player(name="IR Bell",
                 role="Top-order batsman",
                 match="161",
                 runs="5416",
                 high_score="141",
                 avg="37.87",
                 century="4",
                 fifty="35",
                 wickets="6",
                 bbm = "3/9",
                 team=team3)
session.add(player5)
session.commit()

# # Players for Team
# team4 = Team(name="")
# session.add(team4)
# session.commit()
#
# player1 = Player(name="",
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
# player2 = Player(name="",
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
# player3 = Player(name="",
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
# player4 = Player(name="",
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
# player5 = Player(name="",
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
# team5 = Team(name="")
# session.add(team5)
# session.commit()
#
# player1 = Player(name="",
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
# player2 = Player(name="",
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
# player3 = Player(name="",
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
# player4 = Player(name="",
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
# player5 = Player(name="",
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

