'''
Created on Aug 26, 2019

@author: DTE_ADMIN
'''
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utils.commonFunctions import Util


@pytest.mark.DTE_COMMON
class Test_IO_Port_settings():

    @pytest.fixture()
    def test_setUp(self):
        object_util=Util()
        self.driver=object_util.init_ChromeDriver()
        self.LOGGER=object_util.init_Logger()
        #Util.init_IE_Driver(self)
        yield
        self.defaultValues()
        self.driver.find_element_by_name("action").click()
        self.driver.quit()

    def defaultValues(self):
        self.driver.find_element_by_xpath("//*[@id='failsafeOff']").click()
        Select(self.driver.find_element_by_id("selektor_channel_io1")).select_by_value("rwh_rw")
        Select(self.driver.find_element_by_name("dataHoldTime_io1")).select_by_visible_text("0")
        Select(self.driver.find_element_by_id("selektor_channel_io2")).select_by_value("portmode_off")
        Select(self.driver.find_element_by_id("selektor_channel_io3")).select_by_value("portmode_off")        
        self.driver.find_element_by_name("action").click()
        sleep(1)
        self.driver.find_element_by_name("action").click()
        
    def test_change_Settings(self,test_setUp):
        """Test_IO_Port_settings.test_change_Settings

        @DESCRIBE[[Test sequence:
        - verify [1] that changes should be saved 
        - verify [2] same values that are saved are reflecting on page.]]
        @TESTS[DTE80x_DTE90x-1352]
        """
        self.driver.find_element_by_xpath("//*[@id='ioportconfig']/a").click()
        self.driver.switch_to.frame("center")
        sleep(2)
        self.defaultValues()
        
        # Global_Settings
        self.driver.find_element_by_xpath("//*[@id='failsafeOn']").click()
        
        Select(self.driver.find_element_by_id("selektor_channel_io1")).select_by_value("rwh_rw")
        Select(self.driver.find_element_by_name("dataHoldTime_io1")).select_by_visible_text("100")
        
        # IO-1 Settings
        Select(self.driver.find_element_by_id("selektor_channel_io2")).select_by_value("input")
        Select(self.driver.find_element_by_name("dataHoldTime_io2")).select_by_visible_text("2000")
        
        # IO-2 Settings
        Select(self.driver.find_element_by_id("selektor_channel_io3")).select_by_value("output")
        Select(self.driver.find_element_by_name("dataHoldTime_io3")).select_by_visible_text("20")
                
        # Click on Activate and Save
        self.driver.find_element_by_name("action").click()
        
        # Verification
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='tblPortconfig']/tbody[1]/tr[1]/td[2]/span")))
        
        if (self.driver.find_element_by_xpath("//*[@id='tblPortconfig']/tbody[1]/tr[1]/td[2]/span").text == "on"):
            flag1 = True
        else: 
            flag1 = False
        if (self.driver.find_element_by_xpath("//*[@id='currmode_channel_io1']/span").text == "RWH RW"):
            flag2 = True
        else: 
            flag2 = False
        if(self.driver.find_element_by_xpath("//*[@id='tblPortconfig']/tbody[2]/tr[2]/td[2]").text == "100"):
            flag3 = True
        else: 
            flag3 = False
             
        if(self.driver.find_element_by_xpath("//*[@id='currmode_channel_io2']/span").text == "Input"):
            flag4 = True
        else: 
            flag4 = False
        if(self.driver.find_element_by_xpath("//*[@id='tblPortconfig']/tbody[3]/tr[2]/td[2]").text == "2000"):
            flag5 = True
        else: 
            flag5 = False
        
        if(self.driver.find_element_by_xpath("//*[@id='currmode_channel_io3']/span").text == "Output"):
            flag6 = True
        else: 
            flag6 = False
        if(self.driver.find_element_by_xpath("//*[@id='tblPortconfig']/tbody[4]/tr[2]/td[2]").text == "20"):
            flag7 = True
        else: 
            flag7 = False
            
        self.driver.find_element_by_xpath("//input[@name='action']").click()
        assert(flag1==True and flag2==True and flag3==True and
               flag4==True and flag5==True and flag6==True and
               flag7==True)
        
        sleep(1)
