import machine


class Led:
    def __init__(self, pin_number):
        self.pin_number = pin_number
        self.pin = machine.Pin(pin_number, machine.Pin.OUT)
        pass

    def on(self):
        self.pin.value(0)

    def off(self):
        self.pin.value(1)

