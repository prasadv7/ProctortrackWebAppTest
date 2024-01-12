import os
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customlogger import CustomLogger
from allure_commons.types import AttachmentType

log_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "Logs"))
CustomLogger.configure_logger()


class Test_001_Login:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = CustomLogger.get_logger()

    def test_verifyHomePage(self, setup):
        try:
            self.logger.info("======= Test Home Page Title ========")
            self.logger.info("======= Verifying Home Page Title ========")
            self.driver = setup
            self.driver.get(self.baseURL)
            act_title = self.driver.title

            if act_title == "Login11":
                self.logger.info("Home page title is correct.")
                assert True
            else:
                self.logger.error("Home page title is incorrect. Test is failed")
                # screenshot_name = "test_HomePage-title111.png"
                # CustomLogger.capture_screenshot(self.driver, screenshot_name)

                # Get the full path to the screenshot
                allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
                assert False
        except Exception as e:
            self.logger.error(f"Exception occurred: {str(e)}")
            raise
        finally:
            self.driver.close()

    @pytest.mark.sanity
    def test_login(self, setup):
        try:
            self.logger.info("======= Test Login =======")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp = Login(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "// *[ @ id = 'current-tests'] / div[1] / div / table / tbody")))

            self.logger.info("Login test completed.")
        except Exception as e:
            self.logger.error(f"Exception occurred: {str(e)}")
            # screenshot_name = "test_login_failure.png"
            # CustomLogger.capture_screenshot(self.driver, name="Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

            assert False
        finally:
            self.driver.close()
