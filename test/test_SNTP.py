'''
Created on Sep 19, 2019

@author: DTE_ADMIN
'''
import pytest

from Pages.SNTP import SNTP_Settings
from Utils.commonFunctions import Util

@pytest.mark.DTE_COMMON

class Test_SNTP_Settings():

    @pytest.fixture()
    def test_setUp(self):
        #objects
        object_util=Util()
        self.driver=object_util.init_ChromeDriver()
        self.object_sntp=SNTP_Settings(self.driver)
        yield
        self.object_sntp.set_DefaultValues()
        self.object_sntp.close_Browser()
        
    def test_SNTP_Settings(self,test_setUp): 
        """Test_SNTP_Settings.test_SNTP_Settings

        @DESCRIBE[[Test sequence:
        - verify [1] that user should set NTP server address.]]
        @TESTS[DTE80x_DTE90x-1350]
        """       
        self.object_sntp.click_SNTP_Menu()
         
        self.object_sntp.click_NTP_Radio_On()
         
        #object_sntp.change_NTP_IP_Address()
        self.object_sntp.set_NTP_IP_Address("192", "168","0","5")
         
        self.object_sntp.select_UTC_Option("330")
        self.object_sntp.click_Submit_option()
         
        self.object_sntp.verify_Settings()