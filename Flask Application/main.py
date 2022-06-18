from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from send_email import send_email
from sqlalchemy.sql import func


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:%s@localhost:1804/height_collecter" % quote(
    'Son@devi1')
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_value']
        data = Data(email, height)

        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            db.session.add(data)
            db.session.commit()
            print(email, height)
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            send_email(email, height, average_height)
            print(type(average_height))
            return render_template('success.html')

    return render_template('index.html', text='Email address already used')


if __name__ == '__main__':
    app.debug = True
    app.run()
