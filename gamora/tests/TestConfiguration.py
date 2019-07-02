import json
import sys
import unittest
sys.path.append('../')

from Configuration import Configuration


class TestConfiguration(unittest.TestCase):

    def test_should_load_file(self):
        configuration = Configuration("testConfig.json")
        expected_json = json.loads('{"clientId": "espClientTest"}')

        json_data = configuration.read_json()

        self.assertEquals(json_data, expected_json)

    def test_should_return_client_id_value(self):
        configuration = Configuration("testConfig.json")
        json_data = configuration.read_json()

        configuration.json_to_object(json_data)

        self.assertEquals(configuration.client_id, "espClientTest")


