from umqtt.simple import MQTTClient
from domain.Led import Led
from domain.LedRGB import RGBLed
import machine
import time
import network
import ubinascii
import json


file = open('config.json', 'r')
configuration = json.load(file)

#client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = configuration['topicSubscription']
topic_pub = configuration['topicPublication']
mqtt_server = configuration['mqttServer']
client_id = configuration['clientId']
wifi_ssid = 'twguest'
wifi_secret = 'heroic crab mammal dual swig'
client = MQTTClient(client_id, mqtt_server)
sta_if = network.WLAN(network.STA_IF)


blue_led = Led(5)
red_led = Led(4)
green_led = Led(16)

rgb_led = RGBLed([blue_led, red_led, green_led])

sta_if.connect(wifi_ssid, wifi_secret)
while not sta_if.isconnected():
    rgb_led.blink(red_led)

rgb_led.blink(green_led)


def sub_cb(topic, msg):
    print(topic, msg)
    if topic == b'notification' and msg == b'received':
        print('ESP received hello message')


def connect_and_subscribe():
    client.set_callback(sub_cb)
    while not client.connect():
        time.sleep(4.5)
        rgb_led.blink(blue_led)
        msg= " hi from python "
        client.publish(topic_pub, msg)
    #client.subscribe(topic_sub)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return client


connect_and_subscribe()
