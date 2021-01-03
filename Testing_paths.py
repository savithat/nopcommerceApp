from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
user = driver.find_element_by_id("Email")
user.clear()
user.send_keys("admin@yourstore.com")

passwd = driver.find_element_by_id("Password")
passwd.clear()
passwd.send_keys("admin")

click_butt = driver.find_element_by_xpath("//input[@class='button-1 login-button']")
click_butt.click()

title = driver.title
if title == "Dashboard / nopCommerce administration":
    assert True
else:
    assert  False
driver.close()