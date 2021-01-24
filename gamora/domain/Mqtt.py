from umqtt.simple import MQTTClient
from domain.Servo import Servo
import time


class Mqtt:
    def __init__(self, configuration, rgb_led, wifi_connection):
        self.configuration = configuration

        
        self.write_log("clinetID : "+ self.configuration.mqtt.client_id +
                " server :" + self.configuration.mqtt.mqtt_server + "\n")
        self.write_log("pub topic : "+ self.configuration.mqtt.topic_pub + "\n")
        self.write_log("pub topic : "+ self.configuration.mqtt.topic_pub + "\n")
        self.wifi_connection = wifi_connection
        self.rgb_led = rgb_led
        self.servo = Servo(14)
        self.pulse = 40

    def connect(self):
        pass

    def sub_cb(self, topic, msg):
        message = str(msg)
        self.rgb_led.blink(self.rgb_led.green_led)
        self.write_log("receiving message =>" + message)
        if "open" in message:
            self.servo.Move(45)
            self.write_log("open")
        elif "close" in message:
            self.servo.Move(95)
            self.write_log("close")


    def connect_and_subscribe(self):
        self.write_log("start connection to server")
        client = MQTTClient(self.configuration.mqtt.client_id, self.configuration.mqtt.mqtt_server)    
        self.write_log("setting callback")
        client.set_callback(self.sub_cb)
        
        retry = 0
        self.write_log("wifi status :" + str(self.wifi_connection.isconnected()))
        self.write_log("wifi config :" + str(self.wifi_connection.ifconfig()))
        while retry < 20: 
            try:
                while not client.connect():
                    time.sleep(4.5)
                    self.rgb_led.blink(self.rgb_led.blue_led)
                    msg = " hi from python :"+ str(retry)
                    self.write_log("connecting to server ....")
                    #client.publish(self.configuration.mqtt.topic_pub, msg)
                    client.subscribe(b"myfirst/test")
                    client.wait_msg()
                    reconection = False
            except Exception as e:
                    self.write_log("Can't connect to mqtt..... try:" + str(retry+1))
                    self.write_log(str(e))
                    self.rgb_led.blink(self.rgb_led.red_led)
            finally:
                    self.write_log("finish connection proccess ....")
                    retry+=1
                    pass
            time.sleep(5)

    def write_log(self, message):
        f = open("log.txt", "a")
        f.write(message + " \n")
        f.close()