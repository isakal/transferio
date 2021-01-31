from app import db
from datetime import datetime


# grad odakle krecemo
# adresa di se goste kupi (google api ogranicava grad)
# grad dokle idemo
# adresa di se goste vodi (google api ogranicava grad)
# sredstvo
# cijena(eur)
# dvosmjerno - boolean
# kolicina osoba
# datum


class Transfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_pt = db.Column(db.String(255), nullable=False)
    start_pt_addr = db.Column(db.String(255), nullable=False)
    dest = db.Column(db.String(255), nullable=False)
    dest_addr = db.Column(db.String(255), nullable=False)
    vehicle = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    is_twoway = db.Column(db.Boolean, default=False)
    passenger_amt = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
