'''
Created on Aug 26, 2019

@author: DTE_ADMIN
'''
import os
from pyrobot import Robot, Keys
from time import sleep

import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Paths.ConstantPaths import ConstantPaths
from Utils.commonFunctions import Util


@pytest.mark.DTE_COMMON
class Test_RWH_settings():

    @pytest.fixture()
    def test_setUp(self):
        object_util=Util()
        self.driver=object_util.init_ChromeDriver()
        self.LOGGER=object_util.init_Logger()
        #Util.init_IE_Driver(self)
        yield
        self.defaultValues()
        self.driver.quit()

    def defaultValues(self):
        self.driver.find_element_by_xpath("//input[@value='ident_stable']").click()
        value_hf_power_rd_slider=  self.driver.find_element_by_id("hf_power_rd_slider").get_attribute("value")
        value_hf_power_wr_slider=  self.driver.find_element_by_id("hf_power_wr_slider").get_attribute("value")
        
        if (value_hf_power_rd_slider!="23") or (value_hf_power_wr_slider!="23"):
            self.driver.execute_script("arguments[0].value=23", self.driver.find_element_by_id("hf_power_rd_slider"))
            self.driver.execute_script("arguments[0].value=23", self.driver.find_element_by_id("hf_power_wr_slider"))   
            self.driver.find_element_by_css_selector("#antennaCfgForm input[type='button']:nth-child(1)").click()
            sleep(1)
            respose=self.driver.find_element_by_xpath("//*[@id='antennaCfgForm']/p").text
            assert(respose== "The settings have been accepted.")        
        self.driver.switch_to.default_content()
    
    def defaultValues_customizeSetting(self):
        self.driver.find_element_by_xpath("//input[@value='ident_customized']").click()
        value_hf_power_rd_slider=  self.driver.find_element_by_id("hf_power_rd_slider").get_attribute("value")
        value_hf_power_wr_slider=  self.driver.find_element_by_id("hf_power_wr_slider").get_attribute("value")
        if (value_hf_power_rd_slider!="23") or (value_hf_power_wr_slider!="23"):
            self.driver.execute_script("arguments[0].value=23", self.driver.find_element_by_id("hf_power_rd_slider"))
            self.driver.execute_script("arguments[0].value=23", self.driver.find_element_by_id("hf_power_wr_slider"))  
            
        Select(self.driver.find_element_by_id("ant_rf_mode_sel")).select_by_visible_text("PR-ASK, M4, 250KHz, DRM (FCC)")
        self.driver.find_element_by_id("idle_time").clear()
        self.driver.find_element_by_id("idle_time").send_keys("50")
        
        self.driver.find_element_by_id("inventory_time").clear()
        self.driver.find_element_by_id("inventory_time").send_keys("200")
        
        self.driver.find_element_by_id("estimated_id_tag_count").clear()
        self.driver.find_element_by_id("estimated_id_tag_count").send_keys("16") 
        self.driver.find_element_by_css_selector("#antennaCfgForm input[type='button']:nth-child(1)").click()
        sleep(1)
        respose=self.driver.find_element_by_xpath("//*[@id='antennaCfgForm']/p").text
        assert(respose== "The settings have been accepted.")        
        self.driver.switch_to.default_content()
        
    def test_change_QuickSettings(self,test_setUp):
        """Test_RWH_settings.test_change_Settings

        @DESCRIBE[[Test sequence:
        - verify [1] that changes should be saved 
        - verify [2] same values that are saved are reflecting on page.]]
        @TESTS[DTE80x_DTE90x-1353]
        """
        wait=WebDriverWait(self.driver,10)
        self.driver.find_element_by_xpath("//*[@id='antenna']/a").click()
        self.driver.switch_to.frame("center")
        sleep(2)
        self.defaultValues()
        
        self.driver.find_element_by_xpath("//*[@id='antenna']/a").click()
        self.driver.switch_to.frame("center")
        self.driver.find_element_by_xpath("//input[@value='ident_quick']").click()
        self.driver.execute_script("arguments[0].value=16", self.driver.find_element_by_id("hf_power_rd_slider"))
        self.driver.execute_script("arguments[0].value=16", self.driver.find_element_by_id("hf_power_wr_slider")) 
        self.driver.find_element_by_css_selector("#antennaCfgForm input[type='button']:nth-child(1)").click()
        sleep(1)
        respose=self.driver.find_element_by_xpath("//*[@id='antennaCfgForm']/p").text
        assert(respose== "The settings have been accepted.")        
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@id='antenna']/a").click()
        self.driver.switch_to.frame("center")
        value_hf_power_rd_slider=  self.driver.find_element_by_id("hf_power_rd_slider").get_attribute("value")
        value_hf_power_wr_slider=  self.driver.find_element_by_id("hf_power_wr_slider").get_attribute("value")
        if (value_hf_power_rd_slider=="16") and (value_hf_power_wr_slider=="16"):
            assert(True)
        else:
            assert(False)
            
    def test_change_CustomizedSettings(self,test_setUp):
        """Test_RWH_settings.test_change_Settings

        @DESCRIBE[[Test sequence:
        - verify [1] that changes should be saved 
        - verify [2] same values that are saved are reflecting on page.]]
        @TESTS[DTE80x_DTE90x-1353]
        """
        wait=WebDriverWait(self.driver,10)
        self.driver.find_element_by_xpath("//*[@id='antenna']/a").click()
        self.driver.switch_to.frame("center")
        sleep(2)
        self.defaultValues_customizeSetting()
        
        self.driver.find_element_by_xpath("//*[@id='antenna']/a").click()
        self.driver.switch_to.frame("center")
        self.driver.find_element_by_xpath("//input[@value='ident_customized']").click()
        self.driver.execute_script("arguments[0].value=16", self.driver.find_element_by_id("hf_power_rd_slider"))
        self.driver.execute_script("arguments[0].value=16", self.driver.find_element_by_id("hf_power_wr_slider")) 
        Select(self.driver.find_element_by_id("ant_rf_mode_sel")).select_by_visible_text("DSB-ASK, FM0, 400KHz")
        self.driver.find_element_by_id("idle_time").clear()
        self.driver.find_element_by_id("idle_time").send_keys("250")
        
        self.driver.find_element_by_id("inventory_time").clear()
        self.driver.find_element_by_id("inventory_time").send_keys("700")
        
        self.driver.find_element_by_id("estimated_id_tag_count").clear()
        self.driver.find_element_by_id("estimated_id_tag_count").send_keys("31000")
        
        self.driver.find_element_by_css_selector("#antennaCfgForm input[type='button']:nth-child(1)").click()
        sleep(1)
        respose=self.driver.find_element_by_xpath("//*[@id='antennaCfgForm']/p").text
        assert(respose== "The settings have been accepted.")        
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@id='antenna']/a").click()
        self.driver.switch_to.frame("center")
        
        value_hf_power_rd_slider=  self.driver.find_element_by_id("hf_power_rd_slider").get_attribute("value")
        value_hf_power_wr_slider=  self.driver.find_element_by_id("hf_power_wr_slider").get_attribute("value")
        if (value_hf_power_rd_slider=="16") and (value_hf_power_wr_slider=="16"):
            assert(True)
        else:
            assert(False)
        sleep(2)
        rf_Mode_selected_Opt=Select(self.driver.find_element_by_id("ant_rf_mode_sel")).first_selected_option
        if(rf_Mode_selected_Opt.text=="DSB-ASK, FM0, 400KHz"):
            assert(True)
        else:
            assert(False)
        value_idle_time=  self.driver.find_element_by_id("idle_time").get_attribute("value")
        value_inventory_time=  self.driver.find_element_by_id("inventory_time").get_attribute("value")
        value_tag_count=  self.driver.find_element_by_id("estimated_id_tag_count").get_attribute("value")
        if(value_idle_time=="250") and (value_inventory_time=="700") and(value_tag_count=="31000")  :
            assert(True)
        else:
            assert(False)
            