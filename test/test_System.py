'''
Created on Sep 17, 2019

@author: DTE_ADMIN
'''
import os
from pyrobot import Robot, Keys
from sqlite3 import Time
import subprocess
from time import sleep
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Paths.ConstantPaths import ConstantPaths
from Utils.commonFunctions import Util

@pytest.mark.DTE_COMMON
class Test_System_Settings():

    def setPassword(self,oldPass,newPass):
        
        self.driver.find_element_by_xpath("//*[@id='pwpForm']//input[@name='passwordOld']").send_keys(oldPass)
        self.driver.find_element_by_xpath("//*[@id='pwpForm']//input[@name='passwordNew']").send_keys(newPass)
        self.driver.find_element_by_xpath("//*[@id='pwpForm']//input[@name='passwordConf']").send_keys(newPass)
        self.driver.find_element_by_xpath("//*[@id='pwpForm']//input[@type='submit']").click()

    @pytest.fixture()
    def test_setUp(self):
        object_util=Util()
        self.driver=object_util.init_ChromeDriver()
        #self.driver=object_util.init_IE_Driver()
        self.LOGGER=object_util.init_Logger() 
        yield
        self.driver.switch_to.default_content()
        sleep(10)
        #subprocess.call(ConstantPaths.PasswordUnlockAutoIt)
        self.driver.get("http://admin:iepl@192.168.0.79/awe/main.sht?target=system&setLng=en")
        self.driver.switch_to.frame("center")
        wait=WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='pwpForm']//input[@value='off']")))
        self.driver.find_element_by_xpath("//*[@id='pwpForm']//input[@value='off']").click()
        self.setPassword("iepl","admin")
        if not self.driver.find_element_by_css_selector("#resetForm > input[type=checkbox]").is_selected():
            self.driver.find_element_by_css_selector("#resetForm > input[type=checkbox]").click()
        #self.driver.find_element_by_xpath("//*[@id='resetForm']//input[@name='submit_button']").click()
        self.driver.find_element_by_css_selector("#resetForm > table > tbody > tr > td > input[type=submit]").click()
        sleep(1)
        self.driver.quit()

        
    def test_System_Settings(self,test_setUp):
        """Test_System_Settings.test_System_Settings

        @DESCRIBE[[Test sequence:
        - verify [1] that user should set system password. 
        - verify [2] Whenever user click on system menu it should ask for authentication.]]
        @TESTS[DTE80x_DTE90x-1349]
        """
        #self.driver.find_element_by_xpath("//*[@id='system']/a").click()
        self.driver.find_element_by_id('system').click()
        sleep(1)
        self.driver.find_element_by_id('system').click()
        self.driver.switch_to.frame("center")
        wait=WebDriverWait(self.driver,10)
        #sleep(2)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='pwpForm']//input[@value='on']")))
        self.driver.find_element_by_xpath("//*[@id='pwpForm']//input[@value='on']").click()
        self.setPassword("admin","iepl")
        element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='contentIframe']/table//span")))
        if(element.text== "on"):
            flag1= True
        else: 
            flag1= False
        if(self.driver.find_element_by_xpath("//*[@id='contentIframe']/p[1]").text== "The password protection has been activated."):
            flag2= True
        else: 
            flag2= False
        if(self.driver.find_element_by_xpath("//*[@id='contentIframe']/p[2]").text== "Your password has been changed successfully."):
            flag3= True
        else: 
            flag3= False
        #self.driver.find_element_by_xpath("//*[@id='resetForm']/input").click()
        self.driver.find_element_by_css_selector("#resetForm > input[type=checkbox]").click()
        sleep(1)
        if not self.driver.find_element_by_css_selector("#resetForm > input[type=checkbox]").is_selected():
            self.driver.find_element_by_css_selector("#resetForm > input[type=checkbox]").click()
        #self.driver.find_element_by_xpath("//*[@id='resetForm']//input[@name='submit_button']").click()
        self.driver.find_element_by_css_selector("#resetForm > table > tbody > tr > td > input[type=submit]").click()
        sleep(1)
        element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='contentIframe']/p[1]")))
        if(element.text== "The device was successfully restarted."):
            flag4= True
        else: 
            flag4= False
        
        assert(flag1==True and flag2==True and flag3==True and flag4==True)