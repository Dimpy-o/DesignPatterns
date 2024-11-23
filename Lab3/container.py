class Container:
    def __init__(self, container_id):
        self.id = container_id
        self.weight = 0.00
        self.consumption_basic = 2.50
        self.consumption_heavy = 3.00
        self.consumption_refrigerated = 5.00
        self.consumption_liquid = 4.00
        self.max_items = 1000
        self.items = []

    def consumption(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def __eq__(self, other):
        return (
            isinstance(other, Container) and
            self.id == other.id and
            self.weight == other.weight
        )

    def load(self, item):
        if len(self.items) >= self.max_items:
            print("Cannot load: Maximum item count exceeded.")
            return False

        self.weight = sum(c.weight for c in self.items) + item.weight
        print(f"DEBUGDEBUGDEBUG{self.weight}DEBUGDEBUGDEBUG")

        self.items.append(item)
        print(f"Item {item.id} loaded successfully.")
        return True

    def unload(self, item):
        if item not in self.item:
            print(f"Cannot unload: Item {item.id} is not in the container.")
            return False

        self.items.remove(item)
#        self.current_port.items.append(item)
        print(f"Item {item.id} unloaded successfully.")
        return True


class BasicContainer(Container):
    def consumption(self):
        return self.consumption_basic * self.weight


class HeavyContainer(Container):
    def consumption(self):
        return self.consumption_heavy * self.weight


class RefrigeratedContainer(HeavyContainer):
    def consumption(self):
        return self.consumption_refrigerated * self.weight


class LiquidContainer(HeavyContainer):
    def consumption(self):
        return self.consumption_liquid * self.weight
