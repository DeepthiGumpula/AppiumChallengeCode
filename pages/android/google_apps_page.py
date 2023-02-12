import logging
import os
from selenium.webdriver.common.by import By
from utils.base_page import BasePage
import time

logger = logging.getLogger('behaving')


class GoogleAppsPage(BasePage):
    # Uploading Photos
    back_up_switch_loc = (By.ID, "com.google.android.apps.photos:id/auto_backup_switch")
    back_up_title = (By.ID, "com.google.android.apps.photos:id/auto_backup_title_container")
    touch_outside_loc = (By.ID, "com.google.android.apps.photos:id/touch_outside")
    keep_off_loc = (By.XPATH, "//*[@text='Keep off']")
    photo_taken_loc = (By.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'Photo taken')]")
    details_icon = (By.XPATH, "//android.widget.ImageView[@content-desc='Info']")
    label_text = (By.ID, "com.google.android.apps.photos:id/label")
    image_text = (By.ID, "com.google.android.apps.photos:id/label")

    # Gmail page
    skip_text = (By.XPATH, "//*[@text='SKIP']")
    setup_address = (By.ID, "com.google.android.gm:id/setup_addresses_add_another")
    google_text_loc = (By.XPATH, "//*[@text='Google']")
    sign_in_title_text = (By.XPATH, "//*[@text='Sign in']")
    field_value = (By.CLASS_NAME, "android.widget.EditText")
    next = (By.XPATH, "//*[@text='Next']")
    agree_text_button = (By.XPATH, "//*[@text='I agree']")
    switch_toggle = (By.ID, "com.google.android.gms:id/sud_items_switch")
    more_button = (By.XPATH, "//*[@text='MORE']")
    accept_button = (By.XPATH, "//*[@text='ACCEPT']")
    done_button = (By.ID, "com.google.android.gm:id/action_done")
    compose_button = (By.ID, "com.google.android.gm:id/compose_button")
    add_another_email = (By.ID, "com.google.android.gm:id/setup_addresses_add_another")
    account_display_name = (By.ID, "com.google.android.gm:id/account_display_name")
    image_view = (By.ID, "com.google.android.gm:id/illustration_image_view")

    # Compose Email locators
    add_attchment = (By.ID, "com.google.android.gm:id/add_attachment")
    att_title = (By.ID, "com.google.android.gm:id/title")
    preview_of_image = (By.XPATH, "//android.widget.ImageView[@content-desc='Preview of test.png']")
    from_name_acc_name = (By.ID, "com.google.android.gm:id/from_account_name")
    to_acc_name = (By.ID, "com.google.android.gm:id/to")
    subject_of_email = (By.ID, "com.google.android.gm:id/subject")
    send_icon = (By.ID, "com.google.android.gm:id/send")
    sent_msg_id = (By.ID, "com.google.android.gm:id/description_text")

    # Attaching google photo locators
    apps_view = (By.ID, "com.android.documentsui:id/apps_row")
    select_photo = (By.XPATH, "//*[@text='Select photos']")
    photos_text = (By.XPATH, "//*[@text='Photos']")
    pictures_text = (By.XPATH, "//*[@text='Pictures']")
    done = (By.ID, "com.google.android.apps.photos:id/done_button")

    def app_auto_back_up_switch(self):
        self.waitForElement(*self.back_up_title)
        self.click_app_auto_back_up_switch()
        self.touch_outside_back_up()
        self.keep_off()

    def touch_outside_back_up(self):
        self.waitForElement(*self.touch_outside_loc)
        self.find_element(*self.touch_outside_loc).click()

    def keep_off(self):
        self.waitForElement(*self.keep_off_loc)
        self.find_element(*self.keep_off_loc).click()

    def click_app_auto_back_up_switch(self):
        self.find_element(*self.back_up_switch_loc).click()

    def upload_image(self):
        self.upload_image_file()

    def verify_photo_taken(self):
        return self.get_count_of_elements(*self.photo_taken_loc)

    def tap_on_photo_taken(self):
        self.find_element(*self.photo_taken_loc).click()

    def check_details(self):
        self.change_orientation("LANDSCAPE")
        time.sleep(5)
        self.find_element(*self.details_icon).click()

    def get_text_of_image(self):
        get_text = self.find_element(By.ID, "com.google.android.apps.photos:id/label").text
        image_text = os.path.split(get_text)
        return image_text[1]

    def launch_gmail_app(self):
        self.change_orientation("PORTRAIT")
        time.sleep(4)
        self.start_activity()
        time.sleep(10)
        if self.find_element(*self.skip_text):
            self.find_element(*self.skip_text).click()

        self.waitForElement(*self.setup_address)
        self.find_element(*self.setup_address).click()
        self.waitForElement(*self.google_text_loc)
        self.find_element(*self.google_text_loc).click()

    def login_into_gmail(self):
        self.waitForElement(*self.sign_in_title_text)
        self.find_element(*self.field_value).send_keys("deepthigumpula16@gmail.com")
        time.sleep(6)
        self.waitForElement(*self.next)
        self.find_element(*self.next).click()
        time.sleep(6)
        self.find_element(*self.field_value).send_keys("Welcome@2626")
        self.find_element(*self.next).click()
        self.waitForElement(*self.agree_text_button)
        self.find_element(*self.agree_text_button).click()
        self.waitForElement(*self.accept_button)
        self.find_element(*self.accept_button).click()
        self.waitForElement(*self.add_another_email)
        self.waitForElement(*self.account_display_name)
        self.waitForElement(*self.done_button)
        self.find_element(*self.done_button).click()

    def compose_email(self, email_id, subject):
        self.waitForElement(By.ID, "com.google.android.gm:id/compose_button")

        # After logging into email
        write_btn = self.find_element(*self.compose_button)
        write_btn.click()
        time.sleep(6)
        self.waitForElement(*self.from_name_acc_name)

        # Attaching photo to email
        self.add_an_attachment_to_email()
        self.send_email_with_attachment(email_id, subject)

    def send_email_with_attachment(self, email_id, subject):
        self.waitForElement(*self.preview_of_image)
        self.find_element(*self.from_name_acc_name).click()
        self.find_element(*self.to_acc_name).send_keys(email_id)
        self.find_element(*self.subject_of_email).send_keys(subject)
        self.find_element(*self.send_icon).click()
        self.verify_email_sent_notification()

    def verify_email_sent_notification(self):
        self.waitForElement(*self.sent_msg_id)
        time.sleep(5)

    def add_an_attachment_to_email(self):
        self.find_element(*self.add_attchment).click()
        self.waitForElement(*self.att_title)
        self.find_element(*self.att_title).click()
        self.waitForElement(*self.apps_view)
        self.find_element(*self.photos_text).click()
        self.find_element(*self.select_photo)
        self.find_element(*self.pictures_text).click()
        self.waitForElement(By.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'Photo taken')]")
        self.find_element(By.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'Photo taken')]").click()
        time.sleep(4)
        self.find_element(*self.done).click()
        time.sleep(10)
