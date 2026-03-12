from flask import Flask,render_template,request,redirect,session
from db import Database
import api

app = Flask(__name__)
app.secret_key = "mysecretkey123"   
dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html',message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html',message="Email already exists")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.search(email, password)

    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email/password')

@app.route('/profile')
def profile():
    if 'logged_in' in session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/sentiment_analysis')
def sentiment_analysis():
    if 'logged_in' in session:
        return render_template('sentiment_analysis.html')
    else:
        return redirect('/')

@app.route('/perform_sentiment_analysis',methods=['post'])
def perform_sentiment_analysis():
    if 'logged_in' in session:
        text = request.form.get('sentiment_analysis_text')
        response = api.sentiment_analysis(text)


        return render_template('sentiment_analysis.html',response=response)
    else:
        return redirect('/')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)