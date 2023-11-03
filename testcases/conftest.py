import time
import pytest
from appium import webdriver

driver = None

@pytest.fixture()
def start_app(android_setting):
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723', android_setting)
    return driver

@pytest.fixture()
def close_app():
    yield driver
    time.sleep(2)
    driver.close_app()