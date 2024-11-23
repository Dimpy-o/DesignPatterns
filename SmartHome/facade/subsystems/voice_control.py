class VoiceControl:
    def processCommand(self, command, facade):
        if "light" in command.lower():
            facade.controlLighting(50)
        elif "security" in command.lower():
            facade.activateSecuritySystem()
        elif "temperature" in command.lower():
            facade.setClimateControl(24)
        else:
            print("Command not recognized.")
