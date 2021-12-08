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
class Test_Info():
    @pytest.fixture()
    def test_setUp(self):
        object_util=Util()
        self.driver=object_util.init_ChromeDriver()
        self.LOGGER=object_util.init_Logger()
        #Util.init_IE_Driver(self)
        yield
        self.driver.close()
        self.driver.quit()

    def test_Info_Settings(self,test_setUp):
        wait=WebDriverWait(self.driver,10)
        self.driver.find_element_by_css_selector("#info > a").click()
        self.LOGGER.info('Clicked on info menu')
        self.driver.switch_to.frame("center")
        element=wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#contentIframe > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(1)")))
        self.LOGGER.info('Information table is visible')
        sleep(1)
        element=self.driver.find_element_by_css_selector("#license > span > a")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        sleep(2)
        self.driver.switch_to.default_content()
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        sleep(2)
        if (self.driver.find_element_by_css_selector("body > a:nth-child(5)").text=="List of licenses included in newlib 1.14.0 (ARM syscalls) by package"):
            flag1=True
        else:
            flag1=False
        if (self.driver.find_element_by_css_selector("body > a:nth-child(7)").text=="List of copyrights included in newlib 1.14.0 (ARM syscalls) by file"):
            flag2=True
        else:
            flag2=False
        if (self.driver.find_element_by_css_selector("body > a:nth-child(9)").text=="List of licenses included in MD5 by package"):
            flag3=True
        else:
            flag3=False
        if (self.driver.find_element_by_css_selector("body > a:nth-child(11)").text=="List of copyrights included in MD5 by file"):
            flag4=True
        else:
            flag4=False
        if (self.driver.find_element_by_css_selector("body > a:nth-child(13)").text=="List of licenses included in linenoise by package"):
            flag5=True
        else:
            flag5=False
        if (self.driver.find_element_by_css_selector("body > a:nth-child(15)").text=="List of copyrights included in linenoise by file"):
            flag6=True
        else:
            flag6=False
        if (self.driver.find_element_by_css_selector("body > a:nth-child(17)").text=="List of licenses included in Lua 5.1.4 by package"):
            flag7=True
        else:
            flag7=False
        if (self.driver.find_element_by_css_selector("body > a:nth-child(19)").text=="List of copyrights included in Lua 5.1.4 by file"):
            flag8=True
        else:
            flag8=False
        if (self.driver.find_element_by_css_selector("body > a:nth-child(21)").text=="List of licenses included in web documents by package"):
            flag9=True
        else:
            flag9=False
        if (self.driver.find_element_by_css_selector("body > a:nth-child(23)").text=="List of copyrights included in web documents by file"):
            flag10=True
        else:
            flag10=False
        if (self.driver.find_element_by_css_selector("body > a:nth-child(25)").text=="Complete licenses Text"):
            flag11=True
        else:
            flag11=False  
             
        self.driver.find_element_by_css_selector("body > a:nth-child(25)").click()
        sleep(2)
        assert(flag1==True and flag2==True and flag3==True and
               flag4==True and flag5==True and flag6==True  and
               flag7==True and flag8==True and flag9==True and
               flag10==True and flag11==True)