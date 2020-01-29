from selenium import webdriver
from B08_Lib_FWDA import *

## Link 1:  https://www.fahasa.com
## Link 2:  https://www.w3schools.com/howto/howto_js_popup.asp 

def getValue(default, arrayMethods, msg=""):
    print('\n\n DANH SACH METHOD')
    for i in range(0, len(arrayMethods)):
        print(i, arrayMethods[i]['Title'])

    try:
        val = int(input(msg))
    except:
        val = default
    return val 

Firefox_options = webdriver.FirefoxOptions()
#prefs = {"profile.default_content_setting_values.notifications" : 2}
#Firefox_options.add_experimental_option("prefs",prefs)

driver = webdriver.Firefox(firefox_options=Firefox_options)
driver.get("https://tiki.vn/")

xulyPopup = Lib_FWDA(driver)

arrayMethods = {
    0 : {'Title' : 'Ket thuc !'},
    1 : {'Title' : 'Alert', 'Method' : xulyPopup.closeAlert},
    2 : {'Title' : 'IFrame', 'Method' : xulyPopup.getIframe},
    3 : {'Title' : 'Windows', 'Method' : xulyPopup.showWindowINFs}
}

opt = getValue(-1, arrayMethods, "\n\n ***************Chon lua cach thuc xu ly: ")

while (opt > 0):
    if (opt < len(arrayMethods)):
        arrayMethods[opt]['Method']()
    else:
        print(".........................")
    opt = getValue(-1, arrayMethods, "\n\n ***************Chon lua cach thuc xu ly: ")