import re
import time
from datetime import datetime, timedelta
import datetime
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import Login
from pageObjects.TestCreatePage import TestCreatePage
from utilities.readproperties import ReadConfig
from utilities.customlogger import CustomLogger
from faker import Faker


class Test_EditButton:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = CustomLogger.configure_logger()
    fake = Faker()

    def test_CreateTest(self, setup):  # Fix the method name here
        self.driver = setup
        self.driver.get(self.baseURL)
        wait = WebDriverWait(self.driver, 10)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        test_page = TestCreatePage(self.driver)
        test_page.create_test_btn()

        # Generate random test data
        test_name = self.fake.word()
        test_duration = str(self.fake.random_int(min=1, max=180))
        test_attempts = str(self.fake.random_int(min=1, max=5))

        test_page.enter_test_details(test_name, test_duration, test_attempts)

        current_date = datetime.datetime.now()
        exam_start_time = current_date.strftime('%H:%M:%S')
        exam_start_date = current_date.strftime('%d-%m-%Y')
        exam_last_date = current_date + datetime.timedelta(days=30)
        expiry_time = datetime.datetime(exam_last_date.year, exam_last_date.month, exam_last_date.day, 23, 59,
                                        59).strftime(
            '%H:%M:%S')

        test_page.set_test_start_date(exam_start_date, exam_start_time)
        test_page.set_test_end_date(exam_last_date.strftime('%d-%m-%Y'), expiry_time)

        test_page.save_test()

        test_page.upload_question_data()
        test_name_element = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='col-sm-12']//div[@style='float:left;']//span[@style='font-size:36px;']")))
        actual_test_name = test_name_element.text
        # Generate random student data

        if actual_test_name == test_name:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_AddStudent(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        wait = WebDriverWait(self.driver, 10)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        test_page = TestCreatePage(self.driver)
        test_page.add_student()
        stud_name = self.fake.first_name()
        stud_last_name = self.fake.last_name()
        stud_password = self.fake.password(length=8)
        stud_email = self.fake.email()

        test_page.submit_student_details(stud_name, stud_last_name, stud_password, stud_email)
        stud_email_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[2]/div/p[2]")))
        student_email = stud_email_element.text
        cleaned_student_email = student_email.replace("Email:", "").strip()
        self.logger.info(f"Student Email: {cleaned_student_email}")
        if stud_email == cleaned_student_email:

            assert True
        else:
            assert False
        # Close the browser
        self.driver.quit()

    def test_upload_question(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        wait = WebDriverWait(self.driver, 10)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        test_page = TestCreatePage(self.driver)
        test_page.upload_questions()
        csv_path = os.path.abspath("CSV/sample-csv.csv")
        upload_question_csv = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='id_file']")))
        upload_question_csv.send_keys(csv_path)
        upload_data_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='func-upload-question-data']")))
        upload_data_btn.click()
        test_page.save_test()
        self.driver.quit()

    def test_configure(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        wait = WebDriverWait(self.driver, 10)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        test_page = TestCreatePage(self.driver)
        test_page.configure_exam()
        test_page.set_levels()

        level_to_click = "4"  # Give the test level input to select the test level from L1 to L4 (in capital)

        level_xpath_mapping = {
            "1": "//*[@id='according_identity_conf']/div[6]/div/div[2]/div[1]/div/div[2]/div",
            "2": "//*[@id='according_identity_conf']/div[5]/div/div[2]/div[1]/div/div[2]/div/div",
            "3": "//*[@id='according_identity_conf']/div[4]/div/div[2]/div[1]/div/div[2]/div/div",
            "4": "//*[@id='according_identity_conf']/div[3]/div/div[2]/div[1]/div/div[2]/div/div",
            "5": "//*[@id='according_identity_conf']/div[2]/div/div[2]/div[2]/div/div[2]/div/div"
        }

        # Check if the user input corresponds to a valid level
        if level_to_click in level_xpath_mapping:
            # Get the XPath for the selected level
            xpath = level_xpath_mapping[level_to_click]

            # Find the input element using the provided XPath
            switch_element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

            # Check if the switch is off before turning it on
            if not switch_element.is_selected():
                switch_element.click()
        else:
            print("Invalid level input")

        self.driver.refresh()
        time.sleep(2)
        proc_level_element = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[8]/div/div[2]/div/div/div[1]/div/div[2]/h3")))
        proc_level_text = proc_level_element.get_attribute("innerText")

        # Extract the "Proctoring Level" part
        proctoring_level_part = proc_level_text.split(":")[0].strip()

        # Use a regular expression to extract the dynamic number part
        dynamic_number_match = re.search(r'\d+', proc_level_text)
        dynamic_number_part = dynamic_number_match.group() if dynamic_number_match else None

        self.logger.info(f"Proctoring Level Part: {proctoring_level_part}")
        self.logger.info(f"Dynamic Number Part: {dynamic_number_part}")
        if level_to_click == dynamic_number_part:
            self.logger.info("Exam Level changed Successfully")

        else:
            self.logger.info("Exam level not changed Successfully")
            assert False




        self.driver.quit()

