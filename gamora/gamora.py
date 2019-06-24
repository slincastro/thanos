#from umqttsimple import MQTTClient

from umqtt.robust import MQTTClient
import machine
import time
import network
import ubinascii


def set_led(pin):
    
    pin =  machine.Pin(pin, machine.Pin.OUT)
    
    return pin

def blink_led(led):

    for i in range(4):
        off_leds()
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)

    return

def off_leds():
    
    blue_led.value(1)
    red_led.value(1)
    green_led.value(1)

    return

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'myfirst/test'
topic_pub = b'myfirst/test'
mqtt_server = b'10.76.124.45'

blue_led = set_led(5)
red_led = set_led(4)
green_led = set_led(16)

routercon = network.WLAN(network.STA_IF)

if routercon.active():
    blink_led(green_led)
else:
    blink_led(red_led)

routercon.active(True)
routercon.connect('twguest', 'heroic crab mammal dual swig')

wifiap = network.WLAN(network.AP_IF)

if wifiap.active():
    blink_led(green_led)
else:
    blink_led(red_led)

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient("espClient", mqtt_server,"1883")
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

msg= " hi from python "
connect_and_subscribe()
client.publish(topic_pub, msg)