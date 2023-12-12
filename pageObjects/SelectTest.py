import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SelectTest:
    change_test_link_xpath = "//a[normalize-space()='Change Test']"
    test_list_xpath = "//*[@id='test_list']/div"
    search_input_xpath = "//div[@class='chosen-search']//input[@type='text']"
    search_results_xpath = "//*[@id='test_list']/div/div/ul/li"
    update_test_button_xpath = "//button[@id='update_test']"
    test_name_xpath = "//div[@class='col-sm-12']//div[@style='float:left;']//span[@style='font-size:36px;']"

    def __init__(self, driver):
        self.driver = driver

    def change_test(self):
        self.driver.find_element(By.XPATH, self.change_test_link_xpath).click()

    def select_test(self, test_name):
        wait = WebDriverWait(self.driver, 10)

        # Wait for the test list element to be present
        test_list_element = wait.until(EC.presence_of_element_located((By.XPATH, self.test_list_xpath)))
        test_list_element.click()

        search_input = self.driver.find_element(By.XPATH, self.search_input_xpath)
        search_input.clear()
        search_input.send_keys(test_name)

        # Explicit wait for search results
        search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.search_results_xpath)))

        if search_results:
            random_result = random.choice(search_results)
            selected_test_text = random_result.text
            random_result.click()

            # Explicit wait for the update button
            update_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.update_test_button_xpath)))
            update_button.click()

            # Explicit wait for the test name element
            test_name_element = wait.until(EC.presence_of_element_located((By.XPATH, self.test_name_xpath)))
            actual_test_name = test_name_element.text

            return selected_test_text == actual_test_name
        else:
            return False