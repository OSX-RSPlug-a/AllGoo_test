from flask import Flask
from flask import Flask, request, redirect, url_for, session, g, flash, render_template
import os
#from flask_oauth import OAuth
#from sqlalchemy.orm import sessionmaker
#from flask_dance.contrib.twitter import make_twitter_blueprint, twitter 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
 
app = Flask(__name__)
 
@app.route('/')
def home():

    if not session.get('logged_in'):
        return render_template('login.html')

    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)

    s = Session()

    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )

    result = query.first()

    if result:
        session['logged_in'] = True

    else:
        flash('wrong password!')

    return home()
 
@app.route("/logout")
def logout():

    session['logged_in'] = False

    return home()


#app.config['SECRET_KEY'] = 'thisissupposedtobeasecret'

#twitter_blueprint = make_twitter_blueprint(api_key='API_KEY', api_secret='API_SECRET')

#app.register_blueprint(twitter_blueprint, url_prefix='/twitter_login')

#@app.route('/twitter')
#def twitter_login():
#    if not twitter.authorized:
#        return redirect(url_for('twitter.login'))
#    account_info = twitter.get('account/settings.json')

#    if account_info.ok:
#        account_info_json = account_info.json()

#        return '<h1>Your Twitter name is @{}'.format(account_info_json['screen_name'])

#    return '<h1>Request failed!</h1>'

 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
