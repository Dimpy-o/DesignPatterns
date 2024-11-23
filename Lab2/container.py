class Container:
    def __init__(self, container_id, weight):
        self.id = container_id
        self.weight = weight
        self.consumption_basic = 0.025
        self.consumption_heavy = 0.03
        self.consumption_refrigerated = 0.05
        self.consumption_liquid = 0.04

    def consumption(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def __eq__(self, other):
        return (
            isinstance(other, Container) and
            self.id == other.id and
            self.weight == other.weight
        )


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
