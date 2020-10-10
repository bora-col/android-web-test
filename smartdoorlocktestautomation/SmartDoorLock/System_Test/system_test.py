import pytest
from appium import webdriver
from selenium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import sys
sys.path.append('/Users/user/Desktop/smartdoorlocktestautomation')
import SmartDoorLock.Configuration.base_config as base_config
from SmartDoorLock.Helper.parse_data import ParseData


class TestMobileApp:
    data_json_path = "data_mobile_embedded_system_test.json"
    office_id, status, data = ParseData.parse_data(data_json_path)

    lock_door_button_xp = base_config.Configuration().get_lock_the_door_button_xpath()
    do_nothing_button_xp = base_config.Configuration().get_do_nothing_button_xpath()
    activate_alarm_button_xp = base_config.Configuration().get_activate_alarm_button_xpath()
    popup_area_xp = base_config.Configuration().get_popup_area_xpath()
    open_door_button_xp = base_config.Configuration.get_open_the_door_button_xpath()
    door_status_xpath = base_config.Configuration.get_door_status_xpath()

    came_from_file_path = "Edge_Info/came_from.txt"
    my_came_from = None;
    driver = None;

    URL = base_config.Configuration.get_admin_panel_url()



    #EDGES
    def e_start_app(self,driver):
        driver.implicitly_wait(5000)

    def e_click_open(self,driver):
        driver.implicitly_wait(5000)
        open_door_button = driver.find_element_by_xpath(self.open_door_button_xp)
        print("\nIs the open the door button displayed? \n" + str(open_door_button.is_displayed()) + "\n")
        open_door_button.click()

    def e_press_open_lt3sec(self,driver):
        driver.implicitly_wait(5000)
        open_door_button = driver.find_element_by_xpath(self.open_door_button_xp)
        print("\nIs the open the door button displayed? \n" + str(open_door_button.is_displayed()) + "\n")
        touch_action = TouchAction(driver)
        touch_action.long_press(open_door_button, None, None, 2000).release().perform()

    def e_press_open_ge3sec(self,driver):
        driver.implicitly_wait(5000)
        open_door_button = driver.find_element_by_xpath(self.open_door_button_xp)
        print("\nIs the open the door button displayed? \n" + str(open_door_button.is_displayed()) + "\n")
        touch_action = TouchAction(driver)
        touch_action.long_press(open_door_button, None, None, 4000).release().perform()
        driver.implicitly_wait(5000)

    def e_timeout(self,driver):
        driver.implicitly_wait(9000)

    def e_click_lock(self,driver):
        driver.implicitly_wait(5000)
        lock_door_button = driver.find_element_by_xpath(self.lock_door_button_xp)
        print("\nIs the lock the door button displayed? \n" + str(lock_door_button.is_displayed()) + "\n")
        lock_door_button.click()

    def e_press_lock_ge3sec_and_click_do_nothing(self,driver):
        driver.implicitly_wait(10000)
        lock_door_button = driver.find_element_by_xpath(self.lock_door_button_xp)
        print("\nIs the lock the door button displayed? \n" + str(lock_door_button.is_displayed()) + "\n")
        touch_action = TouchAction(driver)
        touch_action.long_press(lock_door_button, None, None, 4000).release().perform()
        driver.implicitly_wait(3000)
        do_nothing_button = driver.find_element_by_xpath(self.do_nothing_button_xp)
        do_nothing_button.click()
        driver.implicitly_wait(10000)

    def e_press_lock_ge3sec_and_click_activate_alarm(self,driver):
        driver.implicitly_wait(10000)
        lock_door_button = driver.find_element_by_xpath(self.lock_door_button_xp)
        print("\nIs the lock the door button displayed? \n" + str(lock_door_button.is_displayed()) + "\n")
        touch_action = TouchAction(driver)
        touch_action.long_press(lock_door_button, None, None, 4000).release().perform()
        driver.implicitly_wait(3000)
        activate_alarm_button = driver.find_element_by_xpath(self.activate_alarm_button_xp)
        activate_alarm_button.click()
        driver.implicitly_wait(10000)

    def e_press_lock_lt3sec(self,driver):
        driver.implicitly_wait(7000)
        lock_door_button = driver.find_element_by_xpath(self.lock_door_button_xp)
        print("\nIs the lock the door button displayed? \n" + str(lock_door_button.is_displayed()) + "\n")
        touch_action = TouchAction(driver)
        touch_action.long_press(lock_door_button, None, None, 2000).release().perform()

    

    # define desired capabilities of the mobile application
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_cap = {
            # TODO (@alperen.bekci) this block will move under the base-mobile class with page-object model task.
            "deviceName": base_config.Configuration.get_device_name(),
            "platformName": base_config.Configuration.get_platform_name(),
            "app": base_config.Configuration.get_apk_path(),
            "appPackage": base_config.Configuration.get_app_package(),
            "appWaitActivity": base_config.Configuration.get_app_wait_activity()
        }
        driver = webdriver.Remote(base_config.Configuration.get_appium_driver(), desired_cap)


        #init my_came_from
        with open(self.came_from_file_path, "r") as cf:
            lines = cf.readlines()
            for line in lines:
                self.my_came_from = line.strip()
        print("init->my_came_from: ", self.my_came_from)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value

    




    # initializing of the chrome driver
    @pytest.fixture(scope="class")
    def chrome_driver_init(self, request):
        chrome_driver = webdriver.Chrome(base_config.Configuration.get_chrome_driver())
        request.cls.driver = chrome_driver
        yield
        chrome_driver.close()
        

    #VERTEXES
    @pytest.mark.usefixtures("chrome_driver_init")
    def test_unlock_the_door_sys(self, driver):
        edge_to_call = getattr(globals()['TestMobileApp'](), self.my_came_from)
        edge_to_call(driver)
        self.driver.get(self.URL)
        driver.implicitly_wait(7000)
        door_status = webdriver.Chrome.find_element_by_xpath(self.driver, self.door_status_xpath).text
        print("\nData in the server: " + str(self.status))
        print("\nData in the web: " + door_status)
        assert (door_status == "Closed / Unlocked" and self.status == 1)

    @pytest.mark.usefixtures("chrome_driver_init")
    def test_open_the_door_sys(self, driver):
        edge_to_call = getattr(globals()['TestMobileApp'](), self.my_came_from)
        edge_to_call(driver)
        self.driver.get(self.URL)
        driver.implicitly_wait(7000)
        door_status = webdriver.Chrome.find_element_by_xpath(self.driver, self.door_status_xpath).text
        print("\nData in the server: " + str(self.status))
        print("\nData in the web: " + door_status)
        assert (door_status == "Open" and self.status == 0)

    @pytest.mark.usefixtures("chrome_driver_init")
    def test_lock_the_door_sys(self, driver):
        # edge_to_call = getattr(sys.modules[__name__].TestMobileApp, self.my_came_from)
        # edge_to_call(driver,self.open_door_button_xp)
        # self.e_press_open_ge3sec(driver)
        self.driver.get(self.URL)
        driver.implicitly_wait(10000)
        lock_door_button = driver.find_element_by_xpath(self.lock_door_button_xp)
        # touch_action = TouchAction(self.driver)
        # touch_action.long_press(lock_door_button, None, None, 4000).release().perform()
        driver.implicitly_wait(3000)
        activate_alarm_button = driver.find_element_by_xpath(self.activate_alarm_button_xp)
        activate_alarm_button.click()
        driver.implicitly_wait(10000)
        door_status = webdriver.Chrome.find_element_by_xpath(self.driver, self.door_status_xpath).text
        print("\nData in the server: " + str(self.status))
        print("\nData in the web: " + door_status)
        assert (door_status == "Closed / Locked" and self.status == 2)


    @pytest.mark.usefixtures("chrome_driver_init")
    def test_click_on_the_open_the_door_button_once(self, driver):
        self.driver.get(self.URL)
        driver.implicitly_wait(5000)
        open_door_button = driver.find_element_by_xpath(self.open_door_button_xp)
        open_door_button.click()
        door_status = webdriver.Chrome.find_element_by_xpath(self.driver, self.door_status_xpath).text
        print("\nData in the server: " + str(self.status))
        print("\nData in the web: " + door_status)
        assert door_status == "Closed / Unlocked" and self.status == 1
        
        
    @pytest.mark.usefixtures("chrome_driver_init")
    def test_click_on_the_open_the_door_button_twice(self, driver):
        self.driver.get(self.URL)
        driver.implicitly_wait(5000)
        open_door_button = driver.find_element_by_xpath(self.open_door_button_xp)
        open_door_button.click()
        open_door_button.click()
        door_status = webdriver.Chrome.find_element_by_xpath(self.driver, self.door_status_xpath).text
        print("\nData in the server: " + str(self.status))
        print("\nData in the web: " + door_status)
        assert door_status == "Closed / Unlocked" and self.status == 1

    @pytest.mark.usefixtures("chrome_driver_init")
    def test_click_on_the_lock_the_door_button_once(self, driver):
        self.driver.get(self.URL)
        driver.implicitly_wait(5000)
        open_door_button = driver.find_element_by_xpath(self.lock_door_button_xp)
        open_door_button.click()
        door_status = webdriver.Chrome.find_element_by_xpath(self.driver, self.door_status_xpath).text
        print("\nData in the server: " + str(self.status))
        print("\nData in the web: " + door_status)
        assert door_status == "Closed / Unlocked" and self.status == 1

    @pytest.mark.usefixtures("chrome_driver_init")
    def test_click_on_the_lock_the_door_button_twice(self, driver):
        self.driver.get(self.URL)
        driver.implicitly_wait(5000)
        open_door_button = driver.find_element_by_xpath(self.lock_door_button_xp)
        open_door_button.click()
        open_door_button.click()
        door_status = webdriver.Chrome.find_element_by_xpath(self.driver, self.door_status_xpath).text
        print("\nData in the server: " + str(self.status))
        print("\nData in the web: " + door_status)
        assert door_status == "Closed / Unlocked" and self.status == 1
