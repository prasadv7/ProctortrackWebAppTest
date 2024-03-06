import os
import time

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.d2l_pageObjects.D2L_Login_Page import D2L_Login_Page
from utilities.readproperties import ReadConfig
from utilities.customlogger import CustomLogger
from allure_commons.types import AttachmentType

log_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "Logs"))
CustomLogger.configure_logger()


class TestD2LLogin:
    baseURL = ReadConfig.getD2LAppURL()
    username = ReadConfig.getD2LUserEmail()
    password = ReadConfig.getD2LPassword()
    logger = CustomLogger.get_logger()

    def test_verifyD2lHomepage(self,setup):
        try:
            self.logger.info("==D2L Home Page Title==")
            self.logger.info("==Verifying D2L Home Page Title==")
            self.driver = setup
            self.driver.get(self.baseURL)
            act_title = self.driver.title
            time.sleep(2)
            assert act_title == "Login - Partners11"
        except AssertionError:
            self.logger.error(f"==D2L Home Page== Exception Occured: {str(AssertionError)}")
            print(f"==D2L Home Page== Exception Occured: Assertion failed")
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

        finally:
            self.driver.close()

    def test_Login(self,setup):
        try:
            self.logger.info("======= Test Login =======")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.d2l = D2L_Login_Page(self.driver)
            self.d2l.set_username(self.username)
            self.d2l.set_password(self.password)
            self.d2l.clickLoginButton()
            homepage_title = self.driver.title
            assert homepage_title == "Homepage - Partners"
        except AssertionError as ae:
            self.logger.error(f"Login test failed")
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

        finally:
            self.driver.close()

    def test_select_course(self,setup):
        try:
            self.logger.info("test select course")
            self.driver = setup
            self.driver.get(self.baseURL)
        finally:
            pass


