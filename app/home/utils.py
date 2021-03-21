import os
from app import gmaps, mail
from flask_mail import Message


PRICE_PER_KM = 1.5

PRICE_MODS = {
    "Limo": 1,
    "Minivan": 1.3,
    "Minibus": 2.5
}


def get_available_vehicles(num_of_pass):
    """returns available vehicles depending on the number of passengers"""
    available_vehicles = {
        "Limo": 4,
        "Minivan": 7,
        "Minibus": 28,
    }

    for k, v in list(available_vehicles.items()):
        if num_of_pass > v:
            available_vehicles.pop(k)

    return available_vehicles


def calculate_distance(origin, destination):
    """returns distance between 2 cities in meters"""
    response = gmaps.distance_matrix(
        origins=origin,
        destinations=destination,
        mode="driving",
        region="hr",
    )

    distance = response["rows"][0]["elements"][0]["distance"]["value"]

    return distance


def round_to_5(number):
    """rounds number to the nearest 5"""
    return 5 * round(number / 5)


def calculate_price(distance):
    """calculate price based on distance in meters"""
    return round_to_5(distance / 1000 * PRICE_PER_KM)


def get_offers(available_vehicles, distance):
    """makes offers depending on available vehicles and distance"""
    base_price = calculate_price(distance)
    offers = []

    for k, v in available_vehicles.items():
        price_mod = PRICE_MODS[k]

        offer = {"vehicle_type": k, "max_num_of_pass": v, "price": base_price * price_mod}
        offers.append(offer)

    return offers


def calculate_price_final(vehicle, departure, destination, is_twoway):
    distance = calculate_distance(departure, destination)
    base_price = calculate_price(distance)

    if is_twoway:
        price = base_price * PRICE_MODS[vehicle] * 1.95
    else:
        price = base_price * PRICE_MODS[vehicle]

    return price


def send_transfer_data_mail(transfer):
    msg = Message()
    msg.subject = f"Transfer reservation #{transfer.id}"
    msg.body = f"""Thank you for using transfer.io

Reservation info:

Pickup location: {transfer.dptr}
Pickup Address: {transfer.dptr_addr}
Departure date: {transfer.dptr_date.strftime('%d.%m.%Y.')}

Dropoff location: {transfer.dest}
Dropoff Address: {transfer.dest_addr}

Vehicle: {transfer.vehicle.name}
Two way: {"Yes" if transfer.is_twoway else "No"}

Price : {transfer.price} €

    """
    msg.add_recipient(transfer.contact_email)

    mail.send(msg)
