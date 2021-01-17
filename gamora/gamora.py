from domain.Led import Led
from domain.LedRGB import RGBLed
from domain.Wifi import Wifi
from domain.Mqtt import Mqtt
from configuration.MQTTConfiguration import MQTTConfiguration
from configuration.Configuration import Configuration
import machine

configuration = Configuration("config.json")

blue_led = Led(5)
red_led = Led(4)
green_led = Led(16)

rgb_led = RGBLed(red_led, green_led, blue_led)

wifi = Wifi(configuration, rgb_led)

station_connection = wifi.connect()

mqtt = Mqtt(configuration, rgb_led, station_connection)

mqtt.connect_and_subscribe()
