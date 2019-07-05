import json
import sys
sys.path.append('../')
from configuration.MQTTConfiguration import MQTTConfiguration
from configuration.WifiConfiguration import WifiConfiguration


class Configuration:

    def __init__(self, configuration_path):
        self.wifi = WifiConfiguration()
        self.mqtt = MQTTConfiguration()

        self.configuration_path = configuration_path
        self.file_data = self.read_json()
        self.json_to_object()

    def read_json(self):
        file_content = open(self.configuration_path, 'r')
        configuration = json.load(file_content)

        return configuration

    def json_to_object(self):

        self.mqtt.client_id = self.extract_value("clientId")
        self.mqtt.topic_sub = self.extract_value("topicSubscription")
        self.mqtt.topic_pub = self.extract_value("topicPublication")
        self.mqtt.mqtt_server = self.extract_value("mqttServer")
        self.wifi.ssid = self.extract_value("wifiSsid")
        self.wifi.secret = self.extract_value("wifiSecret")
        pass

    def extract_value(self, key):

        if key in self.file_data:
            return self.file_data[key]
        else:
            return ""


