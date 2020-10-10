import pytest
from selenium import webdriver
import sys
sys.path.append('/Users/user/Desktop/smartdoorlocktestautomation')
import SmartDoorLock.Configuration.base_config as base_config
from SmartDoorLock.Helper.parse_data import ParseData


# initializing of the chrome driver
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(base_config.Configuration.get_chrome_driver())
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("chrome_driver_init")
class TestDoorStatus:
    door_status_xpath = base_config.Configuration.get_door_status_xpath()
    URL = base_config.Configuration.get_admin_panel_url()
    data_json_path = "data_web_embedded.json"

    # Check the value on the web ui and compare it with the value received via socket.io
    def test_door_status(self):
        self.driver.get(self.URL)
        office_id, status, data = ParseData.parse_data(self.data_json_path)
        print("\nData in the server: " + str(status))
        door_status = webdriver.Chrome.find_element_by_xpath(self.driver, self.door_status_xpath)
        door_status_text = door_status.text
        print("\nData in the web: " + door_status_text)
        if status == -1:
            assert door_status_text == "Unknown"
        elif status == 0:
            assert door_status_text == "Open"
        elif status == 1:
            assert door_status_text == "Closed / Unlocked"
        elif status == 2:
            assert door_status_text == "Closed / Locked"
        elif status == 3:
            assert door_status_text == "Busy"
        elif status == 4:
            assert door_status_text == "Waiting"
