from selenium.webdriver.common.by import By


class SelectD2Lcourse:
    course_name_xpath = ('//*[@id="panel-search-my-enrollments"]/d2l-my-courses-content//d2l-my-courses-card-grid//div'
                         '/d2l-enrollment-card//d2l-card//div/a/span')

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(driver, 10)

    def get_course_name(self):
        course_name = self.driver.find_element(By.XPATH, self.course_name_xpath)
        text = course_name.text
        return text
