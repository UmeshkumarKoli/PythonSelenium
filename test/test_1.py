'''
Created on Mar 16, 2020

@author: inkolium
'''
import pytest
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup") 
class Test1():
    
    def test_1(self):      
        wait=WebDriverWait(self.driver,10)
        self.driver.get('http://www.ifm.com')
        