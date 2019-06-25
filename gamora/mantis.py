from umqtt.simple import MQTTClient
import machine
import time
import network
import ubinascii

def set_led(pin):
    pin =  machine.Pin(pin, machine.Pin.OUT)
    return pin

def blink_led(led):

    for i in range(1):
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
client = MQTTClient(client_id="espClientTest", server=mqtt_server)
  
blue_led = set_led(5)
red_led = set_led(4)
green_led = set_led(16)

sta_if = network.WLAN(network.STA_IF)
sta_if.connect('twguest', 'heroic crab mammal dual swig')

while not sta_if.isconnected():
    blink_led(red_led)

blink_led(green_led)

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')

def connect_and_subscribe():
  #global client_id, mqtt_server, topic_sub
  client.set_callback(sub_cb)
  while not client.connect() :
        time.sleep(4.5)
        blink_led(blue_led)
        msg= " hi from python "
        client.publish(topic_pub, msg)
  #client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client


connect_and_subscribe()
