from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .webscraping import scrape, toItems

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        search = request.form.get("search")

        #function scrape returns a list of search results
        items = scrape(search)
        itemObjects = toItems(items)

    return render_template("home.html", user=current_user, items=itemObjects)

@views.route('/saved', methods=["GET"])
@login_required
def saved():
    return render_template("save.html", user=current_user)