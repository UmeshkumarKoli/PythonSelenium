import logging
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utils.commonFunctions import Util

@pytest.mark.DTE_COMMON

class Test_Monitor():
    @pytest.fixture()
    def test_setUp(self):
        object_util=Util()
        self.driver=object_util.init_ChromeDriver()
        self.LOGGER=object_util.init_Logger()
        #Util.init_IE_Driver(self)
        yield
        #test_case_name=__name__
        #self.driver.get_screenshot_as_file("%s.png" % test_case_name)
        self.driver.close()
        self.driver.quit()

    def test_Monitor_Page(self,test_setUp):
        """Test_Monitor.test_Monitor_Page

        @DESCRIBE[[Test sequence:
        - verify [1] that user can read/write to tag]]
        @TESTS[DTE80x_DTE90x-1351,DTE80x_DTE90x-1344]
        """
        wait=WebDriverWait(self.driver,10)
        self.driver.find_element_by_css_selector("#monitor > a").click()
        self.LOGGER.info('Clicked on Monitor menu')
        self.driver.switch_to.frame("center")
         
        if (self.driver.find_element_by_xpath("//*[@id='uhf_tag0_epc']").text !=""):
            self.driver.find_element_by_xpath("//*[@id='uhf_tag0_epc']").click()
            
            self.driver.find_element_by_id("inpDataFormat").click()
            Select(self.driver.find_element_by_id("inpDataFormat")).select_by_visible_text("ASCII")
            self.driver.find_element_by_id("inpDataFormat").click()
            
            self.driver.find_element_by_id("inpTagOffset").click()
            self.driver.find_element_by_id("inpTagOffset").clear()
            self.driver.find_element_by_id("inpTagOffset").send_keys("0")
            self.driver.find_element_by_id("btnReadTag").click()
            
            sleep(1)
            error_respose=self.driver.find_element_by_xpath("//*[@id='contentIframe']/p[2]").text
            if (error_respose== "ERROR: Reading/writing data has been rejected because of an invalid data length (1 .. 240 bytes)."):
                flag1= True
            else: 
                flag1= False
                
            self.driver.find_element_by_id("inpDataFormat").click()
            Select(self.driver.find_element_by_id("inpDataFormat")).select_by_visible_text("ASCII")
            self.driver.find_element_by_id("inpDataFormat").click()
            
            self.driver.find_element_by_id("inpTagOffset").clear()
            self.driver.find_element_by_id("inpTagOffset").send_keys("0")
            self.driver.find_element_by_id("lengthUnit").click()
            self.driver.find_element_by_id("displayTagData").click()
            self.driver.find_element_by_id("displayTagData").clear()
            self.driver.find_element_by_id("displayTagData").send_keys("UmeshKoliPuneMahara") # length is 19
            self.driver.find_element_by_id("btnWriteTag").click()
            sleep(1)
            if(self.driver.find_element_by_xpath("//*[@id='contentIframe']/p[2]/span").text== "INFO: Data were successfully written."):
                flag2= True
            else: 
                flag2= False
            
            self.driver.find_element_by_id("inpTagLength").clear()
            self.driver.find_element_by_id("inpTagLength").send_keys("24")
            self.driver.find_element_by_id("btnReadTag").click()
            self.driver.find_element_by_id("displayTagData").click()
            sleep(1)
            if("UmeshKoliPuneMahara....."== self.driver.find_element_by_id("displayTagData").get_attribute("value")):
                flag3=True
            else:
                flag3=False
        
            assert(flag1==True and flag2==True and flag3==True)
        else:
            print("Tag is not available")
            assert(False)