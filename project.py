from flask import Flask
from flask import render_template
app = Flask(__name__)

# Fake teams
team = {'name': 'India','id': '1'}

teams = [{'name': 'India','id': '1'},
         {'name': 'Australia','id': '2'},
         {'name': 'England','id': '3'}]

# Fake players
player = [{'name': "MS Dhoni",'role': "Wicketkeeper batsman",'match': "312",'runs': "9898",'high_score': "183*",'avg': "51.55",'century': "10",'fifty': "67",'wickets': "1",'bbm': "1/14",'id': "1"}]

players = [
    {'name': "MS Dhoni",'role': "Wicketkeeper batsman",'match': "312",'runs': "9898",'high_score': "183*",'avg': "51.55",'century': "10",'fifty': "67",'wickets': "1",'bbm': "1/14",'id': "1"},
    {'name': "Virat Kohli",'role': " Top-order batsman",'match': "202",'runs': "9030",'high_score': "183",'avg': "55.74",'century': "32",'fifty': "45",'wickets': "4",'bbm': "1/15",'id': "1"},
    {'name': "Ravichandran Ashwin",'role': "Bowling allrounder",'match': "111",'runs': "675",'high_score': "65",'avg': "16.07",'century': "0",'fifty': "1",'wickets': "150",'bbm': "4/25",'id': "1"},
    {'name': "Shikhar Dhawan",'role': "Opening batsman",'match': "96",'runs': "4038",'high_score': "137",'avg': "44.86",'century': "12",'fifty': "23",'wickets': "0",'bbm': "0",'id': "1"},
    {'name': "Mohammed Shami Ahmed",'role': "Bowler",'match': "50",'runs': "116",'high_score': "25",'avg': "10.54",'century': "0",'fifty': "0",'wickets': "91",'bbm': "4/35",'id': "1"},
]


@app.route("/")
@app.route("/teams/")
def show_teams():
    # return "This page will show all Teams"
    return render_template('teams.html',teams=teams)

@app.route("/team/new/")
def new_team():
    # return "This page will create new Team"
    return render_template('newteams.html')

@app.route("/team/<int:team_id>/edit/")
def edit_team(team_id):
    # return "This page will edit Team %s" % team_id
    return render_template('editteams.html',team=team)

@app.route("/team/<int:team_id>/delete/")
def delete_team(team_id):
    # return "This page will delete Team %s" % team_id
    return render_template('deleteteams',team=team)

@app.route("/team/<int:team_id>/")
@app.route("/team/<int:team_id>/players/")
def show_players(team_id):
    # return "This page will show all players of Team %s" % team_id
    return render_template('players.html',team=team,players=players)

@app.route("/team/<int:team_id>/player/new/")
def new_player(team_id):
    # return "This page add new player in Team %s" % team_id
    return render_template('newplayers.html',team=team)

@app.route("/team/<int:team_id>/player/<int:player_id>/edit/")
def edit_player(team_id, player_id):
    # return "This page will edit player %s of Team %s" % (player_id, team_id)
    return render_template('editplayers.html',team=team,player=player)

@app.route("/team/<int:team_id>/player/<int:player_id>/delete/")
def delete_player(team_id, player_id):
    # return "This page will delete player %s of Team %s" % (player_id, team_id)
    return render_template('deleteplayer.html',team=team,player=player)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
