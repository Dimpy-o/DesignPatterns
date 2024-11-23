class Switch:
    def __init__(self, appliance):
        self.appliance = appliance

    def turn_on(self):
        self.appliance.start()

    def turn_off(self):
        self.appliance.stop()
