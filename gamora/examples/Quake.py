import network
import machine
import time

class Quake:
    def __init__(self):
        
        pass

    def connect(self):
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        sta_if.connect("", "") #Insert wifi configuration

        while not sta_if.isconnected():
            led = machine.Pin(4, machine.Pin.OUT)
            led.value(1)
            time.sleep(0.5)
            led.value(0)
       
        ok_led = machine.Pin(5, machine.Pin.OUT)
        ok_led.value(1)
        time.sleep(4.5)
        return sta_if

green_led = machine.Pin(16, machine.Pin.OUT)
green_led.value(0)
Quake().connect()