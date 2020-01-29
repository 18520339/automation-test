from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class PO_Booking(object): 
    cSelectLanguage = [ By.XPATH, "//a[@id='b_tt_holder_3']"]
    cTiengViet = [ By.XPATH, "//div[@id='current_language_foldout']//div[2]//li[@class='lang_vi selected_country']"]

    cPlace = [ By.NAME, "ss"]

    cTime = [ By.XPATH, "//div[@class='xp__dates-inner']" ]
    cCheckIn = [ By.XPATH, "//div[@class='bui-calendar__content']/div[1]//td[normalize-space(.)='"]
    cCheckOut = [ By.XPATH, "//div[@class='bui-calendar__content']/div[2]//td[normalize-space(.)='"]

    cCheckInInfo = [ By.XPATH, "//div[@class='xp__dates-inner xp__dates__checkin']//div[contains(@class,'sb-date-field__display')]"]
    cCheckOutInfo = [ By.XPATH, "//div[@class='xp__dates-inner xp__dates__checkout']//div[contains(@class,'sb-date-field__display')]"]

    cQty = [ By.XPATH, "//div[@class='xp__input-group xp__guests']" ]
    cAdults = [ By.XPATH, "//span[@class='xp__guests__count']/span[1]" ]
    cChildren = [ By.XPATH, "//span[@class='xp__guests__count']/span[2]" ]
    cRooms = [ By.XPATH, "//span[@class='xp__guests__count']/span[3]" ]

    cAdultInfo = [ By.XPATH, "//div[@class='sb-group__field sb-group__field-adults']//span[@class='bui-stepper__display']" ]
    cChildernInfo = [ By.XPATH, "//div[@class='sb-group__field sb-group-children ']//span[@class='bui-stepper__display']" ]
    cRoomInfo = [ By.XPATH, "//div[@class='sb-group__field sb-group__field-rooms']//span[@class='bui-stepper__display']" ]

    btnSearch = [ By.CLASS_NAME, "sb-searchbox__button" ]

    def __init__(self, driver, baseURL=""):
        self.driver = driver
        if (baseURL != ""):
            self.baseURL = baseURL
            driver.get(self.baseURL)
        else:
            self.baseURL = driver.current_url

    def set_Place(self, vPlace):
        uiPlace = self.driver.find_element(self.cPlace[0], self.cPlace[1])        
        uiPlace.clear()
        uiPlace.send_keys(vPlace)

    def set_Time(self, vCheckIn, vCheckOut):
        self.driver.find_element(self.cTime[0], self.cTime[1]).click()
        self.driver.find_element(self.cCheckIn[0], self.cCheckIn[1] + vCheckIn + "']").click()
        self.driver.find_element(self.cCheckOut[0], self.cCheckOut[1] + vCheckOut + "']").click()

    def set_Qty(self):
        self.driver.find_element(self.cQty[0], self.cQty[1]).click()
        self.driver.find_element(self.cAdults[0], self.cAdults[1]).click()
        self.driver.find_element(self.cChildren[0], self.cChildren[1]).click()
        self.driver.find_element(self.cRooms[0], self.cRooms[1]).click()

    def get_Info(self):
        placeInfo = self.driver.find_element(self.cPlace[0], self.cPlace[1])
        placeInfo.get_property("value")
        
        uiCheckIninfo = self.driver.find_element(self.cCheckInInfo[0], self.cCheckInInfo[1])
        uiCheckIninfo.get_property("innerText")

        uiCheckOutinfo = self.driver.find_element(self.cCheckOutInfo[0], self.cCheckOutInfo[1])
        uiCheckOutinfo.get_property("innerText")

        uiAdults = self.driver.find_element(self.cAdults[0], self.cAdults[1])
        uiAdults.get_property("innerText")

        uiChildren = self.driver.find_element(self.cChildren[0], self.cChildren[1])
        uiChildren.get_property("innerText")

        uiRooms = self.driver.find_element(self.cRooms[0], self.cRooms[1])
        uiRooms.get_property("innerText")

    def click_submit(self):
        self.driver.find_element(self.btnSearch[0], self.btnSearch[1]).click()

    def do_action(self, vPlace, vCheckIn, vCheckOut):
        self.set_Place(vPlace) 
        self.set_Time(vCheckIn, vCheckOut)
        self.set_Qty()   
        self.get_Info()
        self.click_submit() 

    def verify(self):
        try:
            assert 'index.vi.html' in self.driver.current_url   
        except AssertionError:
            self.driver.find_element(self.cSelectLanguage[0], self.cSelectLanguage[1]).click()
            self.driver.find_element(self.cTiengViet[0], self.cTiengViet[1]).click()    