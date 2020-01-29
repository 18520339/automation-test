from selenium import webdriver
import unittest

class test_WebUi(unittest.TestCase):
    def setUp(self):
        ## B1. WebDriver - WebBrowser
        self.driverWeb = webdriver.Firefox()
        self.driverWeb.get('https://www.fahasa.com')

    def test_Fahasha(self):
        ## B2. Var, Obj, TestData, ExpectedResult
        ExpectedResult = "98%"

        ## B3. Run - Script
        uiFlashSale = self.driverWeb.find_element_by_xpath("//div[@id='flashsale-slider']//li[1]")
        uiCompDiscount = uiFlashSale.find_element_by_xpath("//span[@class='p-sale-label discount-l-fs']")
        uiOldPrice = uiFlashSale.find_element_by_xpath("//div[@class='flashsale-price-old']")
        uiSpecialPrice = uiFlashSale.find_element_by_xpath("//div[@class='flashsale-price-special']")

        # Check
        ActualResult = uiCompDiscount.text
        print("Discount", uiCompDiscount.text)
        print("OldPrice", uiOldPrice.text)
        print("SpecialPrice", uiSpecialPrice.text)

        ## B4,5. Verify, Report
        self.assertEqual(ExpectedResult, ActualResult, "FAIL - !!!")

    def tearDown(self):
        ## B6. Reset
        self.driverWeb.close()

### Call Test "Auto"
if __name__ == '__main__':
    unittest.main(verbosity = 2) # verbosity = 2: Hien tung buoc