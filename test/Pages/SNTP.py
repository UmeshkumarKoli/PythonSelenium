'''
Created on Sep 19, 2019

@author: DTE_ADMIN
'''
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Utils import commonFunctions


class SNTP_Settings():
    SNTP_MENU=(By.CSS_SELECTOR,'#sntpconfig > a')
    SNTP_SUPPORT_RADIO_ON=(By.CSS_SELECTOR,"input[type='radio']:nth-child(1)")
    SNTP_SUPPORT_RADIO_OFF=(By.CSS_SELECTOR,"input[type='radio']:nth-child(3)")
    SNTP_IP_ADDRESS_FIRST=(By.CSS_SELECTOR,"#sntpcfgForm  tr[class='row_even']  input[type=text]:nth-child(1)")
    SNTP_IP_ADDRESS_SECOND=(By.CSS_SELECTOR,"#sntpcfgForm  tr[class='row_even']  input[type=text]:nth-child(2)")
    SNTP_IP_ADDRESS_THIRD=(By.CSS_SELECTOR,"#sntpcfgForm  tr[class='row_even']  input[type=text]:nth-child(3)")
    SNTP_IP_ADDRESS_FOURTH=(By.CSS_SELECTOR,"#sntpcfgForm  tr[class='row_even']  input[type=text]:nth-child(4)")
    SNTP_UTC_COMBO_BOX=(By.NAME,"utc")
    SNTP_SUBMIT_BTN=(By.CSS_SELECTOR,"#sntpcfgForm input[type=submit]")
    SNTP_CONFIRM_PAGE_NTP_SUPPORT=(By.CSS_SELECTOR, "#contentIframe tr[class='row_odd']  span")
    SNTP_CONFIRM_PAGE_IPADDRESS=(By.CSS_SELECTOR, "#contentIframe tbody tr:nth-child(3) td:nth-child(2)")
    SNTP_CONFIRM_PAGE_UTC=(By.CSS_SELECTOR, "#contentIframe tbody tr:nth-child(4) td:nth-child(2)")
    SNTP_CURRENT_SETTING_IPADDRESS=(By.CSS_SELECTOR,"#sntpcfgForm tr:nth-child(3) td:nth-child(2)")
    SNTP_CURRENT_SETTING_UTC=(By.CSS_SELECTOR,"#sntpcfgForm tr:nth-child(4) td:nth-child(2)")
    SNTP_CURRENT_SETTING_STATE=(By.CSS_SELECTOR,"#sntpcfgForm > table > tbody > tr:nth-child(5) > td.sysvar > span")
    
    def __init__(self,driver_Browser):
        self.driver=driver_Browser
        
    def set_DefaultValues(self):
        self.click_NTP_Radio_On()
        self.set_NTP_IP_Address("0","0","0","0")
        self.select_UTC_Option("")
        self.click_Submit_option()
        
        self.driver.switch_to.default_content()
        self.click_SNTP_Menu()
        self.click_NTP_Radio_OFF()
        self.click_Submit_option()
        
    def close_Browser(self):
        self.driver.close()
        self.driver.quit()

    def verify_Settings(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(self.SNTP_CONFIRM_PAGE_NTP_SUPPORT))
        if (self.driver.find_element(*self.SNTP_CONFIRM_PAGE_NTP_SUPPORT).text == "on"):
            flag1= True
        else: 
            flag1= False
            
        if(self.driver.find_element(*self.SNTP_CONFIRM_PAGE_IPADDRESS).text== "192.168.0.5"):
            flag2= True
        else: 
            flag2= False
        if(self.driver.find_element(*self.SNTP_CONFIRM_PAGE_UTC).text== "UTC+5:30"):
            flag3= True
        else: 
            flag3= False
        self.driver.switch_to.default_content()
        self.driver.find_element(*self.SNTP_MENU).click()
        self.driver.switch_to.frame("center")
        wait.until(expected_conditions.visibility_of_element_located(self.SNTP_SUPPORT_RADIO_ON))
        if(self.driver.find_element(*self.SNTP_CURRENT_SETTING_IPADDRESS).text== "192.168.0.5"):
            flag4= True
        else: 
            flag4= False
        if(self.driver.find_element(*self.SNTP_CURRENT_SETTING_UTC).text== "UTC+5:30"):
            flag5= True
        else: 
            flag5= False
#         if(self.driver.find_element(*self.SNTP_CURRENT_SETTING_STATE).text== "synchronised"):
#             flag6= True
#         else: 
#             flag6= False
        #assert(flag1==True and flag2==True and flag3==True and flag4==True and flag5==True and flag6==True)
        assert(flag1==True and flag2==True and flag3==True and flag4==True and flag5==True)  
    
    def click_SNTP_Menu(self):
        self.driver.find_element(*self.SNTP_MENU).click()
        self.driver.switch_to.frame("center")
    
    def click_NTP_Radio_On(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of_element_located(self.SNTP_SUPPORT_RADIO_ON))
        self.driver.find_element(*self.SNTP_SUPPORT_RADIO_ON).click()
        
    def click_NTP_Radio_OFF(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of_element_located(self.SNTP_SUPPORT_RADIO_ON))
        self.driver.find_element(*self.SNTP_SUPPORT_RADIO_OFF).click()
        
    def select_UTC_Option(self,option):        
        Select(self.driver.find_element(*self.SNTP_UTC_COMBO_BOX)).select_by_value(option)
    
    def click_Submit_option(self):    
        self.driver.find_element(*self.SNTP_SUBMIT_BTN).click()
        #self.verify_Settings()
        
    def set_NTP_IP_Address(self,firstPartIP, secondPartIP, thirdPartIP,fourthPartIP):
        self.driver.find_element(*self.SNTP_IP_ADDRESS_FIRST).send_keys(firstPartIP)
        self.driver.find_element(*self.SNTP_IP_ADDRESS_SECOND).send_keys(secondPartIP)
        self.driver.find_element(*self.SNTP_IP_ADDRESS_THIRD).send_keys(thirdPartIP)
        self.driver.find_element(*self.SNTP_IP_ADDRESS_FOURTH).send_keys(fourthPartIP)
        