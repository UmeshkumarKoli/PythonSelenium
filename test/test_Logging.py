'''
Created on Oct 3, 2019

@author: DTE_ADMIN
'''
import logging
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utils.commonFunctions import Util

@pytest.mark.DTE_COMMON
class Test_Logging():
    @pytest.fixture()
    def test_setUp(self):
        object_util=Util()
        self.driver=object_util.init_ChromeDriver()
        self.LOGGER=object_util.init_Logger()
        #Util.init_IE_Driver(self)
        yield
        self.driver.get("http://192.168.0.79/service")
        Select(self.driver.find_element_by_xpath("//select[@name='loglevel']")).select_by_index(1)
        self.driver.find_element_by_css_selector("#subContentIframe input[type='radio']:nth-child(2)").click()
        self.driver.find_element_by_css_selector("#subContentIframe > form:nth-child(4) > table > tbody > tr:nth-child(5) > td:nth-child(2) > input[type='submit']").click()
        self.driver.close()
        self.driver.quit()

    def test_Service(self,test_setUp):
        self.driver.get("http://192.168.0.79/service")
        wait=WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#subContentIframe select")))
        element=self.driver.find_elements_by_css_selector("#subContentIframe select > option")
        countOfOptions= len(element)
        if (countOfOptions== 4):
            flag1=True
        else:
            flag1= False
        for loglevel in range(countOfOptions):
            Select(self.driver.find_element_by_xpath("//select[@name='loglevel']")).select_by_index(loglevel)
            element=Select(self.driver.find_element_by_xpath("//select[@name='loglevel']")).first_selected_option
            LogLevelText=element.text
            self.LOGGER.info("LogLevel %s = %s" %(loglevel+1, LogLevelText))
            self.driver.find_element_by_css_selector("#subContentIframe input[type='radio']:nth-child(1)").click()
            self.driver.find_element_by_css_selector("#subContentIframe > form:nth-child(4) > table > tbody > tr:nth-child(5) > td:nth-child(2) > input[type='submit']").click()
            sleep(1)
            if (self.driver.find_element_by_css_selector("#contentIframe > p").text=="Changing logging configuration successfully performed:"):
                flag2=True
            else:
                flag2=False
            if (self.driver.find_element_by_css_selector("#contentIframe tr.row_odd > td.sysvar").text==LogLevelText) and (self.driver.find_element_by_css_selector("#contentIframe tr.row_even > td.sysvar").text=="on"):
                flag3=True
            else:
                flag3=False
                                
            assert(flag2==True and flag3==True)
            self.driver.get("http://192.168.0.79/service")
            if (self.driver.find_element_by_css_selector("#subContentIframe > form:nth-child(4) > table > tbody > tr.row_odd > td:nth-child(2)").text==LogLevelText) and (self.driver.find_element_by_css_selector("#subContentIframe > form:nth-child(4) > table > tbody > tr.row_even > td:nth-child(2)").text=="on") :
                flag4=True
            else:
                flag4=False
            assert(flag4==True)