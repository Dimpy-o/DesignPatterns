class Appliance:
    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError


class SmartBulb(Appliance):
    def start(self):
        print("Smart Bulb turned on.")

    def stop(self):
        print("Smart Bulb turned off.")


class SmartFan(Appliance):
    def start(self):
        print("Smart Fan turned on.")

    def stop(self):
        print("Smart Fan turned off.")
