from selenium import webdriver
import time, random
import unittest

class UIForm_Fahasa:
    def __init__(self, webDriver):
        self.webDriver = webDriver

    def ToiTrangNoiBat(self):
        self.webDriver.get("https://www.fahasa.com/sach-trong-nuoc/sort-by/num_orders/sort-direction/asc.html?attempt=1")
        print("\n.. toi Trang Noi Bat")

    def printAllAttributes(self, uiElement, attrs, strShow):
        print("\n\n ****** " , strShow)
        for attr in attrs:
            print("\t", attr, "Property = [", uiElement.get_property(attr) , "]")
            print("\t", attr, "Attribute = [", uiElement.get_attribute(attr) , "]")
    
    def printEachElements(self, uiBlockElement, allUIs):
        for uikey in allUIs.keys():
            uiElement = uiBlockElement.find_element_by_xpath(allUIs[uikey]["xpath"])
            self.printAllAttributes(uiElement, allUIs[uikey]["Attributes"], uikey)

    def ChonMotSach(self):
        print("\n.. Chon 1 sach ")
        i = random.randint(1, 20)
        xpath = "//ul[@class='products-grid row fhs-top']/li[" + str(i) + "]"
        uiBooki = self.webDriver.find_element_by_xpath(xpath)

        allUIs = { 
            "Discount" : {
                  "xpath": ".//span[@class='p-sale-label']",
                  "Attributes": ["innerText"] },

            "BookName" : {
                  "xpath": ".//h2/a",
                  "Attributes": ["innerText"] },

            "Price" : {
                  "xpath": ".//span[@class='price']",
                  "Attributes": ["innerText"] },
        }

        self.printEachElements(uiBooki, allUIs)
        uiBooki.click()

    def ChonMua(self):
        print("\n.. Chon mua ")

        xpath = "//i[@class='fa fa-shopping-cart']"
        uiMuaButton = self.webDriver.find_element_by_xpath(xpath)
        uiSoLuong = self.webDriver.find_element_by_xpath("//input[@id='qty']")
        uiSoLuong.clear()
        uiSoLuong.send_keys("2")
        uiMuaButton.click()

        time.sleep(5)
        uiChonThem = self.webDriver.find_element_by_xpath("//a[@id='continue_shopping']")
        uiChonThem.click()

    def XemGioHang(self):
        xpath = "//div[@class='cart-total']"
        uiXemGioHangBtn = self.webDriver.find_element_by_xpath(xpath)
        uiXemGioHangBtn.click()