import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import sys
sys.path.append('/Users/user/Desktop/smartdoorlocktestautomation')
# for path in sys.path:
#     print(path)
from SmartDoorLock.Helper.parse_data import ParseData
import SmartDoorLock.Configuration.base_config as base_config





class TestEmbeddedMobile:
    open_door_button_xp = base_config.Configuration().get_open_the_door_button_xpath()
    lock_door_button_xp = base_config.Configuration().get_lock_the_door_button_xpath()
    do_nothing_button_xp = base_config.Configuration().get_do_nothing_button_xpath()
    open_door_slider_xp = base_config.Configuration().get_open_door_slider_xpath()
    activate_alarm_button_xp = base_config.Configuration().get_activate_alarm_button_xpath()
    popup_area_xp = base_config.Configuration().get_popup_area_xpath()
    data_json_path = "data_mobile_embedded.json"
    came_from_file_path = "Edge_Info/came_from.txt"
    my_came_from = None;


    # define desired capabilities of the mobile application
    @pytest.fixture(scope="function")
    def driver(self, request):
        # TODO (@alperen.bekci) this block will move under the base-mobile class with page-object model task.
        desired_cap = {
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

    def e_halfslide_slider(self,driver):
        driver.implicitly_wait(7000)
        open_door_slider = driver.find_element_by_xpath(self.open_door_slider_xp)
        print("\nIs the open the door slider displayed? \n" + str(open_door_slider.is_displayed()) + "\n")
        location = open_door_slider.location;
        x_prev = location["x"]
        y_prev = location["y"]
        print("Slider coordinates before sliding: ", "x:",x_prev, " y:",y_prev)
        driver.swipe(x_prev, y_prev, x_prev+350, y_prev, 2000);
        driver.implicitly_wait(2000)

    def e_click_slider(self,driver):
        driver.implicitly_wait(7000)
        open_door_slider = driver.find_element_by_xpath(self.open_door_slider_xp)
        print("\nIs the open the door slider displayed? \n" + str(open_door_slider.is_displayed()) + "\n")
        open_door_slider.click()

    def e_fullslide_slider(self,driver):
        driver.implicitly_wait(7000)
        open_door_slider = driver.find_element_by_xpath(self.open_door_slider_xp)
        print("\nIs the open the door slider displayed? \n" + str(open_door_slider.is_displayed()) + "\n")
        location = open_door_slider.location;
        x_prev = location["x"]
        y_prev = location["y"]
        print("Slider coordinates before sliding: ", "x:",x_prev, " y:",y_prev)
        driver.swipe(x_prev, y_prev, x_prev+850, y_prev, 2000);
        driver.implicitly_wait(2000)




    #VERTEXES
    def test_initial_state(self, driver):
        edge_to_call = getattr(globals()['TestEmbeddedMobile'](), self.my_came_from)
        edge_to_call(driver)
        open_door_slider = driver.find_element_by_xpath(self.open_door_slider_xp)
        location = open_door_slider.location;
        x = location["x"]
        assert x == 122

    def test_open_the_door(self, driver):
        edge_to_call = getattr(globals()['TestEmbeddedMobile'](), self.my_came_from)
        edge_to_call(driver)
        office_id, status, data = ParseData.parse_data(self.data_json_path)
        print("\nData:" + str(status))
        assert status == 0

    def test_lock_the_door(self, driver):
        edge_to_call = getattr(globals()['TestEmbeddedMobile'](), self.my_came_from)
        edge_to_call(driver)
        driver.implicitly_wait(5000)
        office_id, status, data = ParseData.parse_data(self.data_json_path)
        print("\nData:" + str(status))
        assert status == 2

    def test_slide_garden_door(self, driver):
        edge_to_call = getattr(globals()['TestEmbeddedMobile'](), self.my_came_from)
        edge_to_call(driver)
        open_door_slider = driver.find_element_by_xpath(self.open_door_slider_xp)
        location = open_door_slider.location;
        x_new = location["x"]
        y_new = location["y"] 
        print("Slider coordinates after sliding: ", "x:",x_new, " y:",y_new)
        assert x_new == 869

    def test_unlock_the_door(self, driver):
        edge_to_call = getattr(globals()['TestEmbeddedMobile'](), self.my_came_from)
        edge_to_call(driver)
        office_id, status, data = ParseData.parse_data(self.data_json_path)
        print("\nData:" + str(status))
        assert status == 1



































