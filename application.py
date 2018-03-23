#!/usr/bin/env python2.7

from flask import Flask
from flask import render_template, request, redirect, url_for
from flask import jsonify
from flask import flash
# step 8.1 import User table as well
from sqlalchemy import create_engine, asc
from database_setup import Base, Team, Player, User
from sqlalchemy.orm import sessionmaker
# Step 2.1 Create anti forgery state token
from flask import session as login_session
import random
import string
# Step 5.1 GConnect
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

engine = create_engine('sqlite:///teamplayerwithuser.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Step 5.2 delclare Client id by refrencing client secrets
CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web'][
    'client_id']


# Step 2.2 Create a state token to prevent request forgery.
# store it in the session for later validation
@app.route('/login')
def show_login():
    state = ''.join(
        random.choice(string.ascii_uppercase + string.digits) for x in
        xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']

        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("you have successfully been logged out.")
        return redirect(url_for('show_teams'))
    else:
        flash("you are not logged in to begin with")
        return redirect(url_for('show_teams'))


# Step 5.3 gconnect route
@app.route('/gconnect', methods=['POST'])
def gconnect():
    '''on server side, create this function
    to handle the code sent back from the callback method
    5.3.1. Validate state token
    '''
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
        response = make_response(
            json.dumps('Failed to upgrade the authorization code'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # 4. Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # 5. Verify that the access token is used for the intended user.
    # (since we know the access is working but is it right?)
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match with given user ID."),
            401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # 6. Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token Client id did not match app's"), 401)
        print "Token Client id did not match app's"
        response.headers['Content-Type'] = 'application/json'
        return response

    # 7. check to see if the user is already logged in
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already logged in'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # 7.0 Store the access token in the session for later use.
    login_session['provider'] = 'google'
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

    # see if User exist, it it doesn't then make a new one
    user_email = login_session['email']
    user_id = getUserID(user_email)
    if user_id is None:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;' \
              '-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# Step 9. User Helper Function

# Create User
def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# get user id from email
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# get user info from user id as object
def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


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
    url = 'http://accounts.google.com/o/oauth2/revoke?token=%s' % \
          login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    print 'result is'
    print result

    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.', 200))
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
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
    # return "This page will show all Teams"
    teams = session.query(Team).order_by(asc(Team.name))
    if 'username' not in login_session:
        return render_template('publicteams.html', teams=teams)
    else:
        creator = getUserInfo(login_session['user_id'])
        return render_template('teams.html', teams=teams, creator=creator)


@app.route("/team/new/", methods=['GET', 'POST'])
def new_team():
    # return "This page will create new Team"
    # n Step 7. redirect to login page if user is not logged in before creating
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        if request.form['name']:
            # add user_id details in database while creating new Team
            name = request.form['name']
            image_url = request.form['image_url']
            newTeam = Team(name=name, image_url=image_url,
                           user_id=login_session['user_id'])
            session.add(newTeam)
            session.commit()
            flash('New Team Added')
        return redirect(url_for('show_teams'))
    else:
        creator = getUserInfo(login_session['user_id'])
        return render_template('newteam.html', creator=creator)


@app.route("/team/<int:team_id>/edit/", methods=['GET', 'POST'])
def edit_team(team_id):
    # return "This page will edit Team %s" % team_id
    editedTeam = session.query(Team).filter_by(id=team_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if login_session['user_id'] != editedTeam.user_id:
        return "<script>function myFunction() {" \
               "alert('You are not authorized to manipulate this Team data." \
               " Please create your own Team in order to do so.');}" \
               "</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedTeam.name = request.form['name']
            editedTeam.image_url = request.form['image_url']
        session.add(editedTeam)
        session.commit()
        flash('Team Name Successfully Edited')
        return redirect(url_for('show_teams'))
    else:
        creator = getUserInfo(login_session['user_id'])
        return render_template('editteam.html', team=editedTeam,
                               team_id=team_id, creator=creator)


@app.route("/team/<int:team_id>/delete/", methods=['GET', 'POST'])
def delete_team(team_id):
    # return "This page will delete Team %s" % team_id
    deletedTeam = session.query(Team).filter_by(id=team_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if login_session['user_id'] != deletedTeam.user_id:
        return "<script>function myFunction() {" \
               "alert('You are not authorized to manipulate this Team data." \
               " Please create your own Team in order to do so.');}" \
               "</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(deletedTeam)
        session.commit()
        flash('Team Successfully Deleted')
        return redirect(url_for('show_teams'))
    else:
        creator = getUserInfo(login_session['user_id'])
        return render_template('deleteteam.html', team=deletedTeam,
                               creator=creator)


@app.route("/team/<int:team_id>/")
@app.route("/team/<int:team_id>/players/")
def show_players(team_id):
    # return "This page will show all players of Team %s" % team_id
    team = session.query(Team).filter_by(id=team_id).one()
    players = session.query(Player).filter_by(team_id=team.id).all()
    roles_array = [player.role for player in players]
    roles = set(roles_array)
    owner = getUserInfo(team.user_id)
    if 'username' not in login_session or login_session['user_id'] != owner.id:
        return render_template('publicplayers.html', team=team,
                               players=players, roles=roles, creator=owner)
    else:
        return render_template('players.html', team=team, players=players,
                               roles=roles, creator=owner)


@app.route("/team/<int:team_id>/player/new/", methods=['POST', 'GET'])
def new_player(team_id):
    # return "This page add new player in Team %s" % team_id
    team = session.query(Team).filter_by(id=team_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if login_session['user_id'] != team.user_id:
        return "<script>function myFunction() {" \
               "alert('You are not authorized to manipulate this Team data." \
               " Please create your own Team in order to do so.');}</script>" \
               "<body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            # step 9. add player creator user_id details
            # while creating new player in team
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
                               user_id=team.user_id,
                               team=team
                               )
            session.add(newPlayer)
            session.commit()
            flash('New Player Added in Team')
        return redirect(url_for('show_players', team_id=team_id))
    else:
        creator = getUserInfo(login_session['user_id'])
        return render_template('newplayer.html', team=team, creator=creator)


@app.route("/team/<int:team_id>/player/<int:player_id>/edit/",
           methods=['POST', 'GET'])
def edit_player(team_id, player_id):
    # return "This page will edit player %s of Team %s" % (player_id, team_id)
    team = session.query(Team).filter_by(id=team_id).one()
    editedPlayer = session.query(Player).filter_by(id=player_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if login_session['user_id'] != team.user_id:
        return "<script>function myFunction() {" \
               "alert('You are not authorized to manipulate this Team data." \
               " Please create your own Team in order to do so.');}</script>" \
               "<body onload='myFunction()''>"

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
        return redirect(
            url_for('show_players', team_id=team_id, player_id=player_id))
    else:
        creator = getUserInfo(login_session['user_id'])
        return render_template('editplayer.html', team=team,
                               player=editedPlayer, creator=creator)


@app.route("/team/<int:team_id>/player/<int:player_id>/delete/",
           methods=['POST', 'GET'])
def delete_player(team_id, player_id):
    # return "This page will delete player %s of Team %s" %(player_id, team_id)
    team = session.query(Team).filter_by(id=team_id).one()
    deletedPlayer = session.query(Player).filter_by(id=player_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if login_session['user_id'] != team.user_id:
        return "<script>function myFunction() {" \
               "alert('You are not authorized to manipulate this Team data. " \
               "Please create your own Team in order to do so.');}</script>" \
               "<body onload='myFunction()''>"

    if request.method == 'POST':
        session.delete(deletedPlayer)
        session.commit()
        flash('Player Successfully Deleted')
        return redirect(url_for('show_players', team_id=team_id))
    else:
        creator = getUserInfo(login_session['user_id'])
        return render_template('deleteplayer.html', team=team,
                               player=deletedPlayer, creator=creator)


if __name__ == '__main__':
    app.secret_key = 'some_secret'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
