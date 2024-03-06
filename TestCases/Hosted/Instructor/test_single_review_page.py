import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import Login
from pageObjects.TestCreatePage import TestCreatePage
from pageObjects.SingleReview import TestSingleReview
from utilities.readproperties import ReadConfig
from utilities.customlogger import CustomLogger
import allure
import pytest
from allure_commons.types import AttachmentType


class TestSingleReviewPage():
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = CustomLogger.configure_logger()

    # Class-level variable to store the URL
    opened_url = None

    # @pytest.mark.xfail(raises=AssertionError)
    def test_single_review_test_url(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        wait = WebDriverWait(self.driver, 10)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        review_page = TestSingleReview(self.driver)
        wait = WebDriverWait(self.driver, 10)
        name_to_search = "Automation L3"
        non_empty_row_counter = 0

        while True:
            rows = review_page.get_all_rows()

            for row in rows:
                try:
                    # Refresh the row element on each iteration
                    row = review_page.get_row_by_index(rows.index(row) + 1)
                    if row.find_element(By.XPATH, 'td[1]').text.strip():
                        non_empty_row_counter += 1
                        a_tag = row.find_element(By.XPATH, 'td[1]/a')
                        a_tag_text = a_tag.text
                        if a_tag_text == name_to_search:
                            if review_page.click_name_in_row(name_to_search):
                                if review_page.no_candidate_msg():
                                    # Store the URL in the class-level variable
                                    TestSingleReviewPage.opened_url = self.driver.current_url
                                    time.sleep(3)
                                    self.driver.quit()
                                    return
                except Exception as e:
                    pass

            # If the name is not found in any row, take the last page's screenshot and assert False
            allure.attach(self.driver.get_screenshot_as_png(), name='name_not_found.png',
                          attachment_type=allure.attachment_type.PNG)

            try:
                review_page.click_next_button()
                # Take a screenshot before clicking on the next button
                allure.attach(self.driver.get_screenshot_as_png(),
                              name=f'before_next_button_{non_empty_row_counter}.png',
                              attachment_type=allure.attachment_type.PNG)
            except:
                # If the next button is not clickable, take a screenshot
                allure.attach(self.driver.get_screenshot_as_png(), name='last_page_before_exit.png',
                              attachment_type=allure.attachment_type.PNG)
                assert False

    def test_select_session(self, setup):
        opened_url = TestSingleReviewPage.opened_url
        if opened_url is not None:
            self.driver = setup
            self.driver.get(self.baseURL)
            wait = WebDriverWait(self.driver, 10)

            self.lp = Login(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            review_page = TestSingleReview(self.driver)
            time.sleep(3)
            self.driver.get(opened_url)
            time.sleep(3)



            self.driver.quit()
        else:
            # Handle the case where the first test method failed
            pytest.skip("Skipping test_select_session as the previous method failed.")
