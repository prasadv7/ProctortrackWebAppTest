import random
import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://preproduction.verificient.com/")

# Wait for the username input field to be present
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_username']")))
username_input.send_keys("prasadvidhate+inst@verificient.com")

# Wait for the password input field to be present
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_password']")))
password_input.send_keys("Vidhaterajendra7@")

# Wait for the login button to be clickable
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='log_in']")))
login_button.click()

# # Wait for the edit menu button to be displayed
# edit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='id_edit_menu']")))
#
# current_testsbtn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[7]/div[3]/div/div[3]/ul/li[1]/a")))
# current_testsbtn.click()
# time.sleep(2)
# #########################
# driver.execute_script("window.open('', '_blank');")
#
# # Switch to the new tab
# driver.switch_to.window(driver.window_handles[1])
#
# # Open the desired URL in the new tab
# desired_url = 'https://preproduction.verificient.com/614e06160524313a1a3f4a17/proctoring/review/session/e5067c9e1c0849e3b49175a93751a291/new/'
# driver.get(desired_url)
#
# # Add a delay to let the page load
# time.sleep(2)
# wait = WebDriverWait(driver, 10)
#
# # XPath of the video tab button
# # video_tab_button_xpath = '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/ul/li[1]/a'
# #
# # # Wait until the video tab button is present
# # video_tab_button = wait.until(EC.presence_of_element_located((By.XPATH, video_tab_button_xpath)))
#
# # Click on the video tab button to activate it
# # video_tab_button.click()
#
# # Wait for the tab content to load (adjust the XPath as needed)
# tab_content_xpath = '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div/div'
# tab_content = wait.until(EC.presence_of_element_located((By.XPATH, tab_content_xpath)))
#
# # Check if the video element is present in the tab content
# video_xpath = '/videogular/vg-media/'
# time.sleep(2)
# video_play = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div/div/videogular/vg-overlay-play/div/div")
# video_play.click()
# video_content = wait.until(EC.presence_of_element_located((By.XPATH, video_xpath)))
#
# try:
#     video = tab_content.find_element(By.XPATH, video_xpath)
#     print("Video found in the first tab.")
# except NoSuchElementException:
#     print("No video found in the first tab.")
# Assuming 'driver' is your Selenium WebDriver instance
# ################################################
# # Assuming 'driver' is your Selenium WebDriver instance
wait = WebDriverWait(driver, 10)
time.sleep(2)
new_url = 'https://preproduction.verificient.com/614e06160524313a1a3f4a17/proctoring/student-list/test/760c7b7b6e804a66ad672e205de26050/new/'
time.sleep(2)
driver.get(new_url)
table_xpath = '//*[@id="content"]/div[3]/div/table'
time.sleep(2)
drpdwn_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div[3]/div/table/thead/tr/td/div[1]/button")))
drpdwn_btn.click()
time.sleep(1)
all_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div[3]/div/table/thead/tr/td/div[1]/ul/li[1]/a")))
# XPath of the table
all_btn.click()
time.sleep(5)

# Wait until the table is present
table = wait.until(EC.presence_of_element_located((By.XPATH, table_xpath)))

# Find all rows within the table
rows = table.find_elements(By.XPATH, './tbody/tr')

# Filter alternate rows with the <a> tag in the 4th column
filtered_rows = [row for i, row in enumerate(rows) if i % 2 == 0 and row.find_elements(By.XPATH, './td[4]/a')]

# Check if there are filtered rows
if filtered_rows:
    # Choose a random row index
    random_row_index = random.randint(0, len(filtered_rows) - 1)

    # Print the HTML of the randomly selected row (for debugging)
    random_row = filtered_rows[random_row_index]
    print("Randomly selected row HTML:", random_row.get_attribute("outerHTML"))

    # Find the <a> element in the randomly selected row
    a_element = random_row.find_element(By.XPATH, './td[4]/a')

    # Click on the <a> element
    a_element.click()
    time.sleep(5)
else:
    print("No alternate rows with <a> tag in the 4th column found in the table.")
