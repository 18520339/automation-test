from selenium import webdriver 
import pytest 
import os
from CSV_TestData import CSVTestData
from POM.PO_Booking import PO_Booking 

## Data
dta = CSVTestData(os.getcwd() + '\\booking_TCs.csv')
tcdata = dta.TData["Data"]["raw"]

## Test CLASS
class Test_ActionPy_Booking:
    countCLS = 0

    @classmethod
    def setup_class(cls):
        cls.baseurl = 'https://www.booking.com/'
        cls.firefoxfile = os.getcwd() + "\\geckodriver.exe"
        cls.browser = webdriver.Firefox() #cls.chromefile)

    def setup_method(self, method):
        Test_ActionPy_Booking.countCLS += 1
        self.browser.get(self.baseurl)

    @pytest.mark.parametrize("vPlace, vCheckIn, vCheckOut", tcdata)
    def test_Home(self, vPlace, vCheckIn, vCheckOut):
        xbooking = PO_Booking(self.browser)
        xbooking.do_action(vPlace, vCheckIn, vCheckOut)
        xbooking.verify()

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()