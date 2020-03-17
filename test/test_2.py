'''
Created on Mar 16, 2020

@author: inkolium
'''
import pytest
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup") 
class Test2():
    @pytest.mark.usefixtures("resource_1_teardown") 
    def test_2(self):      
        wait=WebDriverWait(self.driver,10)
        self.driver.get('http://www.google.co.in')
        print "test2
