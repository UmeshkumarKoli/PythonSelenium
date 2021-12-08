import logging
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utils.commonFunctions import Util

@pytest.mark.DTE_COMMON

class Test_Home():
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

    def test_Home_Page(self,test_setUp):
        """Test_Home.test_Home_Page

        @DESCRIBE[[Test sequence:
        - verify [1] that how many language supports
        - verify [2] change language and check whether text are changing to respective language]]
        @TESTS[DTE10x-4660,DTE10x-4725]
        """
        wait=WebDriverWait(self.driver,10)
        self.driver.find_element_by_css_selector("#home > a").click()
        self.LOGGER.info('Clicked on Home menu')
        element=wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#select_language")))
        self.LOGGER.info('Home page language combo box is visible')
        sleep(1)
        element=self.driver.find_elements_by_css_selector("#select_language > option")
        countOfOptions= len(element)
        if (countOfOptions== 10):
            flag1=True
        else:
            flag1= False
        for language in range(10):
            Select(self.driver.find_element_by_id("select_language")).select_by_index(language)
            element=Select(self.driver.find_element_by_id("select_language")).first_selected_option
            self.LOGGER.info("Language %s = %s" %(language+1, element.text))
        Select(self.driver.find_element_by_id("select_language")).select_by_index(0)
        element=Select(self.driver.find_element_by_id("select_language")).first_selected_option
        if (element.text== "Deutsch | Deutsch"):
            flag2=True
        else:
            flag2= False
        
        assert(flag1==True and flag2== True)