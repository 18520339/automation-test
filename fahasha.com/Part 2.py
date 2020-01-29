from selenium import webdriver
import time
import unittest

class test_WebUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ## B1. WebDriver - WebBrowser
        cls.driverWeb = webdriver.Firefox()

    def setUp(self):
        ## B1. Open WEB
        self.driverWeb.get("https://www.fahasa.com")

    def printAttributes(self, uiElement, attr, strShow):
        print(strShow, uiElement.get_attribute(attr))
    
    def getOneUi_FlashSale(self, uiFlashSale, xpath):
        '''
        uiComp_Discount = uiFlashSale.find_element_by_xpath(xpath + "//span[@class='p-sale-label discount-l-fs']")
        uiComp_OldPrice = uiFlashSale.find_element_by_xpath(xpath + "//div[@class='flashsale-price-old']")
        uiComp_SpecialPrice = uiFlashSale.find_element_by_xpath(xpath +  "//div[@class='flashsale-price-special']")
        '''

        uiComp_Discount = uiFlashSale.find_element_by_xpath( ".//span[@class='p-sale-label discount-l-fs']")
        uiComp_OldPrice = uiFlashSale.find_element_by_xpath(".//div[@class='flashsale-price-old']")
        uiComp_SpecialPrice = uiFlashSale.find_element_by_xpath( ".//div[@class='flashsale-price-special']")

        uiComp_Image = uiFlashSale.find_element_by_xpath( ".//img[@class='flashsale-item-image']")
        uiComp_Name = uiFlashSale.find_element_by_xpath( ".//h2[@class='product-name']//a")

        self.printAttributes(uiComp_Discount, "innerHTML", "Discount:")
        self.printAttributes(uiComp_OldPrice, "innerText", "OldPrice:")
        self.printAttributes(uiComp_SpecialPrice, "innerText", "SpecialPrice:")

        self.printAttributes(uiComp_Image, "currentSrc", "Image:")
        self.printAttributes(uiComp_Name, "innerText", "Name:")
        self.printAttributes(uiComp_Name, "href", "Link:")
        
    def test_Fahasa_FlashSale(self):
        time.sleep(5)
        driver = self.driverWeb

        for i in range(1, 11):
            time.sleep(1)
            xpath = "//div[@id='flashsale-slider']//li[" + str(i) + "]"
            uiFlashSale = driver.find_element_by_xpath(xpath)
            print("\n...Phan tu thu", i)
            self.getOneUi_FlashSale(uiFlashSale, xpath)

    def tearDown(self):  
        ## B6. RESET      
        ## self.driverWeb.close()
        print(" ..... Done !!!")
    
    @classmethod
    def tearDownClass(cls):
        cls.driverWeb.close()

### Call Test "Auto"
if __name__ == '__main__':
    unittest.main(verbosity=2)