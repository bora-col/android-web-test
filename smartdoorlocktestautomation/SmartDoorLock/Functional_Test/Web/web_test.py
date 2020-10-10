import pytest
from selenium import webdriver
import os
import sys
sys.path.append('/Users/user/Desktop/smartdoorlocktestautomation')
import SmartDoorLock.Configuration.base_config as Config


# initializing of the chrome driver
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(Config.Configuration.get_chrome_driver())
    # os.chmod(chrome_driver, 484)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


# Navigate to smart door lock website.
# Check if page title is correct
@pytest.mark.usefixtures("chrome_driver_init")
class TestPageTitle:
    URL = Config.Configuration.get_admin_panel_url()

    def test_open_url(self):
        self.driver.get(self.URL)
        page_title = self.driver.title
        print("\nTitle: " + page_title)
        assert page_title == "Biss Smart Lock"
