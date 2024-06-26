from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


class TestSingleReview:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_all_rows(self):
        table = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="current-tests"]/div[1]/div/table')))
        rows = table.find_elements(By.XPATH, 'tbody/tr')
        return rows

    def get_row_by_index(self, index):
        rows = self.get_all_rows()
        if 0 <= index < len(rows):
            return rows[index]
        return None

    def click_next_button(self):
        next_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="current-tests"]/div[2]/div[2]/div/span/button[3]')))
        next_button.click()

    def click_name_in_row(self, name):
        try:
            row_xpath = f'//a[text()="{name}"]/ancestor::tr'
            row = self.wait.until(EC.visibility_of_element_located((By.XPATH, row_xpath)))
            a_tag = row.find_element(By.XPATH, 'td[1]/a')
            a_tag.click()
            return True
        except StaleElementReferenceException:
            print(f"StaleElementReferenceException occurred while clicking on name '{name}'. Retrying...")
            return False
        except Exception as e:
            print(f"Error clicking on name '{name}': {e}")
            return False

    def no_candidate_msg(self):
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                self.driver.refresh()
                no_candidates_found_msg = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH,
                                                      '//*[@id="content"]/div[3]/div/table/tbody/tr/td/div/div[2]/translate/span')))
                dropdown_btn = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="content"]/div[3]/div/table/thead/tr/td/div[1]/button')))

                msg = no_candidates_found_msg.text
                print(msg)
                if no_candidates_found_msg.is_displayed():
                    dropdown_btn.click()
                    select_all_sessions_btn = self.wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, '//*[@id="content"]/div[3]/div/table/thead/tr/td/div[1]/ul/li[1]/a')))
                    select_all_sessions_btn.click()
                break
            except StaleElementReferenceException:
                retry_count += 1
                print(f"StaleElementReferenceException occurred. Retrying ({retry_count}/{max_retries}).")
