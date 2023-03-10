import os
import six
import sys
import time
import unittest

from appium import webdriver
from behave.tag_matcher import ActiveTagMatcher, setup_active_tag_values
#from appium import Saucelabs
#from appium import SauceTestCase
#from appium import on_platforms
#from sauceclient import SauceClient

CWD = os.getcwd()
SCREEN_SHOTS_PATH = CWD + "/reports/screenshots/"

__driver_configs = {}

def driver_setup(host, port, appium_version, platform_name,platform_version,device_name,app_activity,app_uri,automation_name,app_package):
    __driver_configs['host'] = host
    __driver_configs['port'] = port
    __driver_configs['appium_version'] = appium_version
    __driver_configs['platform_name'] = platform_name
    __driver_configs['platform_version'] = platform_version
    __driver_configs['device_name'] = device_name
    __driver_configs['app_activity'] = app_activity
    __driver_configs['app_uri'] = app_uri
    __driver_configs['automation_name'] = automation_name
    __driver_configs['app_package'] = app_package

def start_driver(context):
    try:
        context.driver = webdriver.Remote(
        command_executor='http://%s:%s/wd/hub' % (__driver_configs.get('host'),__driver_configs.get('port')),
        desired_capabilities={
            'platformName': __driver_configs.get('platform_name'),
            'platformVersion': __driver_configs.get('platform_version'),
            'appPackage': __driver_configs.get('app_package'),
            'appActivity': __driver_configs.get('app_activity'),
            'deviceName': __driver_configs.get('device_name'),
            'app': __driver_configs.get('app_uri'),
            'automationName': __driver_configs.get('automation_name')
        })

        context.platform = __driver_configs.get('platform_name')
        if  context.platform == 'Android':
            from pages.android.google_apps_page import GoogleAppsPage
        ## TODO :IOS
        # elif context.platform == 'iOS':
        #from pages.ios.google_apps_page import GoogleAppsPage
        else:
            raise RuntimeError('Unrecognized platform: {}'.format(platform))
        context.google_apps_page = GoogleAppsPage(context.driver)
    except Exception as e:
        raise e

def take_screenshot(context, filename):
    # ts = time.time()
    # st = time.ctime(ts)
    # screenshot_file =  SCREEN_SHOTS_PATH + filename + st + ".PNG"
    
    context.driver.save_screenshot(filename)

def cleanup_driver(context):
    context.driver.quit()

def teardown_driver(context):
    context.driver.quit()
