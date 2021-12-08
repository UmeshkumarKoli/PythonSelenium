'''
Created on Oct 3, 2019

@author: DTE_ADMIN
'''
import logging
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utils.commonFunctions import Util

@pytest.mark.DTE_COMMON
class Test_Rest():
    @pytest.fixture()
    def test_setUp(self):
        object_util=Util()
        self.driver=object_util.init_ChromeDriver()
        self.LOGGER=object_util.init_Logger()
        #Util.init_IE_Driver(self)
        yield
        self.driver.close()
        self.driver.quit()

    def test_Reset_Function(self,test_setUp):
        """Test_Rest.test_Reset_Function

        @DESCRIBE[[Test sequence:
        - verify [1] when user click on reset, device should restart within 10 second.]]
        @TESTS[DTE80x_DTE90x-1347]
        """
        wait=WebDriverWait(self.driver,10)
        self.driver.find_element_by_css_selector("#reset > a").click()
        self.LOGGER.info('Clicked on reset menu')
        self.driver.switch_to.frame("center")
        element=wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#contentIframe input[type=checkbox]")))
        element.click()
        self.LOGGER.info('Clicked on "Please confirm you want to reboot the device Checkbox" ')
        self.driver.find_element_by_css_selector("#contentIframe input[type=submit]").click()
        self.LOGGER.info('Clicked on Reset button')
        sleep(2)
        element=wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#contentIframe > p.resp_success")))
        sleep(2)
        assert(element.text=="The device was successfully restarted.")
        self.LOGGER.info('Verified "The device was successfully restarted."')
        sleep(5)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector("#reset > a").click()
        self.driver.switch_to.frame("center")
        element=wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#contentIframe input[type=checkbox]")))
        element.click()