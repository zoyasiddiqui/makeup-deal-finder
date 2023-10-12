from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    pass

@views.route('/saved', methods=["GET"])
@login_required
def saved():
    pass