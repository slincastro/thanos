import json


class Configuration:

    def __init__(self, configuration_path):
        self.configuration_path = configuration_path
        self.client_id = None
        self.json_to_object(self.read_json())
        pass

    def read_json(self):
        file_content = open(self.configuration_path, 'r')
        configuration = json.load(file_content)

        return configuration

    def json_to_object(self, file_data):

        self.client_id = file_data["clientId"]

        pass


