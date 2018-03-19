from flask import Flask
from flask import render_template, request, redirect, url_for
from flask import jsonify
from flask import flash

app = Flask(__name__)

from sqlalchemy import create_engine, asc

engine = create_engine('sqlite:///teamplayer.db')

from database_setup import Base, Team, Player

Base.metadata.bind = engine

from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Step 2.1 Create anti forgery state token
from flask import session as login_session
import random, string

# Step 5.1 GConnect
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

# Step 5.2 delclare Client id by refrencing client secrets
CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']


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

# Step 2.2 Create a state token to prevent request forgery.
# store it in the session for later validation
@app.route('/login')
def show_login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" %login_session['state']
    return render_template('login.html', STATE=state)


# Step 5.3 gconnect route
@app.route('/gconnect', methods=['POST'])
def gconnect():
    '''on server side, create this function to handle the code sent back from the callback method'''
    # 1. Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid State parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # 2. Obtain authorization code
    code = request.data
    print code
    try:
        # 3. Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade the authorization code'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # 4. Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content_Type'] = 'application/json'
        return response

    # 5. Verify that the access token is used for the intended user.(since we know the access is working but is it right?)
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match with given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # 6. Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps("Token Client id did not match app's"), 401)
        print "Token Client id did not match app's"
        response.headers['Content-Type'] = 'application/json'
        return response

    # 7. check to see if the user is already logged in
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already logged in'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # 7.0 Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # 8. Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    print data

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# Step 6 Disconnect
@app.route("/gdisconnect")
def gdisconnect():
    '''
    DISCONNECT - Revoke a current user's token and reset their login_session
    '''
    access_token = login_session.get('access_token')
    # only disconnect a connected user
    if access_token is None:
        response = make_response(json.dumps('Current user not connected'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    print 'in gdisconnect access token is [%s]' % access_token
    print 'User name is: '
    print login_session['username']

    # Execute HTTP GET request to REVOKE(officially cancel) current token
    url = 'http://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    print 'result is'
    print result

    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.', 200))
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response



@app.route('/teams/JSON')
def teams_json():
    teams = session.query(Team).all()
    return jsonify(Team=[team.serialize for team in teams])


@app.route('/team/<int:team_id>/players/JSON')
def team_players_json(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    players = session.query(Player).filter_by(team_id=team.id).all()
    return jsonify(Players=[player.serialize for player in players])


@app.route('/team/<int:team_id>/player/<int:player_id>/JSON')
def player_info_json(team_id, player_id):
    team = session.query(Team).filter_by(id=team_id).one()
    player = session.query(Player).filter_by(id=player_id)
    return jsonify(Player=[p.serialize for p in player])


@app.route("/")
@app.route("/teams/")
def show_teams():
    teams = session.query(Team).all()
    # return "This page will show all Teams"
    return render_template('teams.html', teams=teams)


@app.route("/team/new/", methods=['GET', 'POST'])
def new_team():
    # return "This page will create new Team"
    if request.method == 'POST':
        if request.form['name']:
            name = request.form['name']
            image_url = request.form['image_url']
            newTeam = Team(name=name, image_url=image_url)
            session.add(newTeam)
            session.commit()
            flash('New Team Added')
        return redirect(url_for('show_teams'))
    else:
        return render_template('newteam.html')


@app.route("/team/<int:team_id>/edit/", methods=['GET', 'POST'])
def edit_team(team_id):
    # return "This page will edit Team %s" % team_id
    editedTeam = session.query(Team).filter_by(id=team_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedTeam.name = request.form['name']
            editedTeam.image_url = request.form['image_url']
        session.add(editedTeam)
        session.commit()
        flash('Team Name Successfully Edited')
        return redirect(url_for('show_teams'))
    else:
        return render_template('editteam.html', team=editedTeam, team_id=team_id)


@app.route("/team/<int:team_id>/delete/", methods=['GET', 'POST'])
def delete_team(team_id):
    # return "This page will delete Team %s" % team_id
    deletedTeam = session.query(Team).filter_by(id=team_id).one()
    if request.method == 'POST':
        session.delete(deletedTeam)
        session.commit()
        flash('Team Successfully Deleted')
        return redirect(url_for('show_teams'))
    else:
        return render_template('deleteteam.html', team=deletedTeam)


@app.route("/team/<int:team_id>/")
@app.route("/team/<int:team_id>/players/")
def show_players(team_id):
    # return "This page will show all players of Team %s" % team_id
    team = session.query(Team).filter_by(id=team_id).one()
    players = session.query(Player).filter_by(team_id=team.id).all()
    roles_array = [player.role for player in players]
    roles = set(roles_array)
    return render_template('players.html', team=team, players=players, roles=roles)


@app.route("/team/<int:team_id>/player/new/", methods=['POST', 'GET'])
def new_player(team_id):
    # return "This page add new player in Team %s" % team_id
    team = session.query(Team).filter_by(id=team_id).one()
    if request.method == 'POST':
        if request.form['name']:
            newPlayer = Player(name=request.form['name'],
                               role=request.form['role'],
                               match=request.form['match'],
                               runs=request.form['runs'],
                               high_score=request.form['high_score'],
                               avg=request.form['avg'],
                               century=request.form['century'],
                               fifty=request.form['fifty'],
                               wickets=request.form['wickets'],
                               bbm=request.form['bbm'],
                               image_url=request.form['image_url'],
                               team=team
                               )
            session.add(newPlayer)
            session.commit()
            flash('New Player Added in Team')
        return redirect(url_for('show_players', team_id=team_id))
    else:
        return render_template('newplayer.html', team=team)


@app.route("/team/<int:team_id>/player/<int:player_id>/edit/", methods=['POST', 'GET'])
def edit_player(team_id, player_id):
    # return "This page will edit player %s of Team %s" % (player_id, team_id)
    team = session.query(Team).filter_by(id=team_id).one()
    editedPlayer = session.query(Player).filter_by(id=player_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedPlayer.name = request.form['name']
        if request.form['role']:
            editedPlayer.role = request.form['role']
        if request.form['match']:
            editedPlayer.match = request.form['match']
        if request.form['runs']:
            editedPlayer.runs = request.form['runs']
        if request.form['high_score']:
            editedPlayer.high_score = request.form['high_score']
        if request.form['avg']:
            editedPlayer.avg = request.form['avg']
        if request.form['century']:
            editedPlayer.century = request.form['century']
        if request.form['fifty']:
            editedPlayer.fifty = request.form['fifty']
        if request.form['wickets']:
            editedPlayer.wickets = request.form['wickets']
        if request.form['bbm']:
            editedPlayer.bbm = request.form['bbm']
        if request.form['image_url']:
            editedPlayer.bbm = request.form['image_url']
        session.add(editedPlayer)
        session.commit()
        flash('Player Information Successfully Edited')
        return redirect(url_for('show_players', team_id=team_id, player_id=player_id))
    else:
        return render_template('editplayer.html', team=team, player=editedPlayer)


@app.route("/team/<int:team_id>/player/<int:player_id>/delete/", methods=['POST', 'GET'])
def delete_player(team_id, player_id):
    # return "This page will delete player %s of Team %s" % (player_id, team_id)
    team = session.query(Team).filter_by(id=team_id).one()
    deletedPlayer = session.query(Player).filter_by(id=player_id).one()
    if request.method == 'POST':
        session.delete(deletedPlayer)
        session.commit()
        flash('Player Successfully Deleted')
        return redirect(url_for('show_players', team_id=team_id))
    else:
        return render_template('deleteplayer.html', team=team, player=deletedPlayer)


if __name__ == '__main__':
    app.secret_key = 'some_secret'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
