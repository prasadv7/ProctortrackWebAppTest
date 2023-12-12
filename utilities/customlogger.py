import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class CustomLogger:
    @staticmethod
    def configure_logger(log_dir="Logs", initial_info_message="Info Message"):
        log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", log_dir))
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = f"log_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
        log_path = os.path.join(log_dir, log_file)

        try:
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            file_handler = RotatingFileHandler(log_path, mode='a', maxBytes=10 * 1024 * 1024, backupCount=5)
            file_handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s %(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.info(initial_info_message)

            return logger
        except Exception as e:
            print("Exception while configuring logger:", e)
            return None

    @staticmethod
    def get_logger():
        return logging.getLogger()

    @staticmethod
    def capture_screenshot(driver, screenshot_name):
        try:
            current_dir = os.getcwd()
            screenshots_dir = os.path.abspath(os.path.join(current_dir, "Screenshots"))
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)
            screenshot_path = os.path.join(screenshots_dir, f"{screenshot_name}.png")
            driver.save_screenshot(screenshot_path)
            CustomLogger.get_logger().info(f"Screenshot captured: {screenshot_path}")
        except WebDriverException as e:
            CustomLogger.get_logger().warning(f"Failed to capture screenshot: {str(e)}")


class LoggingWebDriver(RemoteWebDriver, CustomLogger):
    def __init__(self, *args, **kwargs):
        super(LoggingWebDriver, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger()

    def find_element(self, by=By.ID, value=None):
        element = super(LoggingWebDriver, self).find_element(by, value)
        self.logger.info(f"Found element by {by}: {value}")
        return element

    def find_elements(self, by=By.ID, value=None):
        elements = super(LoggingWebDriver, self).find_elements(by, value)
        self.logger.info(f"Found elements by {by}: {value}")
        return elements

    def click(self, element):
        self.logger.info(f"Clicked element: {element}")
        super(LoggingWebDriver, self).click(element)
