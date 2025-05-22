from configparser import ConfigParser
import requests
import allure
from common.recordlog import logs


class SendRequest:
    def _validate_response(self, response, validation_rules):
        """响应验证逻辑"""
        if validation_rules:
            if 'status_code' in validation_rules:
                assert response.status_code == validation_rules['status_code']
            if 'message' in validation_rules:
                assert validation_rules['message'] in response.text

    def run_main(self, name, url, method, header=None, **kwargs):
        """
        重构后的核心请求方法
        :param header: 默认为None避免与**kwargs冲突
        :param kwargs: 包含case_name/validation等扩展参数
        """
        session = requests.Session()
        try:
            logs.info(f'接口请求开始 | {name} | {url}')
            response = session.request(
                method=method,
                url=url,
                headers=header or {},
                **{k: v for k, v in kwargs.items() if k not in ['validation']}
            )
            self._validate_response(response, kwargs.get('validation'))
            return response
        except Exception as e:
            logs.error(f'请求异常: {str(e)}')
            allure.attach(str(e), '请求异常', allure.attachment_type.TEXT)
            raise


