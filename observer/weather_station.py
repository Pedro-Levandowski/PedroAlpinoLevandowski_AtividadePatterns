from observer import TemperatureObserver


class WeatherStation:
    def __init__(self):
        self._observers: list[TemperatureObserver] = []
        self._temperature: float = 0.0

    def subscribe(self, o: TemperatureObserver) -> None:
        if o not in self._observers:
            self._observers.append(o)

    def unsubscribe(self, o: TemperatureObserver) -> None:
        if o in self._observers:
            self._observers.remove(o)

    def set_temperature(self, temp: float) -> None:
        self._temperature = temp
        self._notify_observers()

    def _notify_observers(self) -> None:
        for o in self._observers:
            o.on_temperature_changed(self._temperature)
