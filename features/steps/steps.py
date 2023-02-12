import os
import sys

from appium import webdriver
from behave import given, when, then, step
from time import sleep
from pages.android import google_apps_page
import time

PAGE_NAVIGATION_TIMER = 3
IDLE_TIMER = 2


@given('the google photos app is launched')
def step_impl(context):
    try:
        context.google_apps_page.app_auto_back_up_switch()
        return
    except Exception as e:
        raise e
    finally:
        sleep(PAGE_NAVIGATION_TIMER)

@when("I upload photo to the app")
def step_impl(context):
    context.google_apps_page.upload_image()


@then("I verify the photo is uploaded")
def step_impl(context):
    assert context.google_apps_page.verify_photo_taken() == 1


@step("I verify the image name")
def step_impl(context):
    context.google_apps_page.check_details()
    time.sleep(3)
    image_name = context.google_apps_page.get_text_of_image()
    assert image_name == "test.png"


@when("I tap the photo in the app")
def step_impl(context):
    context.google_apps_page.tap_on_photo_taken()
    time.sleep(4)


@step("I launch the Gmail app")
def step_impl(context):
    context.google_apps_page.launch_gmail_app()


@when("I signin into gmail account")
def step_impl(context):
    context.google_apps_page.login_into_gmail()


@step("I send email attaching the photo uploaded earlier")
def step_impl(context):
    context.google_apps_page.compose_email("cs@headspin.io", "Appium Challenge email :Deepthi Gumpula")
