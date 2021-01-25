import network
from util.Log import Log


class Wifi:
    def __init__(self, configuration, rgb_led):
        self.configuration = configuration
        self.rgb_led = rgb_led
        pass

    def connect(self):
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        sta_if.connect(self.configuration.wifi.ssid, self.configuration.wifi.secret)

        while not sta_if.isconnected():
            self.rgb_led.blink(self.rgb_led.red_led)

        log = Log()
        log.write_log("IP configuration :")
        log.write_log(str(sta_if.ifconfig()))
        self.rgb_led.blink(self.rgb_led.green_led)
        return sta_if


