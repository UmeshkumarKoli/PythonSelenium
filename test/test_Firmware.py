'''
Created on Sep 5, 2019

@author: DTE_ADMIN
'''
import os, pytest
from pyrobot import Robot
from pyrobot import Robot, Keys
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Paths.ConstantPaths import ConstantPaths
from Utils.commonFunctions import Util


@pytest.mark.DTE804
class Test_Firmware_Settings():
    @pytest.fixture()
    def test_setUp(self):
        object_util=Util()
        self.driver=object_util.init_ChromeDriver()
        self.LOGGER=object_util.init_Logger()
        #Util.init_IE_Driver(self)
        yield
        self.driver.close()
        self.driver.quit()
    
    def verify_settings(self):
        self.driver.switch_to_default_content()
        sleep(10)
        self.driver.find_element_by_xpath("//*[@id='fwupdate']/a").click()
        self.driver.switch_to.frame("center")
        wait=WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='fwupdateForm']/p[2]/input")))
        version_firmware=self.driver.find_element_by_xpath("//tbody/tr[2]/td[3]").text
        if(version_firmware== "V4.0.2"):
            flag3= True
        else: 
            flag3= False
        self.driver.switch_to_default_content()
        version_firmware_HardwareTable=self.driver.find_element_by_xpath("//*[@id='content']/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]").text
        if(version_firmware_HardwareTable== "V4.0.2"):
            flag4= True
        else: 
            flag4= False
        assert(flag3==True and flag4==True)
        
    def test_firmware_old(self,test_setUp):
        """Test_Firmware_Settings.test_firmware

        @DESCRIBE[[Test sequence:
        - verify [1] that firmware transfer and update succeeded.]]
        @TESTS[DTE80x_DTE90x-1354]
        """
        firmwareToTest=ConstantPaths.Firmware_DTE804_Old
        self.update_firmware(firmwareToTest)
    
    def test_firmware_new(self,test_setUp):
        firmwareToTest=ConstantPaths.Firmware_DTE804_new
        self.update_firmware(firmwareToTest)
           
    def update_firmware(self,firmwareToTest):
        #path=os.getcwd()
        self.driver.find_element_by_xpath("//*[@id='fwupdate']/a").click()
        variant_DTE=self.driver.find_element_by_xpath("//*[@id='content']//tbody/tr[2]//td[2]").text
        self.driver.switch_to.frame("center")
        wait=WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='fwupdateForm']/p[2]/input")))
        self.driver.find_element_by_xpath("//*[@id='fwupdateForm']/p[2]/input").send_keys(os.getcwd()+'\\'+firmwareToTest)
#         sleep(1)
#         robot=Robot()
#         robot.add_to_clipboard(os.getcwd()+'\\'+firmwareToTest)
#         robot.paste()
#         robot.press_and_release(Keys.enter)
#         sleep(2)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='contentIframe']/p[1]/b")))
        if(self.driver.find_element_by_xpath("//*[@id='contentIframe']/p[1]/b").text== "Firmware transfer and update succeeded!"):
            flag1= True
        else: 
            flag1= False
        sleep(1)
        self.driver.find_element_by_xpath("//input[@type='checkbox']").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='contentIframe']/p[1]")))
        sleep(2)
        if(self.driver.find_element_by_xpath("//*[@id='contentIframe']/p[1]").text== "The device was successfully restarted."):
            flag2= True
        else: 
            flag2= False
        assert(flag1==True and flag2==True)
        self.verify_settings()