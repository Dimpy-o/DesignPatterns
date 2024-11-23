from container import RefrigeratedContainer, LiquidContainer, BasicContainer, HeavyContainer


class Ship:
    def __init__(self, ship_id, port, weight_cap, max_containers, max_heavy, max_refrig, max_liquid, fuel_per_km):
        self.id = ship_id
        self.current_port = port
        self.weight_capacity = weight_cap
        self.max_containers = max_containers
        self.max_heavy = max_heavy
        self.max_refrigerated = max_refrig
        self.max_liquid = max_liquid
        self.fuel_per_km = fuel_per_km
        self.containers = []
        self.fuel = 0.0

    def sail_to(self, destination_port):
        if self.current_port == destination_port:
            print("The ship is already at the destination port.")
            return False

        distance = self.current_port.get_distance(destination_port)
        total_fuel_needed = distance * self.fuel_per_km

        # Add fuel consumption of all containers
        for container in self.containers:
            total_fuel_needed += distance * container.consumption()

        if self.fuel >= total_fuel_needed:
            self.fuel -= total_fuel_needed
            self.current_port.outgoing_ship(self)
            destination_port.incoming_ship(self)
            self.current_port = destination_port
            print(f"Ship {self.id} successfully reached port")
            return True
        else:
            print("Not enough fuel to reach the destination port.")
            print(f"Need {total_fuel_needed-self.fuel} more fuel")
            return False

    def refuel(self, new_fuel):
        self.fuel += new_fuel
        print(f"Ship has been refueled by {new_fuel}")

    def load(self, container):
        if len(self.containers) >= self.max_containers:
            print("Cannot load: Maximum container count exceeded.")
            return False

        if sum(c.weight for c in self.containers) + container.weight > self.weight_capacity:
            print("Cannot load: Maximum weight capacity exceeded.")
            return False

        if isinstance(container, HeavyContainer) and len(
            [c for c in self.containers if isinstance(c, HeavyContainer)]
        ) >= self.max_heavy:
            print("Cannot load: Maximum heavy container count exceeded.")
            return False

        if isinstance(container, RefrigeratedContainer) and len(
            [c for c in self.containers if isinstance(c, RefrigeratedContainer)]
        ) >= self.max_refrigerated:
            print("Cannot load: Maximum refrigerated container count exceeded.")
            return False

        if isinstance(container, LiquidContainer) and len(
            [c for c in self.containers if isinstance(c, LiquidContainer)]
        ) >= self.max_liquid:
            print("Cannot load: Maximum liquid container count exceeded.")
            return False

        self.containers.append(container)
        print(f"Container {container.id} loaded successfully.")
        return True

    def unload(self, container):
        if container not in self.containers:
            print(f"Cannot unload: Container {container.id} is not on the ship.")
            return False

        self.containers.remove(container)
        self.current_port.containers.append(container)
        print(f"Container {container.id} unloaded successfully.")
        return True
