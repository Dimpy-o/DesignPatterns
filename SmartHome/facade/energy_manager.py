class EnergyManager(metaclass=SingletonMeta):
    def __init__(self):
        self.energy_usage = {}

    def monitor_usage(self):
        print("Monitoring energy usage...")

    def optimize_energy(self):
        print("Optimizing energy consumption...")
