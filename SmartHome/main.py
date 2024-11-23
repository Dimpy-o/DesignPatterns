from fastapi import FastAPI
from facade.smart_home_facade import SmartHomeFacade

app = FastAPI()
facade = SmartHomeFacade()


@app.get("/")
def home():
    return {"message": "Welcome to Smart Home API"}


@app.post("/lighting/on")
def turn_on_lights():
    facade.controlLighting(100)
    return {"status": "Lights turned on"}


@app.post("/security/activate")
def activate_security():
    facade.activateSecuritySystem()
    return {"status": "Security system activated"}


@app.post("/climate/set/{temperature}")
def set_climate(temperature: int):
    facade.setClimateControl(temperature)
    return {"status": f"Climate set to {temperature}°C"}


@app.post("/entertainment/music/on")
def play_music():
    facade.playMusic()


@app.post("/entertainment/music/off")
def stop_music():
    facade.stopMusic()


@app.post("/entertainment/music/volume")
def set_volume(volume: int):
    facade.setVolume(volume)
    return {"status": f"Volume set to {volume}°C"}