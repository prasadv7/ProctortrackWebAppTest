import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://preproduction.verificient.com/")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys("prasadvidhate+inst@verificient.com")
driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys("Vidhaterajendra7@")
driver.find_element(By.XPATH, "//button[@id='log_in']").click()
time.sleep(4)

editbtn = driver.find_element(By.XPATH,"//*[@id='id_edit_menu']")
editbtn.click()
time.sleep(2)
edittestbtn = driver.find_element(By.XPATH,"//*[@id='cssmenu']/ul/li[3]/ul/li[3]/a")
edittestbtn.click()
time.sleep(2)
createtestbtn = driver.find_element(By.XPATH,"//*[@id='cssmenu']/ul/li[3]/ul/li[3]/ul/li[2]/a")
createtestbtn.click()
time.sleep(2)



















# # driver.find_element(By.XPATH, "//a[normalize-space()='Change Test']").click()
# # time.sleep(4)
#
# # driver.find_element(By.XPATH, "//*[@id='test_list']/div").click()
# #
# # search_input = driver.find_element(By.XPATH, "//div[@class='chosen-search']//input[@type='text']")
# # search_input.send_keys("L3")
# # time.sleep(4)
# #
# # search_results = driver.find_elements(By.XPATH, "//*[@id='test_list']/div/div/ul/li")
# #
# # if search_results:
# #     random_result = random.choice(search_results)
# #     selected_test_text = random_result.text
# #     random_result.click()
# #
# #     driver.find_element(By.XPATH, "//button[@id='update_test']").click()
# #
# #     current_url = driver.current_url
# #
# #     driver.get(current_url)
# #
# #
# #     wait = WebDriverWait(driver, 10)
# #
# #     element_xpath = "//div[@class='col-sm-12']//div[@style='float:left;']//span[@style='font-size:36px;']"
# #
# #     test_name_element = wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))
# #
# #
# #     test_name = test_name_element.text
# #
# #     if selected_test_text == test_name:
# #         print(f"Selected test text matches the div text. {test_name}")
# #     else:
# #         print("Selected test text does not match the div text.")
# #
# # driver.close()
# # driver.quit()
#
#
# from selenium import webdriver
# from selenium.webdriver.common.alert import Alert
# import time
#
# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome()
#
# # Open the URL with a JavaScript alert
# driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
#
# # Switch to the frame containing the alert
# driver.switch_to.frame("iframeResult")
#
# # Find the "Try it" button and click it
# try_it_button = driver.find_element("xpath", "//button[text()='Try it']")
# try_it_button.click()
#
# # Wait for the alert to appear (sleep is used here for simplicity, in practice, you might use WebDriverWait)
# time.sleep(2)
#
# # Switch to the alert and print its text
# alert = Alert(driver)
# print("Alert Text:", alert.text)
#
# # Accept the alert (click OK)
# alert.accept()
#
# # Close the browser
# driver.quit()
