
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import Login
from pageObjects.SelectTest import SelectTest
from utilities.readproperties import ReadConfig
from utilities.customlogger import CustomLogger


class TestSelectFunctionality:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = CustomLogger.configure_logger()

    @pytest.mark.regression
    def test_select_functionality(self, setup):
        self.logger.info("======= Test Select Functionality =======")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 10)
        change_test_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Change Test']")))

        select_test_page = SelectTest(self.driver)
        select_test_page.change_test()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='test_list']/div")))
        test_name_to_select = "L3"
        result = select_test_page.select_test(test_name_to_select)

        if result:
            print(f"Selected test text matches the div text. {test_name_to_select}")
            assert True
        else:
            print("Selected test text does not match the div text. Test is failed.")
            assert False

        self.driver.close()

