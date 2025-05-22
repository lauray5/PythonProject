import allure
import pytest
from base.generateId import m_id, c_id
from base.apiutil import RequestBase
from common.readyaml import get_testcase_yaml

@allure.feature(next(m_id) + '简单API测试模块')
class TestAPI:
    @allure.story(next(c_id) + "测试接口")
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml('./data/test_data.yaml'))
    def test_api(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)