#
# ##########################################
# table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="current-tests"]/div[1]/div/table')))
#
# # Find all rows (tr) in the table
# rows = table.find_elements(By.XPATH, 'tbody/tr')
#
# # Print the number of rows
# print(f"Number of Rows: {len(rows)}")
#
# name_to_search = "Automation L3"
#
# # Replace the next_button_xpath with the actual XPath of the next button
# next_button_xpath = '//*[@id="current-tests"]/div[2]/div[2]/div/span/button[3]'
#
# # Initialize a counter for non-empty rows
# non_empty_row_counter = 0
#
# while True:
#     # Wait for the table to be present
#     table = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, '//*[@id="current-tests"]/div[1]/div/table')))
#
#     # Find all rows (tr) in the table
#     rows = table.find_elements(By.XPATH, 'tbody/tr')
#
#     # Iterate through each row and check if the name is present
#     for row in rows:
#         # Check if the text in the first <td> is not empty
#         if row.find_element(By.XPATH, 'td[1]').text.strip():
#             try:
#                 # Increment the counter for non-empty rows
#                 non_empty_row_counter += 1
#
#                 # Find the first <a> tag in the row
#                 a_tag = row.find_element(By.XPATH, 'td[1]/a')
#
#                 # Get the text from the <a> tag
#                 a_tag_text = a_tag.text
#
#                 # Check if the name matches
#                 if a_tag_text == name_to_search:
#                     print(f"Name '{name_to_search}' found in row {non_empty_row_counter}")
#
#                     # Wait until the name is clickable
#                     wait = WebDriverWait(driver, 10)
#                     clickable_a_tag = wait.until(
#                         EC.element_to_be_clickable((By.XPATH, f'//a[text()="{name_to_search}"]')))
#
#                     # Click on the element
#                     clickable_a_tag.click()
#
#                     # Now you can continue with further actions after the click
#                     time.sleep(3)
#                     driver.quit()
#                     exit()  # Exit the script if the name is found
#             except Exception as e:
#                 print(f"Error processing non-empty row {non_empty_row_counter}: {e}")
#
#     # Check if the next button is enabled
#     try:
#         next_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
#     except:
#         print(f"Name '{name_to_search}' not found in the table.")
#         driver.quit()
#         exit()  # Exit the script if the next button is not clickable
#
#     # Click on the next button
#     next_button.click()
    ###################################################################
# # Check if there are any rows
# if rows:
#     # Choose a random row index
#     random_row_index = random.randint(0, len(rows) - 1)
#
#     # Find the link within the first td element in the randomly selected row
#     random_row = rows[random_row_index]
#     # link_in_first_td = random_row.find_element(By.XPATH, 'td[1]//a')
#     #
#     # # Click on the link within the first td element
#     # link_in_first_td.click()
#     button_in_seventh_td = random_row.find_element(By.XPATH, 'td[7]//button')
#
#     # Click on the button
#     button_in_seventh_td.click()
#
#     # Wait for the popup to appear
#     popup = WebDriverWait(driver, 10).until(EC.alert_is_present())
#
#     # Print the text of the popup (optional)
#     print("Popup Text:", popup.text)
#
#     # Accept the popup
#     popup.accept()
# else:
#     print("No rows found in the table.")
# time.sleep(3)
# # past_testsbtn = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[7]/div[3]/div/div[3]/ul/li[2]/a")))
# # past_testsbtn.click()
# # time.sleep(2)
# # archieved_testsbtn = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[7]/div[3]/div/div[3]/ul/li[3]/a")))
# # archieved_testsbtn.click()
# # time.sleep(2)
##########################################################
# name_to_search = "whose"
#
# # Wait for the table to be present
# table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="current-tests"]/div[1]/div/table')))
#
# # Find all rows (tr) in the table
# rows = table.find_elements(By.XPATH, 'tbody/tr')
#
# # Iterate through each row to find the specific name in the 1st <td>
# target_row = None
# for row in rows:
#     # Find the name within the <a> tag in the 1st <td>
#     name_in_first_td = row.find_element(By.XPATH, 'td[1]/a').text
#
#     if name_in_first_td == name_to_search:
#         target_row = row
#         break
#
# # Check if the target row is found
# if target_row:
#     # Click on the button in the 7th <td> of the target row
#     button_in_seventh_td = target_row.find_element(By.XPATH, 'td[7]//button')
#     button_in_seventh_td.click()
#
#     # Wait for the popup to appear
#     popup = WebDriverWait(driver, 10).until(EC.alert_is_present())
#
#     # Print the text of the popup (optional)
#     print("Popup Text:", popup.text)
#
#     # Accept the popup
#     popup.accept()
# else:
#     print(f"Name '{name_to_search}' not found in any row.")
#########################################################
# element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/span[2]")
#
# # Get the text from the element
# text = element.text
#
# # Print or use the text as needed
# print("Text:", text)
# # Rest of your code...
####################### d2l ##########################
# d2l_login_btn = driver.find_element(By.XPATH, "//*[contains(@id, 'd2l_1_4')]")
# buttn_text = d2l_login_btn.text
# print(buttn_text)
# d2l_login_btn.click()
# time.sleep(3)
# driver.quit()