from abc import ABC, abstractmethod


# Base interface for Ship
class Ship(ABC):
    def __init__(self, ship_id, port, fuel_per_km):
        self.id = ship_id
        self.current_port = port
        self.containers = []
        self.max_fuel = 0
        self.max_weight = 0
        self.max_containers = 0
        self.fuel_per_km = fuel_per_km

    @abstractmethod
    def sail_to(self):
        pass

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def load(self, container):
        if len(self.containers) >= self.max_containers:
            print("Cannot load: Maximum container count exceeded.")
            return False
        if sum(c.weight for c in self.containers) + container.weight > self.max_weight:
            print("Cannot load: Maximum weight capacity exceeded.")
            return False
        self.containers.append(container)
        print(f"Container {container.id} loaded successfully.")
        return True

    @abstractmethod
    def unload(self, container):
        if container not in self.containers:
            print(f"Cannot unload: Container {container.id} is not on the ship.")
            return False

        self.containers.remove(container)
        self.current_port.containers.append(container)
        print(f"Container {container.id} unloaded successfully.")
        return True


# Concrete Ship Classes
class LightWeightShip(Ship):
    def __init__(self, ship_id, port, fuel_per_km):
        super().__init__(ship_id, port, fuel_per_km)
        self.max_containers = 1000
        self.max_weight = 15000
        self.max_fuel = 8000000

    def sail_to(self):
        return "LightWeightShip is sailing with limited range."

    def get_details(self):
        return f"LightWeightShip with containers: {self.containers}, Fuel capacity: {self.max_fuel}"

    def load(self, container):
        super().load()

    def unload(self, container):
        super().unload()


class MediumShip(Ship):
    def __init__(self, ship_id, port, fuel_per_km):
        super().__init__(ship_id, port, fuel_per_km)
        self.max_containers = 10000
        self.max_weight = 100000
        self.max_fuel = 10000000

    def sail_to(self):
        return "MediumShip is sailing with a moderate range."

    def get_details(self):
        return f"MediumShip with containers: {self.containers}, Fuel capacity: {self.max_fuel}"

    def load(self, container):
        super().load()

    def unload(self, container):
        super().unload()


class HeavyShip(Ship):
    def __init__(self, ship_id, port, fuel_per_km):
        super().__init__(ship_id, port, fuel_per_km)
        self.max_containers = 20000
        self.max_weight = 250000
        self.max_fuel = 15000000

    def sail_to(self):
        return "HeavyShip is sailing with a long range."

    def get_details(self):
        return f"HeavyShip with containers: {self.containers}, Fuel capacity: {self.max_fuel}"

    def load(self, container):
        super().load()

    def unload(self, container):
        super().unload()


class ShipFactory(ABC):
    @abstractmethod
    def create_ship(self) -> Ship:
        pass

    @abstractmethod
    def configure_containers(self, ship: Ship):
        pass


# Concrete Factories
class LightWeightShipFactory(ShipFactory):
    def create_ship(self) -> Ship:
        return LightWeightShip(self)

    def configure_containers(self, ship: Ship):
        ship.containers.append("Basic Storage Unit")


class MediumShipFactory(ShipFactory):
    def create_ship(self) -> Ship:
        return MediumShip()

    def configure_containers(self, ship: Ship):
        ship.containers.append(["Refrigerator", "Water Container"])


class HeavyShipFactory(ShipFactory):
    def create_ship(self) -> Ship:
        return HeavyShip()

    def configure_containers(self, ship: Ship):
        ship.containers.extend(["Cargo Hold", "Advanced Storage Systems"])
