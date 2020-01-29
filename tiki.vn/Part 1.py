from selenium import webdriver

driver = webdriver.Firefox()

websites = {
    'https://tiki.vn/': ["//input[@placeholder='Tìm sản phẩm, danh mục hay thương hiệu mong muốn ...']",
                         "//button[@class='FormSearch__Button-hwmlek-3 dVzStw']",
                         "//input[@class='slide-input slide-from']",
                         "//input[@class='slide-input slide-to']",
                         "//button[@id='price-slider-submit']"],
}

product_name = 'Led tivi'
price_min = 30 * 10**6
price_max = 50 * 10**6

for web, elements in websites.items():
    driver.get(web)

    uiInput = driver.find_element_by_xpath(elements[0])
    uiSearch = driver.find_element_by_xpath(elements[1])

    uiInput.clear()
    uiInput.send_keys(product_name)
    uiSearch.click()

    uiPriceMin = driver.find_element_by_xpath(elements[2])
    uiPriceMax = driver.find_element_by_xpath(elements[3])
    uiFilter = driver.find_element_by_xpath(elements[4])

    uiPriceMin.clear()
    uiPriceMin.send_keys(price_min)
    uiPriceMax.clear()
    uiPriceMax.send_keys(price_max)
    uiFilter.click()
