from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCreatePage:
    def __init__(self, driver):
        self.driver = driver
        self.edit_btn_locator = (By.XPATH, "//*[@id='id_edit_menu']")
        self.edittest_btn_locator = (By.XPATH, "//*[@id='id_edit_test_details_menu']")
        self.createtest_btn_locator = (By.XPATH, "//*[@id='func-add-test']")
        self.test_name_locator = (By.XPATH, "//*[@id='id_name']")
        self.test_duration_locator = (By.XPATH, "//*[@id='id_duration']")
        self.test_attempts_locator = (By.XPATH, "//*[@id='id_attempts_allowed']")
        self.start_date_locator = (By.XPATH, "//*[@id='id_start_at_0']")
        self.start_time_locator = (By.XPATH, "//*[@id='id_start_at_1']")
        self.last_date_locator = (By.XPATH, "//*[@id='id_end_at_0']")
        self.expiry_time_locator = (By.XPATH, "//*[@id='id_end_at_1']")
        self.save_test_button_locator = (By.XPATH, "//*[@id='func-save-test']")
        self.upload_file_locator = (By.XPATH, "//*[@id='id_file']")
        self.upload_data_button_locator = (By.XPATH, "//*[@id='func-upload-question-data']")
        self.student_first_name_locator = (By.XPATH, "//*[@id='id_student_first_name']")
        self.student_last_name_locator = (By.XPATH, "//*[@id='id_student_last_name']")
        self.student_id_locator = (By.XPATH, "//*[@id='id_student_id']")
        self.student_email_locator = (By.XPATH, "//*[@id='id_student_email']")
        self.submit_reg_data_locator = (By.XPATH, "//*[@id='submit_reg_data']")
        self.publish_test_button_locator = (By.XPATH, "//button[contains(@data-test-id, 'your_dynamic_test_id')]")
        self.edit_student_button_locator = (By.XPATH, "//*[@id='cssmenu']/ul/li[3]/ul/li[3]/a")
        self.add_student_button_locator = (By.XPATH, "//*[@id='cssmenu']/ul/li[3]/ul/li[3]/ul/li[2]/a")
        self.edit_test_button_locator = (By.XPATH, "//*[@id='cssmenu']/ul/li[3]/ul/li[2]/a")
        self.bulk_question_import_locator = (By.XPATH, "//*[@id='cssmenu']/ul/li[3]/ul/li[2]/ul/li[2]/a")
        self.configure_test_button_locator = (By.XPATH, "//*[@id='cssmenu']/ul/li[3]/ul/li[1]/ul/li[3]/a")
        self.proctoring_level_button_locator = (By.XPATH, "//*[@id='content']/div/div/ul/li[1]/a")
        self.table_locator = (By.XPATH, '//*[@id="current-tests"]/div[1]/div/table')
        self.row_locator = (By.XPATH, 'tbody/tr')
        self.name_in_first_td_locator = (By.XPATH, 'td[1]/a')
        self.button_in_seventh_td_locator = (By.XPATH, 'td[7]//button')

    def create_test_btn(self):
        """Click on the 'Create Test' button."""
        wait = WebDriverWait(self.driver, 10)

        edit_btn = wait.until(EC.element_to_be_clickable(self.edit_btn_locator))
        edit_btn.click()

        edit_test_btn = wait.until(EC.element_to_be_clickable(self.edittest_btn_locator))
        edit_test_btn.click()

        create_test_btn = wait.until(EC.element_to_be_clickable(self.createtest_btn_locator))
        create_test_btn.click()

    def enter_test_details(self, test_name, test_duration, test_attempts):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.visibility_of_element_located(self.test_name_locator)).send_keys(test_name)
        wait.until(EC.visibility_of_element_located(self.test_duration_locator)).send_keys(test_duration)
        wait.until(EC.visibility_of_element_located(self.test_attempts_locator)).send_keys(test_attempts)

    def set_test_start_date(self, start_date, start_time):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.visibility_of_element_located(self.start_date_locator)).send_keys(start_date)
        wait.until(EC.visibility_of_element_located(self.start_time_locator)).send_keys(start_time)

    def set_test_end_date(self, end_date, expiry_time):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.visibility_of_element_located(self.last_date_locator)).send_keys(end_date)
        wait.until(EC.visibility_of_element_located(self.expiry_time_locator)).send_keys(expiry_time)

    def save_test(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable(self.save_test_button_locator)).click()

    def upload_question_data(self):
        wait = WebDriverWait(self.driver, 10)

        # wait.until(EC.visibility_of_element_located(self.upload_file_locator)).send_keys(file_path)
        # wait.until(EC.element_to_be_clickable(self.upload_data_button_locator)).click()
        wait.until(EC.element_to_be_clickable(self.save_test_button_locator)).click()

    def add_student(self):
        wait = WebDriverWait(self.driver, 10)
        edit_btn = wait.until(EC.element_to_be_clickable(self.edit_btn_locator))
        edit_btn.click()
        edit_student_btn = wait.until(EC.element_to_be_clickable(self.edit_student_button_locator))
        edit_student_btn.click()
        add_student_btn = wait.until(EC.element_to_be_clickable(self.add_student_button_locator))
        add_student_btn.click()

    def submit_student_details(self, first_name, last_name, student_id, student_email):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.visibility_of_element_located(self.student_first_name_locator)).send_keys(first_name)
        wait.until(EC.visibility_of_element_located(self.student_last_name_locator)).send_keys(last_name)
        wait.until(EC.visibility_of_element_located(self.student_id_locator)).send_keys(student_id)
        wait.until(EC.visibility_of_element_located(self.student_email_locator)).send_keys(student_email)
        wait.until(EC.element_to_be_clickable(self.submit_reg_data_locator)).click()

    def upload_questions(self):
        wait = WebDriverWait(self.driver, 10)
        edit_btn = wait.until(EC.element_to_be_clickable(self.edit_btn_locator))
        edit_btn.click()
        edit_test_question = wait.until(EC.element_to_be_clickable(self.edit_test_button_locator))
        edit_test_question.click()
        q_bulk_import = wait.until(EC.element_to_be_clickable(self.bulk_question_import_locator))
        q_bulk_import.click()

    def configure_exam(self):
        wait = WebDriverWait(self.driver, 10)
        edit_btn = wait.until(EC.element_to_be_clickable(self.edit_btn_locator))
        edit_btn.click()
        edit_test_btn = wait.until(EC.element_to_be_clickable(self.edittest_btn_locator))
        edit_test_btn.click()
        config_test_btn = wait.until(EC.element_to_be_clickable(self.configure_test_button_locator))
        config_test_btn.click()

    def set_levels(self):
        wait = WebDriverWait(self.driver, 10)
        proctoring_btn = wait.until(EC.element_to_be_clickable(self.proctoring_level_button_locator))
        proctoring_btn.click()

    def publish_test(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable(self.publish_test_button_locator)).click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def get_all_rows(self):
        """Get all rows in the table."""
        wait = WebDriverWait(self.driver, 10)
        table_locator = (By.XPATH, '//*[@id="current-tests"]/div[1]/div/table')
        table = wait.until(EC.presence_of_element_located(table_locator))
        rows = table.find_elements(By.XPATH, './tbody/tr')
        return rows
