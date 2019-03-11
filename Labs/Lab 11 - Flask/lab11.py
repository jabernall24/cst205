#! /usr/bin/env python3

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from flask import Flask, render_template, flash, redirect
from wtforms.validators import DataRequired
from datetime import datetime


# Task 2
# app = Flask(__name__)
#
#
# @app.route("/")
# def home():
#     return "Hello World from flask"


# Task 3
# app = Flask(__name__)
#
#
# @app.route("/")
# def home():
#     return render_template("hello.html")


# Task 4
# app = Flask(__name__)
#
# color_dictionary = {
#         "blue": [(0, 0, 255), "#0000FF"],
#         "red": [(255, 0, 0), "#FF0000"],
#         "green": [(0, 255, 0), "#00FF00"],
#         "cyan": [(0, 255, 255), "#00FFFF"],
#         "turquoise": [(64, 224, 208), "#40E0D0"],
#         "teal": [(0, 128, 128), "#008080"],
#         "pink": [(255, 192, 203), "#FFC0CB"],
#         "lavender": [(230, 230, 250), "#E6E6FA"],
#         "purple": [(85, 37, 130), "#552582"],
#         "gold": [(253, 185, 39), "#FDB927"],
#         "black": [(0, 0, 0), "#000000"],
#         "white": [(255, 255, 255), "#FFFFFF"],
#         "silver": [(192, 192, 192), "#C0C0C0"],
#         "snow": [(255, 250, 250), "#FFFAFA"],
#     }
#
#
# class PlayList(FlaskForm):
#     song_title = StringField('Song Title')
#     submit = SubmitField('Submit')
#
# @app.route('/')
# def home():
#     return render_template("hello.html", s_list = color_dictionary)

# Task 6
app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)


class Playlist(FlaskForm):
    song_title = StringField('Song Title', validators=[DataRequired()])
    artist_title = StringField('Artist', validators=[DataRequired()])
    submit = SubmitField('Submit')


playlist = []


def store_song(my_song, my_artist):
    playlist.append(dict(
        song=my_song,
        artist=my_artist,
        date=datetime.today()
    ))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Playlist()
    if form.validate_on_submit():
        store_song(form.song_title.data, form.artist_title.data)
        return redirect('/pl')
    return render_template('index.html', form=form)


@app.route('/pl')
def pl():
    return render_template('pl.html', playlist=playlist)


if __name__ == '__main__':
    app.run(debug=False)
