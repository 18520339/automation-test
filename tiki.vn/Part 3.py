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
        self.driverWeb.get("https://tiki.vn/")

    def printAttributes(self, uiElement, attr, strShow):
        print("\n" , strShow, " Property " , attr, "[", uiElement.get_property(attr) , "]")
        print(" Attribute ", attr, "[", uiElement.get_attribute(attr) , "]")

    def printAllAttributes(self, uiElement, attrs, strShow):
        print("\n\n ****** " , strShow)
        for attr in attrs:
            print("\t", attr, "Property = [", uiElement.get_property(attr) , "]")
            print("\t", attr, "Attribute = [", uiElement.get_attribute(attr) , "]")
    
    def printEachElements(self, uiBlockElement, allUIs):
        for uikey in allUIs.keys():
            uiElement = uiBlockElement.find_element_by_xpath(allUIs[uikey]["xpath"])
            self.printAllAttributes(uiElement, allUIs[uikey]["Attributes"], uikey)

    def getOneUI_TikiDeal(self, uiBlockElement):
        allUIs = { 
            "Title" : {
                  "xpath": ".//p[@class='title']",
                  "Attributes": ["innerText", "text" , "innerHTML"] },

            "Discount" : {
                  "xpath": ".//span[@class='percent deal']",
                  "Attributes": ["innerText", "text"] },

            "Progress" : {
                  "xpath": ".//div[@class='percent']",
                  "Attributes": ["innerText", "text"] },

            "OldPrice" : {
                  "xpath": ".//span[@class='original deal']",
                  "Attributes": ["innerText", "text"] },

            "SpecialPrice" : {
                 "xpath": ".//p[@class='price']",
                 "Attributes": ["innerText", "text"] }
        }
        self.printEachElements(uiBlockElement, allUIs)

    def test_Tiki_Deal(self):
        time.sleep(5)
        driver = self.driverWeb
        for i in range(1,11):
            time.sleep(1)
            xxpath = "//div[@class='body']//a[" + str(i) + "]"
            uiFlashSale = driver.find_element_by_xpath(xxpath)
            print("\n\n ..... Phan tu thu ", i, "voi xpath = [", xxpath, "]")
            self.getOneUI_TikiDeal(uiFlashSale)

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