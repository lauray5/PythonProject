import configparser

class OperationConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('conf/config.ini', encoding='utf-8')

    def get_section_for_data(self, section, option):
        return self.config.get(section, option)
