import json
from port import Port
from ship import Ship
from container import RefrigeratedContainer, LiquidContainer, BasicContainer, HeavyContainer


# Main function to read input and execute operations
def main(input_file, output_file):
    # Load input JSON
    with open(input_file, 'r') as file:
        operations = json.load(file)

    # Initialize entities
    ports = {}
    ships = {}
    containers = {}

    for op in operations:
        # Parse and execute operation
        execute_operation(op, ports, ships, containers)

    # Generate output
    output = generate_output(ports)
    with open(output_file, 'w') as file:
        json.dump(output, file, indent=4)


# Executes individual operations based on their type
def execute_operation(operation, ports, ships, containers):
    action = operation["action"]

    if action == "create_port":
        port_id = operation["id"]
        latitude = operation["latitude"]
        longitude = operation["longitude"]
        ports[port_id] = Port(port_id, latitude, longitude)

    elif action == "create_ship":
        ship_id = operation["id"]
        port_id = operation["port"]
        weight_cap = operation["weight_capacity"]
        max_containers = operation["max_containers"]
        max_heavy = operation["max_heavy"]
        max_refrig = operation["max_refrigerated"]
        max_liquid = operation["max_liquid"]
        fuel_per_km = operation["fuel_per_km"]
        ships[ship_id] = Ship(ship_id, ports[port_id], weight_cap, max_containers, max_heavy, max_refrig, max_liquid, fuel_per_km)
        ports[port_id].incoming_ship(ships[ship_id])

    elif action == "create_container":
        container_id = operation["id"]
        weight = operation["weight"]
        if "type" in operation:
            container_type = operation["type"]
            if container_type == "R":
                containers[container_id] = RefrigeratedContainer(container_id, weight)
            elif container_type == "L":
                containers[container_id] = LiquidContainer(container_id, weight)
        elif weight <= 3000:
            containers[container_id] = BasicContainer(container_id, weight)
        else:
            containers[container_id] = HeavyContainer(container_id, weight)

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
