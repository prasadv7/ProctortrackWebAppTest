import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


# Your login steps...
def get_total_images_with_scroll(driver, container_xpath):
    try:
        # Wait for the container element to be present
        container_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, container_xpath)))

        total_images = 0
        last_count = -1

        while last_count != total_images:
            last_count = total_images

            # Get all image elements within the container
            image_elements = container_element.find_elements(By.XPATH, ".//img")
            total_images = len(image_elements)

            # Scroll down to load more images
            driver.execute_script("arguments[0].scrollIntoView();", image_elements[-1])

            # Wait for some time for new images to load
            time.sleep(2)

        # Return the final total number of images
        return total_images
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


driver = webdriver.Chrome()
driver.get("https://preproduction.verificient.com/")

username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='id_username']")))
username_input.send_keys("prasadvidhate+inst@verificient.com")

password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='id_password']")))
password_input.send_keys("Vidhaterajendra7@")

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='log_in']")))
login_button.click()

time.sleep(2)

# Navigating to a new URL
new_url = 'https://preproduction.verificient.com/614e06160524313a1a3f4a17/proctoring/review/session/e5067c9e1c0849e3b49175a93751a291/new/'
driver.get(new_url)

# Wait for the loading screen to disappear
loading_screen_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/i"
try:
    WebDriverWait(driver, 10).until_not(EC.visibility_of_element_located((By.XPATH, loading_screen_xpath)))
    print("Loading screen has disappeared.")
except Exception as e:
    print(f"An error occurred: {e}")

# Checking if the video element is present
video_xpath = "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div/div/videogular"
try:
    video_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, video_xpath)))

    if video_element.is_displayed():
        print("Video element is present on the page.")
    else:
        print("Video element is not visible.")
except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(3)

# Online Violation button
online_violation_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/ul/li[2]/a")))
online_violation_btn.click()

# Allow some time for the content to load
time.sleep(5)
snapshot_density_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[4]/div/div/div[2]/div/div[3]/span/span/button')))
snapshot_density_btn.click()
dense_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[4]/div/div/div[2]/div/div[3]/span/span/ul/li/a')))
dense_btn.click()
time.sleep(1)


# Get the total number of images
container_xpath = "//*[@id='scroll_container']"
total_images = get_total_images_with_scroll(driver, container_xpath)

if total_images:
    print(f"Total number of images: {total_images}")
else:
    print("Unable to retrieve the total number of images.")

driver.quit()
