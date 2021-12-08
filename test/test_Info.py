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
        """Test_Info.test_Info_Settings

        @DESCRIBE[[Test sequence:
        - verify [1] all information showing in table related to device.]]
        @TESTS[DTE80x_DTE90x-1348]
        """
        wait=WebDriverWait(self.driver,10)
        self.driver.find_element_by_css_selector("#info > a").click()
        self.LOGGER.info('Clicked on info menu')
        self.driver.switch_to.frame("center")
        element=wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#contentIframe > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(1)")))
        self.LOGGER.info('Information table is visible')
        sleep(1)
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(1)").text=="Power supply state:"):
            flag1= True
        else:
            flag1= False
        self.LOGGER.info('Checked Power Supply State = %s', self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(2) > tbody > tr:nth-child(2) > td.sysvar > span").text)
        
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(1)").text=="Temperature:"):
            flag2= True
        else:
            flag2= False
        self.LOGGER.info('Checked temperature value= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(2) > tbody > tr:nth-child(3) > td.sysvar").text)
       
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(2) > tbody > tr:nth-child(4) > td:nth-child(1)").text=="Reader temperature:"):
            flag3= True
        else:
            flag3= False
        self.LOGGER.info('Checked Reader temperature:= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(2) > tbody > tr:nth-child(4) > td.sysvar").text)
       
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(2) > tbody > tr:nth-child(5) > td:nth-child(1)").text=="System time:"):
            flag4= True
        else:
            flag4= False
        self.LOGGER.info('Checked System time value= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(2) > tbody > tr:nth-child(5) > td.sysvar").text)
        
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(2) > tbody > tr:nth-child(6) > td:nth-child(1)").text=="System date:"):
            flag5= True
        else:
            flag5= False
        self.LOGGER.info('Checked System date value= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(2) > tbody > tr:nth-child(6) > td.sysvar").text)
        
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(5) > tbody > tr.row_odd > td:nth-child(1)").text=="Product article number:"):
            flag5= True
        else:
            flag5= False
        self.LOGGER.info('Checked Product article number:= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(5) > tbody > tr.row_odd > td.sysvar").text)
        
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(5) > tbody > tr.row_even > td:nth-child(1)").text=="Production number:"):
            flag6= True
        else:
            flag6= False
        self.LOGGER.info('Checked Production number:= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(5) > tbody > tr.row_even > td.sysvar").text) 
        
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(5) > tbody > tr:nth-child(4) > td:nth-child(1)").text=="Version PermData:"):
            flag7= True
        else:
            flag7= False
        self.LOGGER.info('Checked Version PermData:= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(5) > tbody > tr:nth-child(4) > td.sysvar").text) 
        
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(2) > td:nth-child(1)").text=="Device Type:"):
            flag8= True
        else:
            flag8= False
        self.LOGGER.info('Checked Device Type:= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(2) > td.sysvar").text) 
        
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(3) > td:nth-child(1)").text=="Hardware Version:"):
            flag9= True
        else:
            flag9= False
        self.LOGGER.info('Checked Hardware Version:= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(3) > td.sysvar").text) 
        
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(4) > td:nth-child(1)").text=="IDLink SW:"):
            flag10= True
        else:
            flag10= False
        self.LOGGER.info('Checked IDLink SW:= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(4) > td.sysvar").text) 
       
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(5) > td:nth-child(1)").text=="Firmware Version:"):
            flag11= True
        else:
            flag11= False
        self.LOGGER.info('Checked Firmware Version:= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(5) > td.sysvar").text) 
        
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(6) > td:nth-child(1)").text=="Reader Type:"):
            flag12= True
        else:
            flag12= False
        self.LOGGER.info('Checked Reader Type:= %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(6) > td.sysvar").text) 
         
        if (self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(7) > td:nth-child(1)").text=="Reader Firmware Version:"):
            flag13= True
        else:
            flag13= False
        self.LOGGER.info('Checked Reader Firmware Version: = %s',self.driver.find_element_by_css_selector("#contentIframe > table:nth-child(8) > tbody > tr:nth-child(7) > td.sysvar").text) 
          
        #print flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8,flag9
        assert(flag1==True and flag2==True and flag3==True and
               flag4==True and flag5==True and flag6==True  and
               flag7==True and flag8==True and flag9==True and
               flag10==True and flag11==True and flag12==True and
               flag13==True )