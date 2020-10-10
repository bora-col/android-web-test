import yaml
import json
import os
from SmartDoorLock import __file__

"""
This class using for separate configuration variable and also fixed path combination for all computer. 
It means you don't need update your computer paths.
All configuration variables reading on "properties.yml" which is in the project folder.
"""


class Configuration:

    @staticmethod
    def read_config_file():
        root_dir = os.path.dirname(os.path.abspath(__file__))
        # print()
        # print("base_config.py -> read_config_file() -> root_dir = ", root_dir)
        # print()
        config_path = os.path.join(root_dir, 'properties.yaml')
         # config_path = os.path.join(root_dir, 'properties.json')
        with open(config_path) as file:
            configuration_paths = yaml.full_load(file)
             # configuration_paths = json.load(file)
            return configuration_paths

    @staticmethod
    def get_device_name():
        configuration_paths = Configuration.read_config_file()
        device_name = configuration_paths.get("deviceName")
        return str(device_name)

    @staticmethod
    def get_platform_name():
        configuration_paths = Configuration.read_config_file()
        platform_name = configuration_paths.get("platformName")
        return str(platform_name)

    @staticmethod
    def get_apk_path():
        configuration_paths = Configuration.read_config_file()
        apk_path = os.path.dirname(os.path.abspath(__file__)) + configuration_paths.get("apkPath")
        return str(apk_path)

    @staticmethod
    def get_app_package():
        configuration_paths = Configuration.read_config_file()
        app_package = configuration_paths.get("appPackage")
        return str(app_package)

    @staticmethod
    def get_app_wait_activity():
        configuration_paths = Configuration.read_config_file()
        app_wait_activity = configuration_paths.get("appWaitActivity")
        return str(app_wait_activity)

    @staticmethod
    def get_no_reset():
        configuration_paths = Configuration.read_config_file()
        no_reset = configuration_paths.get("noReset")
        return str(no_reset)

    @staticmethod
    def get_automation_name():
        configuration_paths = Configuration.read_config_file()
        automation_name = configuration_paths.get("automationName")
        return str(automation_name)

    @staticmethod
    def get_open_door_slider_xpath():
        configuration_paths = Configuration.read_config_file()
        open_door_slider_xpath = configuration_paths.get("OpenDoorSliderXpath")
        return open_door_slider_xpath

    @staticmethod
    def get_open_the_door_button_xpath():
        configuration_paths = Configuration.read_config_file()
        open_the_door_button_xpath = configuration_paths.get("OpenTheDoorButtonXpath")
        return open_the_door_button_xpath

    @staticmethod
    def get_chrome_driver():
        configuration_paths = Configuration.read_config_file()
        chrome_driver = os.path.dirname(os.path.abspath(__file__)) + configuration_paths.get("chromedriver")
        return chrome_driver

    @staticmethod
    def get_admin_panel_url():
        configuration_paths = Configuration.read_config_file()
        admin_panel_url = configuration_paths.get("AdminPanelUrl")
        return admin_panel_url

    @staticmethod
    def get_door_status_xpath():
        configuration_paths = Configuration.read_config_file()
        door_status_xpath = configuration_paths.get("DoorStatusXpath")
        return door_status_xpath

    @staticmethod
    def get_appium_driver():
        configuration_paths = Configuration.read_config_file()
        appium_driver = configuration_paths.get("appiumdriver")
        return appium_driver

    @staticmethod
    def get_base_url():
        configuration_paths = Configuration.read_config_file()
        base_url = configuration_paths.get("url")
        return str(base_url)

    @staticmethod
    def get_mobile_device_password():
        configuration_paths = Configuration.read_config_file()
        password = configuration_paths.get("password")
        return str(password)

    @staticmethod
    def get_socket_path():
        configuration_paths = Configuration.read_config_file()
        socket_path = configuration_paths.get("path")
        return str(socket_path)



    # eklenenler
    @staticmethod
    def get_lock_the_door_button_xpath():
        configuration_paths = Configuration.read_config_file()
        lock_the_door_button_xpath = configuration_paths.get("LockTheDoorButtonXpath")
        return lock_the_door_button_xpath

    @staticmethod
    def get_do_nothing_button_xpath():
        configuration_paths = Configuration.read_config_file()
        do_nothing_button_xpath = configuration_paths.get("DoNothingButtonXpath")
        return do_nothing_button_xpath

    @staticmethod
    def get_activate_alarm_button_xpath():
        configuration_paths = Configuration.read_config_file()
        activate_alarm_button_xpath = configuration_paths.get("ActivateAlarmButtonXpath")
        return activate_alarm_button_xpath

    @staticmethod
    def get_door_status_text_xpath():
        configuration_paths = Configuration.read_config_file()
        door_status_text_xpath = configuration_paths.get("DoorStatusTextXpath")
        return door_status_text_xpath

    @staticmethod
    def get_open_door_slider_area_xpath():
        configuration_paths = Configuration.read_config_file()
        open_door_slider_area_xpath = configuration_paths.get("OpenDoorSliderAreaXpath")
        return open_door_slider_area_xpath

    @staticmethod
    def get_popup_area_xpath():
        configuration_paths = Configuration.read_config_file()
        popup_area_xpath = configuration_paths.get("PopupAreaXpath")
        return popup_area_xpath


