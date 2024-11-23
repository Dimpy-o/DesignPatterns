from facade.subsystems.lighting_system import LightingSystem
from facade.subsystems.security_system import SecuritySystem
from facade.subsystems.climate_control import ClimateControlSystem
from facade.subsystems.entertainment_system import EntertainmentSystem


class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightingSystem()
        self.security = SecuritySystem()
        self.climate = ClimateControlSystem()
        self.entertainment = EntertainmentSystem()

    def activateSecuritySystem(self):
        self.security.armSystem()

    def setClimateControl(self, temperature):
        self.climate.setTemperature(temperature)

    def controlLighting(self, brightness):
        self.lighting.setBrightness(brightness)

    def playMusic(self):
        self.entertainment.playMusic()

    def stopMusic(self):
        self.entertainment.stopMusic()

    def setVolume(self, volume):
        self.entertainment.setVolume(volume)