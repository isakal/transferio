from app.models import Vehicles


def get_available_vehicles(num_of_pass):
    available_vehicles = {
        "Limo": 4,
        "Minivan": 7,
        "Minibus": 28,
    }

    for k, v in list(available_vehicles.items()):
        if num_of_pass > v:
            available_vehicles.pop(k)

    return available_vehicles
