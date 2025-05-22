import allure
import jsonpath
from common.recordlog import logs
import logging
import allure
from jsonpath import jsonpath
logs = logging.getLogger(__name__)

class Assertions:
    def contains_assert(self, value, response, status_code):
        flag = 0
        for assert_key, assert_value in value.items():
            if assert_key == "status_code":
                if assert_value != status_code:
                    flag += 1
                    allure.attach(f"预期结果：{assert_value}\\n实际结果：{status_code}", '响应代码断言结果:失败',
                                  attachment_type=allure.attachment_type.TEXT)
                    logs.error("contains断言失败：接口返回码【%s】不等于【%s】" % (status_code, assert_value))
            else:
                resp_list = jsonpath.jsonpath(response, f"$..{assert_key}")
                if resp_list:
                    if assert_value in resp_list[0]:
                        logs.info("字符串包含断言成功：预期结果【%s】,实际结果【%s】" % (assert_value, resp_list[0]))
                    else:
                        flag = flag + 1
                        allure.attach(f"预期结果：{assert_value}\\n实际结果：{resp_list[0]}", '响应文本断言结果：失败',
                                      attachment_type=allure.attachment_type.TEXT)
                        logs.error("响应文本断言失败：预期结果为【%s】,实际结果为【%s】" % (assert_value, resp_list[0]))
        return flag

    def assert_result(self, expected, response, status_code):
        all_flag = 0
        for yq in expected:
            for key, value in yq.items():
                if key == "contains":
                    flag = self.contains_assert(value, response, status_code)
                    all_flag = all_flag + flag
        if all_flag == 0:
            logs.info("测试成功")
            assert True
        else:
            logs.error("测试失败")
            assert False
