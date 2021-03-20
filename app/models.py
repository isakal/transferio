from app import db
from enum import Enum
from datetime import date


# grad odakle krecemo
# adresa di se goste kupi (google api ogranicava grad)
# grad dokle idemo
# adresa di se goste vodi (google api ogranicava grad)
# sredstvo
# cijena(eur)
# dvosmjerno - boolean
# kolicina osoba
# datum

class Vehicles(Enum):
    Limo = 1
    Minivan = 2
    Minibus = 3


class Transfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dptr = db.Column(db.String(255), nullable=False)
    dptr_addr = db.Column(db.String(255), nullable=False)
    dptr_date = db.Column(db.Date, nullable=False)
    dest = db.Column(db.String(255), nullable=False)
    dest_addr = db.Column(db.String(255), nullable=False)
    vehicle = db.Column(db.Enum(Vehicles), nullable=False)  # TODO: vidi kako ovo sranje radi
    price = db.Column(db.Float(precision=2), nullable=False)  # EURO
    is_twoway = db.Column(db.Boolean, default=False)
    passenger_amt = db.Column(db.Integer, nullable=False)
    contact_email = db.Column(db.String(255), nullable=False)
