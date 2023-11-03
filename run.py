import os
import pytest

current_path = os.path.dirname(os.path.abspath(__file__))

json_report_path = os.path.join(current_path, 'report/json')
html_report_path = os.path.join(current_path, 'report/html')

pytest.main(['-s', '-v', f'--alluredir={json_report_path}', '--clean-alluredir'])
# os.system('allure generate %s -o %s --clean'%(json_report_path, html_report_path))
os.system(f'allure generate {json_report_path} -o {html_report_path} --clean')
