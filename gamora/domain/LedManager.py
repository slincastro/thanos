import time


class LedManager:

    def __init__(self, blue_led, red_led, green_led):
        self.blue_led = blue_led
        self.red_led = red_led
        self.green_led = green_led
        
    def blink_led(self, led):

        for i in range(1):
            self.off_leds()
            led.value(1)
            time.sleep(0.5)
            led.value(0)
            time.sleep(0.5)

        return

    def off_leds(self):
        
        self.blue_led.value(1)
        self.red_led.value(1)
        self.green_led.value(1)

        return
