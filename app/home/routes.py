from app import db
from datetime import date
from app.models import Vehicles, Transfer
from flask import Blueprint, render_template, request, redirect, url_for, abort
from app.home.utils import get_available_vehicles, calculate_distance, get_offers, send_transfer_data_mail, calculate_price_final


home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def homepage():

    today = date.today()

    if request.method == "POST":
        departure = request.form.get("departure")
        destination = request.form.get("destination")
        num_of_pass = request.form.get("number_of_passengers")
        departure_date = request.form.get("departure_date")

        return redirect(url_for("home.vehicles",
                        departure=departure,
                        destination=destination,
                        num_of_pass=num_of_pass,
                        departure_date=departure_date))

    return render_template('home.html', title='Home', today=today)


@home.route('/transfer/<string:departure>/<string:destination>/<int:num_of_pass>/<string:departure_date>')
def vehicles(departure, destination, num_of_pass, departure_date):

    available_vehicles = get_available_vehicles(num_of_pass)
    distance = calculate_distance(departure, destination)

    offers = get_offers(available_vehicles, distance)

    return render_template("vehicles.html",
                           title="Vehicles",
                           offers=offers,
                           departure=departure,
                           destination=destination,
                           num_of_pass=num_of_pass,
                           departure_date=departure_date
                           )


@home.route('/transfer/<string:departure>/<string:destination>/<int:num_of_pass>/<string:departure_date>/<string:vehicle>', methods=['GET', 'POST'])
def transfer_data(departure, destination, num_of_pass, departure_date, vehicle):

    today = date.today()

    if vehicle not in [v.name for v in Vehicles]:
        abort(404)

    if request.method == "POST":
        dptr = request.form.get("departure")
        dptr_addr = request.form.get("dropoff-address")
        dptr_date = request.form.get("departure_date")
        dest = request.form.get("destination")
        dest_addr = request.form.get("pickup-address")
        vehicle_enum = Vehicles.__dict__.get(vehicle)
        is_twoway = True if request.form.get("is_twoway") == "Yes" else False
        price = calculate_price_final(vehicle, dptr, dest, is_twoway)
        num_of_pass = request.form.get("number_of_passengers")
        contact_email = request.form.get("email")

        transfer = Transfer(
            dptr=dptr,
            dptr_addr=dptr_addr,
            dptr_date=dptr_date,
            dest=dest,
            dest_addr=dest_addr,
            vehicle=vehicle_enum,
            price=price,
            is_twoway=is_twoway,
            num_of_pass=num_of_pass,
            contact_email=contact_email
        )
        db.session.add(transfer)
        db.session.commit()

        send_transfer_data_mail(transfer)

        return render_template("thank_you.html")
    else:
        return render_template("transfer_details.html",
                               title="Transfer Details",
                               today=today,
                               departure=departure,
                               destination=destination,
                               num_of_pass=num_of_pass,
                               )


# @home.route("/thankyou")
# def thankyou():
#     return render_template("thank_you.html")
