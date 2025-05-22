import shutil
import pytest
import os
import webbrowser
from conf.setting import REPORT_TYPE

if __name__ == '__main__':
    environment_xml_path = './environment.xml'
    if not os.path.exists(environment_xml_path):
        print(f"Error: {environment_xml_path} not found.")
    else:
        if REPORT_TYPE == 'allure':
            pytest.main([
                '-s', '-v',
                '--alluredir=./report/temp',
                './testcase',
                '--clean-alluredir',
                '--junitxml=./report/results.xml'
            ])
            shutil.copy(environment_xml_path, './report/temp')
            os.system('allure serve ./report/temp')
        elif REPORT_TYPE == 'tm':
            pytest.main([
                '-vs',
                '--pytest-tmreport-name=testReport.html',
                '--pytest-tmreport-path=./report/tmreport'
            ])
            webbrowser.open_new_tab(
                os.getcwd() + '/report/tmreport/testReport.html'
            )