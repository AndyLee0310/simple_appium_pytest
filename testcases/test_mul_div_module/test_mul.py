import allure, re
from appium.webdriver.webdriver import By
 
@allure.epic('安卓计算机项目')
@allure.feature('V1.0版本')
class TestAddSub():
    @allure.story('乘法运算')
    @allure.title('[case02] 验证计算机能否正常完成乘法功能')
    def test_mul(self,start_app,close_app):
        with allure.step('1、启动安卓系统中的计算机app'):
            driver = start_app
        with allure.step('2、依次按下3、*、4、='):
            driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_03').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="乘法"]').click()
            driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_04').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="等於"]').click()
            actual_result = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.sec.android.app.popupcalculator:id/calc_edt_formula"]').text
        with allure.step('3、验证实际结果是否正确'):
            result_num = re.sub('[\u4e00-\u9fa5]', '', actual_result).replace(' ', '')
            assert result_num == '12'
