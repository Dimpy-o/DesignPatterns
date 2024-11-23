import math


class Port:
    def __init__(self, port_id, latitude, longitude):
        self.id = port_id
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.history = []
        self.current_ships = []

    def incoming_ship(self, ship):
        if ship not in self.current_ships:
            self.current_ships.append(ship)
        if ship not in self.history:
            self.history.append(ship)

    def outgoing_ship(self, ship):
        if ship in self.current_ships:
            self.current_ships.remove(ship)

    def get_distance(self, other):

        r = 6371
        lat1, lon1 = math.radians(self.latitude), math.radians(self.longitude)
        lat2, lon2 = math.radians(other.latitude), math.radians(other.longitude)
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return r * c

