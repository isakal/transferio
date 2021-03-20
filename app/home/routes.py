from datetime import date
from app.models import Vehicles, Transfer
from flask import Blueprint, render_template, request, redirect, url_for
from app.home.utils import get_available_vehicles, calculate_distance, get_offers, send_transfer_data_mail

import os
from app import mail
from flask_mail import Message


home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def homepage():
    today = date.today()
    if request.method == "POST":
        departure = request.form.get("departure")
        destination = request.form.get("destination")
        num_of_pass = request.form.get("number_of_passengers")
        departure_date = request.form.get("departure_date")

        return redirect(url_for("home.transfer", departure=departure, destination=destination, num_of_pass=num_of_pass, departure_date=departure_date))

    return render_template('home.html', title='Home', today=today)


@home.route('/transfer/<string:departure>/<string:destination>/<int:num_of_pass>/<string:departure_date>', methods=['GET', 'POST'])
def transfer(departure, destination, num_of_pass, departure_date):

    available_vehicles = get_available_vehicles(num_of_pass)
    distance = calculate_distance(departure, destination)

    offers = get_offers(available_vehicles, distance)

    return render_template("transfer.html", message=offers[0], offers=offers)


@home.route('/send-mail')
def send_mail():
    send_transfer_data_mail()

    return "sent"
