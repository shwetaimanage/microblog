from application import app, db
from flask import render_template,flash, redirect
from flask import request, jsonify
from models import Users, Team
from application.forms import LoginForm
from flask import render_template, flash, redirect, url_for
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Shweta tyagi'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# add user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    print type(data)
    print data
    username = data.get("username")
    email = data.get("email")
    team = data.get("team")
    dict= {"username": username, "email":email, "team":team}
    u = Users(username=username, email=email, team=team)
    db.session.add(u)
    db.session.commit()
    return (jsonify({'Added User Details': dict}))

# delete user
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    record = Users.query.get(user_id)
    print ("*********",record.username)
    db.session.delete(record)
    db.session.commit()
    return (jsonify({'Deleted User_ID': user_id}))

# modify user
@app.route('/modify_user/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    record = Users.query.get(user_id)
    print ("****changing email id of *****",record.username)
    record.username="abc"
    record.email="shwetatyagi@gmail.com"
    db.session.commit()
    return (jsonify({'Update record for User_ID': user_id}))

# add team
@app.route('/add_team', methods=['POST'])
def add_team():
    data = request.json
    print type(data)
    print data
    teamname = data.get("team")
    dict= {"username": teamname}
    t = Team(team=teamname)
    db.session.add(t)
    db.session.commit()
    return (jsonify({'Added team Details': dict}))

# delete team
@app.route('/delete_team/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    record = Team.query.get(team_id)
    print ("*********",record.team)
    db.session.delete(record)
    db.session.commit()
    return (jsonify({'Deleted Team_ID': team_id}))

# modify team
@app.route('/modify_team/<int:team_id>', methods=['PUT'])
def modify_team(team_id):
    record = Team.query.get(team_id)
    print ("****changing name of team *****",record.team)
    record.team="Quality Eng"
    db.session.commit()
    return (jsonify({'Update record for Team_ID': team_id}))
