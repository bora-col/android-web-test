import pytest
from appium import webdriver
import sys
sys.path.append('/Users/user/Desktop/smartdoorlocktestautomation')
import SmartDoorLock.Configuration.base_config as base_config


class TestMobileApp:
    open_garden_door_slider = base_config.Configuration.get_open_door_slider_xpath()
    open_door_button = base_config.Configuration.get_open_the_door_button_xpath()

    # define desired capabilities of the mobile application
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_cap = {
            "deviceName": base_config.Configuration.get_device_name(),
            "platformName": base_config.Configuration.get_platform_name(),
            "app": base_config.Configuration.get_apk_path(),
            "appPackage": base_config.Configuration.get_app_package(),
            "appWaitActivity": base_config.Configuration.get_app_wait_activity(),
            "noReset": base_config.Configuration.get_no_reset(),
            "automationName": base_config.Configuration.get_automation_name()
        }
        driver = webdriver.Remote(base_config.Configuration.get_appium_driver(), desired_cap)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value

    def test_check_the_open_garden_door_slider(self, driver):
        driver.implicitly_wait(5000)
        open_garden_door_slider = driver.find_element_by_xpath(self.open_garden_door_slider)
        print("\nIs the open garden door slider displayed? \n" + str(open_garden_door_slider.is_displayed()) + "\n")
        assert open_garden_door_slider.is_displayed()

    def test_open_the_door_button(self, driver):
        driver.implicitly_wait(5000)
        open_door_button = driver.find_element_by_xpath(self.open_door_button)
        print("\nIs the open the door button displayed? \n" + str(open_door_button.is_displayed()) + "\n")
        assert open_door_button.is_displayed()
