from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/teams/")
def show_players():
    return "This page will show all Teams"


@app.route("/team/new/")
def new_team():
    return "This page will create new Team"


@app.route("/team/<int:team_id>/edit/")
def edit_team(team_id):
    return "This page will edit Team %s" % team_id


@app.route("/team/<int:team_id>/delete/")
def delete_team(team_id):
    return "This page will delete Team %s" % team_id


@app.route("/team/<int:team_id>/")
@app.route("/team/<int:team_id>/players/")
def show_players(team_id):
    return "This page will show all players of Team %s" % team_id


@app.route("/team/<int:team_id>/player/new/")
def new_player(team_id):
    return "This page add new player in Team %s" % team_id


@app.route("/team/<int:team_id>/player/<int:player_id>/edit/")
def edit_player(team_id, player_id):
    return "This page will edit player %s of Team %s" % (player_id, team_id)


@app.route("/team/<int:team_id>/player/<int:player_id>/delete/")
def delete_player(team_id, player_id):
    return "This page will delete player %s of Team %s" % (player_id, team_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
