'''
Created on Aug 22, 2019

@author: DTE_ADMIN
'''
import logging
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from Paths.ConstantPaths import ConstantPaths


class Util():
    
#     logging.basicConfig(
#         format='%(asctime)s.%(msecs)03d %(levelname)-2s %(message)s',
#         datefmt='%d.%m.%y %H:%M:%S')
    
    def init_Logger(self):
        self.LOGGER= logging.getLogger('LOG')
        self.LOGGER.setLevel(logging.INFO)
        return self.LOGGER
    
    def init_ChromeDriver(self):
        #self.driver=webdriver.Chrome("..\BrowserDriver\Chrome\chromedriver_76.exe")
        #path=os.getcwd()
        #self.driver=webdriver.Chrome("..\BrowserDriver\Chrome\chromedriver_76.exe")
        self.driver=webdriver.Chrome(ConstantPaths.ChromeDriverExePath)
        self.driver.maximize_window()
        #self.driver.get('http://192.168.0.79')
        return self.driver
    
    
    def init_IE_Driver(self):
        self.driver=webdriver.Ie(ConstantPaths.InternetExplorerDriverExePath)
        self.driver.maximize_window()
        self.driver.get('http://192.168.0.79')
        return self.driver