from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_user_xpath = "//input[@id='id_username']"
    textbox_user_pass_xpath = "//input[@id='id_password']"
    btn_login_xpath = "//button[@id='log_in']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_user_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_user_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_user_pass_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_user_pass_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
