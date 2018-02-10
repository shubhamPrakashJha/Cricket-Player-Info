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
team1 = Team(name="India",
             image_url="data:image/png;base64,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")
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
                 bbm="1/14",
                 image_url="http://www.espncricinfo.com/inline/content/image/1099927.html?alt=20",
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
                 bbm="1/15",
                 image_url="http://www.espncricinfo.com/inline/content/image/1099912.html?alt=20",
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
                 bbm="4/25",
                 image_url="http://www.espncricinfo.com/inline/content/image/1099922.html?alt=17",
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
                 image_url="http://www.espncricinfo.com/inline/content/image/1099915.html?alt=20",
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
                 image_url="http://www.espncricinfo.com/inline/content/image/1099933.html?alt=1",
                 team=team1)
session.add(player6)
session.commit()

# Players for Team Australia
team2 = Team(name="Australia",
             image_url="data:image/jpeg;base64,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")
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
                 bbm="5/35",
                 image_url="http://www.espncricinfo.com/inline/content/image/817097.html?alt=1",
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
                 bbm="0", image_url="http://www.espncricinfo.com/inline/content/image/817087.html?alt=1",
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
                 bbm="4/24", image_url="http://www.espncricinfo.com/inline/content/image/1099509.html?alt=1",
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
                 bbm="4/32", image_url="http://www.espncricinfo.com/inline/content/image/1030005.html",
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
                 bbm="0", image_url="http://www.espncricinfo.com/inline/content/image/1099503.html?alt=1",
                 team=team2)
session.add(player5)
session.commit()

# Players for Team England
team3 = Team(name="England",
             image_url="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASIAAACuCAMAAAClZfCTAAAAM1BMVEX////OESQAAADMAANQUFDtvb9ABQvWEiXNABXuwcPTAAf2xMY/AABKOzxTU1PhjZEXFxea6ikiAAAB4ElEQVR4nO3aSU4DQQAEQYM3PBv+/2tB4jKWLOLYRmS8oJTnOrwHDqMHvL4SUYmoRPST6L6dBlmXCyzrqG3bfZdoO4wyT1eY5mHjtl2i07AV5+MbHM/Dxp1KJCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJ6DUS3ZzoNmzcPtE6n8e4fX4o0cfnbdC4ed0lWqbjICz03WjUtmnZJbpcvfT/uV5KBCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRPSTqgvXMwwWrI98zD0e+7qBPvcZjtlMxlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiP5NoG7Zinq4wzcPGbbtE9+00yLpcYFlHbdvuu0T5RYmoRFQiKhF9ARc3gVnveUO7AAAAAElFTkSuQmCC")
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
                 bbm="3/32", image_url="http://www.espncricinfo.com/inline/content/image/751925.html?alt=1",
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
                 bbm="5/23", image_url="http://www.espncricinfo.com/inline/content/image/1015875.html",
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
                 bbm="0", image_url="http://www.espncricinfo.com/inline/content/image/1015877.html",
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
                 bbm="0", image_url="http://www.espncricinfo.com/inline/content/image/818163.html?alt=1",
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
                 bbm="3/9", image_url="http://www.espncricinfo.com/inline/content/image/565721.html?alt=1",
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
