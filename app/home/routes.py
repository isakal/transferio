from datetime import datetime
from flask import Blueprint, render_template, request


home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def homepage():
    today = datetime.today()
    if request.method == "POST":
        departure = request.form.get("departure")
        destination = request.form.get("destination")
        num_of_pass = request.form.get("number_of_passengers")
        departure_date = request.form.get("departure_date")

        return render_template('home.html', message=f'{departure} {destination} {num_of_pass} {departure_date}', title='Home', today=today)

    return render_template('home.html', title='Home', today=today)
