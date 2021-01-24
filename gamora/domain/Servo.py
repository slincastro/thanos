import machine

class Servo:
    def __init__(self, pin_number):
        self.pin_number = pin_number
        self.pin = machine.Pin(pin_number, machine.Pin.OUT)
        self.servo = machine.PWM(self.pin,freq=50)
        pass

    def Move(self, pulse_number):
        self.servo.duty(pulse_number)

    def Open(self):
        self.Move(45)
    
    def Close(self):
        self.Move(95)
