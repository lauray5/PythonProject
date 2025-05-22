import json
import allure
import jsonpath
from common.assertions import Assertions
from common.readyaml import get_testcase_yaml
from common.sendrequest import SendRequest
from conf.operationConfig import OperationConfig
from configparser import ConfigParser


class RequestBase:
    def __init__(self):
        self.conf = ConfigParser()
        self.run = SendRequest()

    def specification_yaml(self, base_info, test_case):
        """适配YAML测试用例的入口方法"""
        url_host = self.conf.get_section_for_data('api_envi', 'host')
        return self.run.run_main(
            name=base_info['api_name'],
            url=url_host + base_info['url'],
            method=base_info['method'],
            header=base_info.get('header'),
            **test_case  # 包含case_name/request_params/validation
        )

