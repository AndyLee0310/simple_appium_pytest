import allure, re
from appium.webdriver.webdriver import By
 
@allure.epic('androidCalculatorItem')
@allure.feature('v1.0')
class TestAddSub():
    @allure.story('Sub Calculator')
    @allure.title('[case02] Verify that the calculator can complete the subtraction function normally')
    def test_sub(self,start_app,close_app):
        with allure.step('1. Launch the calculator app in Android'):
            driver = start_app
        with allure.step('2. Press 6, -, 2, ='):
            driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_06').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="減號"]').click()
            driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_02').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="等於"]').click()
            actual_result = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.sec.android.app.popupcalculator:id/calc_edt_formula"]').text
        with allure.step('3. Verify that the result are correct'):
            result_num = re.sub('[\u4e00-\u9fa5]', '', actual_result).replace(' ', '')
            assert result_num == '4'