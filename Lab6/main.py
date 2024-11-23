class SingletonMeta(type):
    """
    A metaclass for Singleton pattern implementation.
    """
    _instances = {}

    def call(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().call(*args, **kwargs)
        return cls._instances[cls]


class SettingsManager(metaclass=SingletonMeta):
    """
    Singleton for managing global settings in the smart home.
    """
    def __init__(self):
        self.settings = {"temperature": 22, "lighting_mode": "default"}

    def update_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key, None)


class EnergyManager(metaclass=SingletonMeta):
    """
    Singleton for monitoring and managing energy usage.
    """
    def __init__(self):
        self.energy_usage = 0

    def monitor_usage(self):
        print("Monitoring energy usage...")

    def optimize_energy(self):
        print("Optimizing energy usage...")


class LightingSystem:
    def turn_on_lights(self):
        print("Lights turned on.")

    def turn_off_lights(self):
        print("Lights turned off.")

    def set_brightness(self, level):
        print(f"Brightness set to {level}.")


class SecuritySystem:
    def arm_system(self):
        print("Security system armed.")

    def disarm_system(self):
        print("Security system disarmed.")

    def trigger_alarm(self):
        print("Alarm triggered!")


class ClimateControlSystem:
    def set_temperature(self, temp):
        print(f"Temperature set to {temp}°C.")

    def turn_on_heater(self):
        print("Heater turned on.")

    def turn_on_ac(self):
        print("Air conditioner turned on.")


class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightingSystem()
        self.security = SecuritySystem()
        self.climate = ClimateControlSystem()

    def activate_security_system(self):
        self.security.arm_system()

    def control_lighting(self, action, brightness=None):
        if action == "on":
            self.lighting.turn_on_lights()
        elif action == "off":
            self.lighting.turn_off_lights()
        if brightness is not None:
            self.lighting.set_brightness(brightness)

    def set_climate_control(self, temperature):
        self.climate.set_temperature(temperature)


class Appliance:
    def start(self):
        raise NotImplementedError("Start method must be implemented.")

    def stop(self):
        raise NotImplementedError("Stop method must be implemented.")


class Fan(Appliance):
    def start(self):
        print("Fan started.")

    def stop(self):
        print("Fan stopped.")


class Switch:
    def __init__(self, appliance):
        self.appliance = appliance

    def turn_on(self):
        self.appliance.start()

    def turn_off(self):
        self.appliance.stop()


if __name__ == "__main__":
    # Singleton Example
    settings = SettingsManager()
    settings.update_setting("temperature", 24)
    print("Current temperature setting:", settings.get_setting("temperature"))

    # Facade Example
    smart_home = SmartHomeFacade()
    smart_home.control_lighting("on", brightness=70)
    smart_home.set_climate_control(22)
    smart_home.activate_security_system()

    # Bridge Example
    fan = Fan()
    fan_switch = Switch(fan)
    fan_switch.turn_on()
    fan_switch.turn_off()
