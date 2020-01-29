from UIForm_Fahasa import *
from selenium import webdriver

'''
//*[contains(@class,"menu")][contains(text(),"F-")]
//*[contains(@class,"menu") and contains(text(),"F-")]
//*[contains(@class,"menu") or contains(text(),"F-")]
//a[contains(text(),"Tài khoản") or contains(text(),"tài khoản")]
'''
class test_WebUI(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        ## B1. WebDriver - WebBrowser
        cls.driverWeb = webdriver.Firefox()

    def setUp(self):
        ## B1. Open WEB
        self.driverWeb.get("https://www.fahasa.com")
        
    def test_Fahasa_FlashSale(self):
        time.sleep(5)
        driver = UIForm_Fahasa(self.driverWeb)

        for i in range(1, random.randint(3, 5)):
            driver.ToiTrangNoiBat()
            driver.ChonMotSach()
            driver.ChonMua()

        driver.XemGioHang()

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