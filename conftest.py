import pytest

@pytest.fixture(scope='session')
def android_setting():
    des = {
        'platformName': 'Android',
        'appium:platformVersion': '13',  # 替换为您设备的 Android 版本号
        'appium:deviceName': 'GalaxyM13',  # 替换为您的设备名称或 ID
        'appium:automationName': 'uiautomator2',
        # 'appPackage': 'com.sec.android.app.popupcalculator',  # 填写被测app包名
        # 'appActivity': '.Calculator',  # 填写被测app的入口
        'noReset': False
    }
    return des
