'''
Created on Mar 16, 2020

@author: inkolium
'''
import pytest
from selenium import webdriver

from Paths.ConstantPaths import ConstantPaths


@pytest.fixture(scope="session")
def setup(request):
    #self.driver=webdriver.Chrome("..\BrowserDriver\Chrome\chromedriver_76.exe")
    #path=os.getcwd()
    #self.driver=webdriver.Chrome("..\BrowserDriver\Chrome\chromedriver_76.exe")
    driver=webdriver.Chrome(ConstantPaths.ChromeDriverExePath)
    driver.maximize_window()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver",driver)
    
    yield 
    driver.close() 