from configparser import ConfigParser
import requests
import allure
from common.recordlog import logs
import requests
import logging
import allure
logs = logging.getLogger(__name__)

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
            # 提取 request_params
            request_params = kwargs.get('request_params', {})
            # 根据请求方法处理 request_params
            if method.upper() == 'GET':
                request_kwargs = {'params': request_params}
            else:
                # 假设其他请求方法使用 JSON 数据
                request_kwargs = {'json': request_params}

            response = session.request(
                method=method,
                url=url,
                headers=header or {},
                **request_kwargs
            )
            logs.info(f'接口请求结束 | {name} | 状态码: {response.status_code}')
            # 提取出 validation 参数进行断言
            if 'validation' in kwargs:
                Assertions().assert_all(response, kwargs['validation'])
            return response
        except Exception as e:
            logs.error(f'请求异常: {e}')
            raise
