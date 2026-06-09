from weather_station import WeatherStation
from observer import ConsoleDisplay, FanController

if __name__ == '__main__':
    station = WeatherStation()

    display = ConsoleDisplay()
    fan = FanController()

    station.subscribe(display)
    station.subscribe(fan)

    station.set_temperature(26)
    station.set_temperature(30)

    station.unsubscribe(display)

    station.set_temperature(27)
