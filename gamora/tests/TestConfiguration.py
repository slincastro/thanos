import json
import sys
import unittest
sys.path.append('../')

from configuration.Configuration import Configuration


class TestConfiguration(unittest.TestCase):

    def test_should_load_file(self):
        configuration = Configuration("testConfig.json")
        expected_json = json.loads('{"clientId": "espClientTest",'
                                   ' "wifiSsid" : "wifiTest", '
                                   '"wifiSecret" : "secreTtest"}')

        json_data = configuration.read_json()

        self.assertEquals(json_data, expected_json)

    def test_should_return_client_id_value(self):
        configuration = Configuration("testConfig.json")

        self.assertEquals(configuration.mqtt.client_id, "espClientTest")

    def test_should_load_mqtt_parameters(self):
        configuration = Configuration("../config.json")

        mqtt_configuration = configuration.mqtt

        self.assertEquals(mqtt_configuration.topic_sub, "myfirst/test")
        self.assertEquals(mqtt_configuration.topic_pub, "myfirst/test")
        self.assertEquals(mqtt_configuration.mqtt_server, "10.76.124.45")

    def test_should_load_wifi_parameters(self):
        configuration = Configuration("testConfig.json")

        wifi_configuration = configuration.wifi

        self.assertEquals(wifi_configuration.ssid, "wifiTest")
        self.assertEquals(wifi_configuration.secret, "secreTtest")
