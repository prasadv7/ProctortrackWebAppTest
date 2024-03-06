from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class D2L_Login_Page:
    username_textbox_xpath = '//*[@id="userName"]'
    password_textbox_xpath = '//*[@id="password"]'
    btn_login_xpath = "//button[contains(@id, 'd2l_1_4_')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

    def set_username(self, username):
        username_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.username_textbox_xpath)))
        username_element.clear()
        username_element.send_keys(username)

    def set_password(self, password):
        password_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.password_textbox_xpath)))
        password_element.clear()
        password_element.send_keys(password)

    def clickLoginButton(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_login_xpath)))
        login_button.click()
