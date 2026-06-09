from abc import ABC, abstractmethod


class TemperatureObserver(ABC):
    @abstractmethod
    def on_temperature_changed(self, temp: float) -> None:
        pass


class ConsoleDisplay(TemperatureObserver):
    def on_temperature_changed(self, temp: float) -> None:
        print(f'Display: temperatura = {float(temp):.1f}')


class FanController(TemperatureObserver):
    def on_temperature_changed(self, temp: float) -> None:
        if temp > 28:
            print('Ventilador: LIGAR')
        else:
            print('Ventilador: DESLIGAR')
