import random
import sqlite3
import time
from datetime import datetime

from flask import Blueprint, render_template, jsonify, session, current_app, request, g, flash, redirect, url_for

from board import auth
from .database import get_db
bp = Blueprint("pages", __name__)

random_number = None
last_generated = None

def generate_random_number():
    global random_number, last_generated
    random_number = random.randint(1, 1000)
    last_generated = time.time()


@bp.route("/")
def home():
    global random_number, last_generated
    if random_number is None or last_generated is None or time.time() - last_generated > 300:
        generate_random_number()
    return render_template("pages/home.html", random_number=random_number)

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/profile")
def profile():
    user_id = session.get('user_id')
    if user_id == None:
        return redirect(url_for("auth.login"))
    db = get_db()
    user = db.execute('SELECT points, username FROM user WHERE id = ?', (user_id,)).fetchone()

    if user:
        points = user['points']
        username = user['username']
    else:
        flash('User not found !')
        return redirect(url_for('auth.login'))

    return render_template("pages/profile.html", points = points, username = username)

@bp.route("/check", methods = ('GET', 'POST'))
def check():
    global random_number
    message = None
    db = get_db()
    user_id = session.get("user_id")

    if user_id is None:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        number = request.form["number"]
        if int(number) == random_number:
            try:
                user = db.execute('SELECT last_number, last_entry_time, points FROM user WHERE id = ?',
                                  (user_id,)).fetchone()
                last_number = user['last_number']
                last_entry_time = user['last_entry_time']
                current_points = user['points']
                if number == last_number and last_entry_time >= datetime.fromtimestamp(last_generated):
                    message = 'You have already entered this number !'
                else:
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    new_points = current_points + 10
                    db.execute('UPDATE user SET last_number = ?, last_entry_time = ?, points = ? WHERE id = ?',
                               (number, current_time, new_points, user_id))
                    db.commit()
                    message = 'You got +10 Points !'
            except sqlite3.IntegrityError:
                db.rollback()
                message = 'Error'
        else:
            message = 'You entered the wrong number !'

    return render_template("pages/check.html", message=message)
