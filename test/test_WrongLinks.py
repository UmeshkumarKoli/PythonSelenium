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
class Test_WrongLinks():
    @pytest.fixture()
    def test_setUp(self):
        object_util=Util()
        self.driver=object_util.init_ChromeDriver()
        self.LOGGER=object_util.init_Logger()
        #Util.init_IE_Driver(self)
        yield
        self.driver.close()
        self.driver.quit()

    def test_Wrong_Links(self,test_setUp):
        linkList=[  "http://192.168.0.79/awe/main.sht?target=monitor11&setLng=en", 
                    "http://192.168.0.79/awe/main.sht?target=monitor11&setLng=en", 
                    "http://192.168.0.79/awe/main.sht?targets=monitor&setLng=en", 
                    "http://192.168.0.79/awe/subdomain.sht?target=monitor&setLng=en", 
                    "http://192.168.0.79/awe/main.shtml?target=monitor&setLng=en", 
                    "http://192.168.0.79/dte/main.sht?target=monitor11&setLng=en", 
                    "http://192.168.0.79/dte/", 
                    "http://192.168.0.79/awe", 
                    "http://192.168.0.79/awe/home.html",
                    "http://192.168.0.79/dte/setLng=osffis" ]
        wait=WebDriverWait(self.driver,10)
        
        for link in linkList:
            self.driver.get(link)
            self.LOGGER.info('Navigate to invalid URL %s' %link)
            iframeCount=len(self.driver.find_elements(By.TAG_NAME, "iframe"))
            if(iframeCount>0):
                self.driver.switch_to.frame("center")
            element=wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//body[text()='HTTP Status: 404 Not Found']")))
            self.LOGGER.info('%s message found' % element.text)
            assert(element.text== 'HTTP Status: 404 Not Found')
        
        correctLink_WrongLanguageLink="http://192.168.0.79/awe/main.sht?target=ipconfig&setLng=ossfi"
        self.driver.get(correctLink_WrongLanguageLink)
        self.LOGGER.info('Navigate to Correct URL but wrong language i.e %s' %correctLink_WrongLanguageLink)
        self.driver.switch_to.frame("center")
        element=wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@name='ip0']")))
        self.LOGGER.info('Network Ip configuration page is visible')
        assert(element.is_displayed()== True)