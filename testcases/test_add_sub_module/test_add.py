import allure, re
from appium.webdriver.webdriver import By
from pathlib import Path

@allure.epic('androidCalculatorItem')
@allure.feature('v1.0')
class TestAddSub():
    @allure.story('Add Calculator')
    @allure.title('[case01] Verify that the calculator can complete the addition function normally')
    def test_add(self, start_app, close_app):
        with allure.step('1. Launch the calculator app in Android'):
            driver = start_app
        with allure.step('2. Press 9, +, 8, ='):
            driver.find_element(By.ID,'com.sec.android.app.popupcalculator:id/calc_keypad_btn_09').click()
            driver.get_screenshot_as_file(rf'report/img/test_add/test01.png')
            allure.attach.file(f"report/img/test_add/test01.png", name="test_1", attachment_type=allure.attachment_type.PNG)

            driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="加號"]').click()
            driver.get_screenshot_as_file(rf'report/img/test_add/test02.png')
            allure.attach.file(f"report/img/test_add/test02.png", name="test_2", attachment_type=allure.attachment_type.PNG)

            driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_08').click()
            driver.get_screenshot_as_file(rf'report/img/test_add/test03.png')
            allure.attach.file(f"report/img/test_add/test03.png", name="test_3", attachment_type=allure.attachment_type.PNG)

            driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="等於"]').click()
            driver.get_screenshot_as_file(rf'report/img/test_add/test04.png')
            allure.attach.file(f"report/img/test_add/test04.png", name="test_4", attachment_type=allure.attachment_type.PNG)

            actual_result = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.sec.android.app.popupcalculator:id/calc_edt_formula"]').text
        with allure.step('3. Verify that the result are correct'):
            result_num = re.sub('[\u4e00-\u9fa5]', '', actual_result).replace(' ', '')
            assert result_num == '17'
