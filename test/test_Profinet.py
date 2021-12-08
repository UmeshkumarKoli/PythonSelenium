'''
Created on Sep 23, 2019

@author: DTE_ADMIN
'''
import logging
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utils.commonFunctions import Util


@pytest.mark.DTE801
#@pytest.mark.DTE_COMMON
class Test_Profinet_Settings():
    @pytest.fixture()
    def test_setUp(self):
        object_util=Util()
        self.driver=object_util.init_ChromeDriver()
        self.LOGGER=object_util.init_Logger()
        #Util.init_IE_Driver(self)
        yield
        self.driver.close()
        self.driver.quit()

    def test_Change_Profinet_Settings(self,test_setUp):
        """Test_Profinet_Settings.test_Change_Profinet_Settings

        @DESCRIBE[[Test sequence:
        - verify [1] user defined profinet station name should save to device]
        @TESTS[DTE10x-4510]
        """
        wait=WebDriverWait(self.driver,10)
        self.driver.find_element_by_xpath("//*[@id='pnconfig']/a").click()
        self.LOGGER.info('Clicked on profinet menu')
        self.driver.switch_to.frame("center")
        element=wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#pnStationNameID")))
        element.send_keys("123456")
        self.LOGGER.info('Entered values in Station name')
        self.driver.find_element_by_css_selector("#pnsettingsID").click()
        element=wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#resetForm > input[type=checkbox]")))
        element.click()
        sleep(1)
        self.driver.find_element_by_css_selector("#resetForm input[type=submit]").click()
        self.LOGGER.info('Clicked on Submit button')
        sleep(1)
        element=wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#contentIframe > p.resp_success")))
        sleep(2)
        assert(element.text=="The device was successfully restarted.")
        self.LOGGER.info('Verified "The device was successfully restarted."')