import json


class Configuration:

    def __init__(self, configuration_path):
        self.mqtt = None
        self.mqtt.mqtt_server = None
        self.mqtt.topic_sub = None
        self.mqtt.topic_pub = None
        self.mqtt.client_id = None

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
        pass

    def extract_value(self, key):

        if key in self.file_data:
            return self.file_data[key]
        else:
            return ""


