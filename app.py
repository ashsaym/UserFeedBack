import flask
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from datetime import datetime

app = Flask(__name__, static_url_path='/static')
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userColor = db.Column(db.String(80), unique=False, nullable=False)
    userCorrectMark = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.Integer, nullable=False)
    timetaken = db.Column(db.Integer, nullable=False)
    c1 = db.Column(db.Integer, nullable=False)
    c2 = db.Column(db.Integer, nullable=False)
    c3 = db.Column(db.Integer, nullable=False)
    s1 = db.Column(db.Integer, nullable=False)
    s2 = db.Column(db.Integer, nullable=False)
    s3 = db.Column(db.Integer, nullable=False)
    s4 = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.id)


@app.before_first_request
def before_request_func():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def index():
    uColor = 'white'
    if request.method == "POST":
        return flask.redirect(flask.url_for('cQues'))
    return render_template("index.html", uColor=uColor)


@app.route("/cQues", methods=['GET', 'POST'])
def cQues():
    uColor = 'white'
    allUser = User.query.all()
    lent = len(allUser)
    if request.method == "POST":
        try:
            session['id'] = lent + 1
            if lent % 2 == 0:
                uColor = 'Green'
            else:
                uColor = 'White'
            session['color'] = uColor
            session['userCorrectMark'] = 0
            session['timeStart'] = datetime.now().timestamp()
            session['c1'] = request.form['optradio1']
            session['c2'] = request.form['optradio2']
            session['c3'] = request.form['optradio3']
            return flask.redirect(flask.url_for('userView1'))
        except:
            uColor = 'lightblue'
            return render_template("cQues.html", uColor=uColor)
    return render_template("cQues.html", uColor=uColor)


@app.route("/page/1", methods=['GET', 'POST'])
def userView1():
    findNum = 6
    qNum = 1
    if session['color'] is not None:
        uColor = session['color']
        previousMark = session['userCorrectMark']
        num = 1
        if request.method == "POST":
            number = request.form['number']
            if int(number) == 3:
                currentMark = int(previousMark) + 1
                session['userCorrectMark'] = currentMark
            return flask.redirect(flask.url_for('userView2'))
        return render_template("page1.html", uColor=uColor, num=num,
                               findNum=findNum, qNum=qNum)
    else:
        return 'invalid'


@app.route("/page/2", methods=['GET', 'POST'])
def userView2():
    findNum = 3
    qNum = 2
    if session['color'] is not None:
        uColor = session['color']
        previousMark = session['userCorrectMark']
        num = 2
        if request.method == "POST":
            number = request.form['number']
            if int(number) == 7:
                currentMark = int(previousMark) + 1
                session['userCorrectMark'] = currentMark
            return flask.redirect(flask.url_for('userView3'))
        return render_template("page1.html", uColor=uColor, num=num,
                               findNum=findNum, qNum=qNum)
    else:
        return 'invalid'


@app.route("/page/3", methods=['GET', 'POST'])
def userView3():
    findNum = 9
    qNum = 3
    if session['color'] is not None:
        uColor = session['color']
        previousMark = session['userCorrectMark']
        num = 3
        if request.method == "POST":
            number = request.form['number']
            if int(number) == 6:
                currentMark = int(previousMark) + 1
                session['userCorrectMark'] = currentMark
            return flask.redirect(flask.url_for('userView4'))
        return render_template("page1.html", uColor=uColor, num=num,
                               findNum=findNum, qNum=qNum)
    else:
        return 'invalid'


@app.route("/page/4", methods=['GET', 'POST'])
def userView4():
    findNum = 2
    qNum = 4
    if session['color'] is not None:
        uColor = session['color']
        previousMark = session['userCorrectMark']
        num = 4
        if request.method == "POST":
            number = request.form['number']
            if int(number) == 5:
                currentMark = int(previousMark) + 1
                session['userCorrectMark'] = currentMark
            return flask.redirect(flask.url_for('userView5'))
        return render_template("page1.html", uColor=uColor, num=num,
                               findNum=findNum, qNum=qNum)
    else:
        return 'invalid'


@app.route("/page/5", methods=['GET', 'POST'])
def userView5():
    findNum = 7
    qNum = 5
    if session['color'] is not None:
        uColor = session['color']
        previousMark = session['userCorrectMark']
        num = 5
        if request.method == "POST":
            number = request.form['number']
            if int(number) == 10:
                currentMark = int(previousMark) + 1
                session['userCorrectMark'] = currentMark
            return flask.redirect(flask.url_for('finalView'))
        return render_template("page1.html", uColor=uColor, num=num,
                               findNum=findNum, qNum=qNum)
    else:
        return 'invalid'


@app.route("/page/results", methods=['GET', 'POST'])
def finalView():
    if session['color'] is not None:
        id = session['id']
        uColor = session['color']
        userCorrectMark = session['userCorrectMark']
        payment = (int(userCorrectMark) * 1)
        preTime = session['timeStart']
        nowTime = datetime.now().timestamp()
        timeTaken = nowTime - preTime

        session['payment'] = payment
        session['timeTaken'] = timeTaken

        if request.method == "POST":
            return flask.redirect(flask.url_for('sQues'))
        return render_template("final.html", uColor=uColor, userCorrectMark=userCorrectMark, payment=payment)
    else:
        return 'invalid'


@app.route("/page/sQues", methods=['GET', 'POST'])
def sQues():
    uColor = 'white'
    if request.method == "POST":
        try:
            session['s1'] = request.form['optradio4']
            session['s2'] = request.form['optradio5']
            session['s3'] = request.form['optradio6']
            session['s4'] = request.form['optradio7']
            return flask.redirect(flask.url_for('submitPage'))
        except:
            return render_template("sQues.html", uColor=uColor)
    return render_template("sQues.html", uColor=uColor)


@app.route("/page/submit", methods=['GET', 'POST'])
def submitPage():
    if session['color'] is not None:
        try:
            idu = session['id']
            uColor = session['color']
            userCorrectMark = session['userCorrectMark']
            payment = session['payment']
            timeTaken = session['timeTaken']
            c1 = session['c1']
            c2 = session['c2']
            c3 = session['c3']
            s1 = session['s1']
            s2 = session['s2']
            s3 = session['s3']
            s4 = session['s4']

            user = User(id=idu, userColor=uColor, userCorrectMark=userCorrectMark, payment=payment, timetaken=timeTaken,
                        c1=c1, c2=c2, c3=c3, s1=s1, s2=s2, s3=s3, s4=s4)
            db.session.add(user)
            db.session.commit()
            addedText = 'Data has been saved Successfully !!'
            return render_template("submit.html", uColor=uColor, addedText=addedText)
        except:
            addedText = 'User already added'
            return render_template("submit.html", uColor=session['color'], addedText=addedText)


@app.route("/admin", methods=['GET', 'POST'])
def adminLogin():
    adminPass = 'MQ4w6cJwLsBZSqZARyQnvfW'
    if request.method == "POST":
        password = request.form['password']
        if password == adminPass:
            session['admin'] = 'ADMIN'
            return flask.redirect(flask.url_for('adminView'))
    return render_template("admin.html")


@app.route("/adminView", methods=['GET', 'POST'])
def adminView():
    try:
        if session['admin'] is not None:
            allUser = User.query.all()
            lent = len(allUser)
            return render_template("adminView.html", allUser=allUser, lent=lent)
    except:
        return flask.redirect(flask.url_for('adminLogin'))
