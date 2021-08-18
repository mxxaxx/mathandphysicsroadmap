from flask.wrappers import Response
from website.auth import login
from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify
from flask_login.utils import login_required, current_user
from .models import User
from . import db

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():
    if current_user.username == "Mete":
        return render_template("metehome.html", name=current_user.username, user=current_user)
    elif current_user.username == "Malik":
        return render_template("malikhome.html", name=current_user.username, user=current_user)