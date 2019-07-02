import time


class RGBLed:
    def __init__(self, leds):
        self.leds = leds
        pass

    def blink(self, led):
        for x in range(0, 3):
            self.leds[x].off()
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

        return
