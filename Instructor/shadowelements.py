import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://partners.brightspace.com/")
username = '//*[@id="userName"]'
password = '//*[@id="password"]'
login_btn = "//button[contains(@id, 'd2l_1_4_')]"

driver.find_element(By.XPATH, username).send_keys('Prasad1.Vidhate')
driver.find_element(By.XPATH, password).send_keys('Prasad@123')
driver.find_element(By.XPATH, login_btn).click()

css_selector_for_host1 = "#d2l_1_10_352"
css_selector_for_host2 = "d2l-my-courses-container"
css_selector_for_host3 = "d2l-my-courses-content"
css_selector_for_host4 = "d2l-my-courses-card-grid"
css_selector_for_host5 = (
    "d2l-enrollment-card[href='https://41b632b6-ff74-4288-b3f1-7ffb6eb14bb4.enrollments.api"
    ".brightspace.com/enrolled-user/uBgbNVu_Pg72gwOJ-1AF7qNPZzfAGq3fBjm4fdgXiJ4/enrollment"
    "?localeId=1']"
)
css_selector_for_host6 = "d2l-card[text='Verificient Technologies Course 2, VerificientCourse2']"

# Execute JavaScript to navigate through nested Shadow DOMs
script = """
    var shadow0 = document.querySelector(arguments[0]).shadowRoot;
    var shadow1 = shadow0.querySelector(arguments[1]).shadowRoot;
    var shadow2 = shadow1.querySelector(arguments[2]).shadowRoot;
    var shadow3 = shadow2.querySelector(arguments[3]).shadowRoot;
    var shadow4 = shadow3.querySelector(arguments[4]).shadowRoot;
    var shadow5 = shadow4.querySelector(arguments[5]).shadowRoot;
    var elementToClick = shadow5.querySelector('a[href=\'/d2l/home/7745\']');
    elementToClick.click();
"""

# Wait for some time to ensure the page is loaded
time.sleep(10)

# Use execute_script to interact with the desired element inside the last Shadow DOM
driver.execute_script(script, css_selector_for_host1, css_selector_for_host2, css_selector_for_host3,
                      css_selector_for_host4, css_selector_for_host5, css_selector_for_host6)

# Close the browser
driver.quit()
