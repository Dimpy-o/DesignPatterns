import json
from port import Port
from itemfactory import Item
from container import RefrigeratedContainer, LiquidContainer, BasicContainer, HeavyContainer
from itemfactory import SmallItemFactory, HeavyItemFactory, RefrigeratedItemFactory, LiquidItemFactory
from shipfactory import LightWeightShipFactory, MediumShipFactory, HeavyShipFactory, LightWeightShip, MediumShip, HeavyShip


def main(input_file, output_file):
    # Load input JSON
    with open(input_file, 'r') as file:
        operations = json.load(file)

    # Initialize entities
    ports = {}
    ships = {}
    containers = {}
    items = {}

    lightweight_factory = LightWeightShipFactory()
    medium_factory = MediumShipFactory()
    heavy_factory = HeavyShipFactory()

    for op in operations:
        # Parse and execute operation
        execute_operation(op, ports, ships, containers, items)

    # Generate output
    output = generate_output(ports)
    with open(output_file, 'w') as file:
        json.dump(output, file, indent=4)


# Executes individual operations based on their type
def execute_operation(operation, ports, ships, containers, items):
    action = operation["action"]

    if action == "create_port":
        port_id = operation["id"]
        latitude = operation["latitude"]
        longitude = operation["longitude"]
        ports[port_id] = Port(port_id, latitude, longitude)

    elif action == "create_ship":
        ship_id = operation["id"]
        port_id = operation["port"]
        ship_type = operation["type"]
        fuel_per_km = operation["fuel_per_km"]
        if ship_type == "lightweight":
            ships[ship_id] = LightWeightShip(ship_id, ports[port_id], fuel_per_km)
        elif ship_type == "medium":
            medium_factory = MediumShipFactory()
            ship = medium_factory.create_ship()
            medium_factory.configure_containers(ship)
            ships[ship_id] = MediumShip(ship_id, ports[port_id], fuel_per_km)
        elif ship_type == "heavy":
            heavy_factory = HeavyShipFactory()
            heavy_factory.create_ship()
            ships[ship_id] = HeavyShip(ship_id, ports[port_id], fuel_per_km)
        ports[port_id].incoming_ship(ships[ship_id])

    elif action == "create_container":
        container_id = operation["id"]
#        weight = operation["weight"]
        if "type" in operation:
            container_type = operation["type"]
            if container_type == "R":
                containers[container_id] = RefrigeratedContainer(container_id)
            elif container_type == "L":
                containers[container_id] = LiquidContainer(container_id)
            elif container_type == "H":
                containers[container_id] = BasicContainer(container_id)
        else:
            containers[container_id] = HeavyContainer(container_id)

    elif action == "create_item":
        item_id = operation["id"]
        item_weight = operation["weight"]
        item_count = operation["count"]
        items[item_id] = Item(item_id, item_weight, item_count)

    elif action == "load_item":
        container_id = operation["container_id"]
        item_id = operation["item_id"]
        container = containers[container_id]
        item = items[item_id]
        container.load(item)

    elif action == "load_container":
        ship_id = operation["ship_id"]
        container_id = operation["container_id"]
        ship = ships[ship_id]
        container = containers[container_id]
        ship.load(container)

    elif action == "unload_container":
        ship_id = operation["ship_id"]
        container_id = operation["container_id"]
        ship = ships[ship_id]
        container = containers[container_id]
        ship.unload(container)

    elif action == "ship_sail":
        ship_id = operation["ship_id"]
        destination_port_id = operation["destination_port_id"]
        ship = ships[ship_id]
        destination_port = ports[destination_port_id]
        ship.sail_to(destination_port)

    elif action == "refuel":
        ship_id = operation["ship_id"]
        new_fuel = operation["fuel"]
        ship = ships[ship_id]
        ship.refuel(new_fuel)


# Generates output JSON
def generate_output(ports):
    output = {}
    for port_id, port in ports.items():
        port_data = {
            "lat": round(port.latitude, 2),
            "lon": round(port.longitude, 2),
            "basic_container": [],
            "heavy_container": [],
            "refrigerated_container": [],
            "liquid_container": [],
            "ships": []
        }

        # Add containers in the port
        for container in port.containers:
            if isinstance(container, BasicContainer):
                port_data["basic_container"].append(container.id)
            elif isinstance(container, RefrigeratedContainer):
                port_data["refrigerated_container"].append(container.id)
            elif isinstance(container, LiquidContainer):
                port_data["liquid_container"].append(container.id)
            else:
                port_data["heavy_container"].append(container.id)

        # Add ships in the port
        for ship in port.current_ships:
            ship_data = {
                "id": ship.id,
                "fuel_left": round(ship.fuel, 2),
                "basic_container": [],
                "heavy_container": [],
                "refrigerated_container": [],
                "liquid_container": []
            }
            for container in ship.containers:
                if isinstance(container, BasicContainer):
                    ship_data["basic_container"].append(container.id)
                elif isinstance(container, RefrigeratedContainer):
                    ship_data["refrigerated_container"].append(container.id)
                elif isinstance(container, LiquidContainer):
                    ship_data["liquid_container"].append(container.id)
                else:
                    ship_data["heavy_container"].append(container.id)
            port_data["ships"].append(ship_data)

        output[f"Port {port_id}"] = port_data
    return output


if __name__ == "__main__":
    main("input.json", "output.json")
