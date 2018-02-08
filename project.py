from flask import Flask
from flask import render_template,request,redirect,url_for
app = Flask(__name__)

from sqlalchemy import create_engine
engine=create_engine('sqlite:///teamplayer.db')

from database_setup import Base, Team, Player
Base.metadata.bind=engine

from sqlalchemy.orm import sessionmaker
DBSession=sessionmaker(bind=engine)
session=DBSession()


# Fake teams
# team = {'name': 'India','id': '1'}
#
# teams = [{'name': 'India','id': '1'},
#          {'name': 'Australia','id': '2'},
#          {'name': 'England','id': '3'}]
#
# # Fake players
#
#
# players = [
#     {'name': "MS Dhoni",'role': "Wicketkeeper batsman",'match': "312",'runs': "9898",'high_score': "183*",'avg': "51.55",'century': "10",'fifty': "67",'wickets': "1",'bbm': "1/14",'id': "1"},
#     {'name': "Virat Kohli",'role': " Top-order batsman",'match': "202",'runs': "9030",'high_score': "183",'avg': "55.74",'century': "32",'fifty': "45",'wickets': "4",'bbm': "1/15",'id': "2"},
#     {'name': "Ravichandran Ashwin",'role': "Bowling allrounder",'match': "111",'runs': "675",'high_score': "65",'avg': "16.07",'century': "0",'fifty': "1",'wickets': "150",'bbm': "4/25",'id': "3"},
#     {'name': "Shikhar Dhawan",'role': "Opening batsman",'match': "96",'runs': "4038",'high_score': "137",'avg': "44.86",'century': "12",'fifty': "23",'wickets': "0",'bbm': "0",'id': "4"},
#     {'name': "Mohammed Shami Ahmed",'role': "Bowler",'match': "50",'runs': "116",'high_score': "25",'avg': "10.54",'century': "0",'fifty': "0",'wickets': "91",'bbm': "4/35",'id': "5"}]
#
# player = {'name': "MS Dhoni",'role': "Wicketkeeper batsman",'match': "312",'runs': "9898",'high_score': "183*",'avg': "51.55",'century': "10",'fifty': "67",'wickets': "1",'bbm': "1/14",'id': "1"}
#
# roles = [p['role'] for p in players]

@app.route("/")
@app.route("/teams/")
def show_teams():
    teams=session.query(Team).all()
    # return "This page will show all Teams"
    return render_template('teams.html',teams=teams)

@app.route("/team/new/", methods=['GET','POST'])
def new_team():
    # return "This page will create new Team"
    if request.method=='POST':
        if request.form['name']:
            name=request.form['name']
            newTeam=Team(name=name)
            session.add(newTeam)
            session.commit()
        return redirect(url_for('show_teams'))
    else:
        return render_template('newteam.html')

@app.route("/team/<int:team_id>/edit/", methods=['GET','POST'])
def edit_team(team_id):
    # return "This page will edit Team %s" % team_id
    editedTeam = session.query(Team).filter_by(id=team_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedTeam.name = request.form['name']
        session.add(editedTeam)
        session.commit()
        return redirect(url_for('show_teams'))
    else:
        return render_template('editteam.html', team=editedTeam, team_id=team_id)

@app.route("/team/<int:team_id>/delete/", methods=['GET','POST'])
def delete_team(team_id):
    # return "This page will delete Team %s" % team_id
    deletedTeam = session.query(Team).filter_by(id=team_id).one()
    if request.method =='POST':
        session.delete(deletedTeam)
        session.commit()
        return redirect(url_for('show_teams'))
    else:
        return render_template('deleteteam.html',team=deletedTeam)

@app.route("/team/<int:team_id>/")
@app.route("/team/<int:team_id>/players/")
def show_players(team_id):
    # return "This page will show all players of Team %s" % team_id
    return render_template('players.html',team=team,players=players,roles=roles)

@app.route("/team/<int:team_id>/player/new/")
def new_player(team_id):
    # return "This page add new player in Team %s" % team_id
    return render_template('newplayer.html',team=team)

@app.route("/team/<int:team_id>/player/<int:player_id>/edit/")
def edit_player(team_id, player_id):
    # return "This page will edit player %s of Team %s" % (player_id, team_id)
    return render_template('editplayer.html',team=team,player=player)

@app.route("/team/<int:team_id>/player/<int:player_id>/delete/")
def delete_player(team_id, player_id):
    # return "This page will delete player %s of Team %s" % (player_id, team_id)
    return render_template('deleteplayer.html',team=team,player=player)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
