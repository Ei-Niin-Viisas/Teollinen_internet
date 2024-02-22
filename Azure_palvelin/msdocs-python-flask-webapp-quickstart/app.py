import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, json)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class DataPiste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aika = db.Column(db.String(80), unique=True, nullable=False)
    nopeus = db.Column(db.String(120), nullable=False)

class RobottiData:
    def __init__(self, speed, time):
        self.speed = speed
        self.time = time

muuttujat = []


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/api/robotics', methods = ['POST'])
def apirobotics():
    nopeus = request.form.get("tcp_speed")
    aika = request.form.get("time")

    muuttujat.append(RobottiData(nopeus, aika))
    return "Kiitos viestistäsi!"

@app.route('/robotics/data')
def data():
    return render_template('roboticsData.html', entries = json.dumps([ob.__dict__ for ob in muuttujat]))

if __name__ == '__main__':
   app.run()
