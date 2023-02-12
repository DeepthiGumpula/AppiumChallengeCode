#==========================
#  Basic page
#==========================
import logging
import os
import sys
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
import utils.CustomLogger as cl
import time
ELEMENT_DISPLAY_TIMER = 10
ENTER_KEY_EVENT       = 66

class BasePage:
    log = cl.customLogger()
    def __init__(self, driver):
        self.driver    = driver
        self.elements  = {}
        self.elements_name = {}
        self._user     = None
        self._logger   = None
        self.action    = TouchAction(self.driver)
        self._screenshot_path = "../reports/screenshots/"
        self.device_width  = self.driver.get_window_size()['width']
        self.device_height = self.driver.get_window_size()['height']

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def send_keys(self, value, *loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e

    def is_element_found(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.visibility_of_element_located(loc))
            return True
        except TimeoutError:
            return False

    def is_tapable_element_found(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.element_to_be_clickable(loc))
            return True
        except TimeoutError:
            return False

    #Andriod enter key
    def send_enter_key(self):
        try:
            self.driver.keyevent(ENTER_KEY_EVENT)
        except Exception as e:
            raise e

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def waitForElement(self, *loc):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        element = wait.until(lambda x: x.find_element(*loc))
        return element

    def get_count_of_elements(self, *loc):
        self.waitForElement(*loc)
        return len(self.driver.find_elements(*loc))


    def change_orientation(self, position):
        self.driver.orientation = position

    def upload_image_file(self):
        path = os.path.abspath(os.path.dirname(__file__))
        img = os.path.join(path, 'test.png')
        ANDROID_PHOTO_PATH = "/mnt/sdcard/Pictures"
        remote_path = f"{ANDROID_PHOTO_PATH}/{os.path.basename(img)}"
        self.log.info("Android photo is uploaded to remote path" + remote_path)
        self.driver.push_file(remote_path, source_path=r'./test.png')
        self.log.info("Photo is pushed to Android device via push file Appium command")
        time.sleep(20)

    def start_activity(self):
        self.driver.start_activity("com.google.android.gm", "com.google.android.gm.GmailActivity");
        time.sleep(10)
