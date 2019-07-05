import time


class RGBLed:
    def __init__(self, red_led, green_led, blue_led,):
        self.leds = [red_led, blue_led, green_led]
        self.red_led = red_led
        self.blue_led = blue_led
        self.green_led = green_led
        pass

    def blink(self, led):
        for x in range(0, 3):
            self.leds[x].off()
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

        return
