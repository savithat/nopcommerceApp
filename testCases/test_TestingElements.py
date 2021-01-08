from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

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

lnk_Customers_menu_xpath = "//a[@href = '#']/span[contains(text(), 'Customers')]"
driver.find_element_by_xpath(lnk_Customers_menu_xpath).click()

lnk_Customers_xpath = "//ul[@class='sidebar-menu tree']/li[4]/ul/li[1]/a"
driver.find_element_by_xpath(lnk_Customers_xpath).click()
time.sleep(5)
txtEmail_id = "SearchEmail"
txtFirstName_id = "SearchFirstName"
txtLastName_id = "SearchLastName"
btnSearch_id = "search-customers"

table_xpath = " //*[@id='customers-grid']/tbody"
tableRows_xpath = "//*[@id='customers-grid']/tbody/tr"
tableColumns_xpath = "//*[@id='customers-grid']/tbody/tr/td"

driver.find_element_by_id(txtEmail_id).clear()
driver.find_element_by_id(txtEmail_id).send_keys("victoria_victoria@nopCommerce.com")

driver.find_element_by_id(txtFirstName_id).clear()
driver.find_element_by_id(txtFirstName_id).send_keys("Victoria ")

driver.find_element_by_id(txtLastName_id).clear()
driver.find_element_by_id(txtLastName_id).send_keys("Terces")


row = driver.find_elements_by_xpath(tableRows_xpath)

#col = len(driver.find_elements_by_xpath(tableColumns_xpath))

print("row=", len(row))
#print("column", col)

driver.find_element_by_id(btnSearch_id).click()
time.sleep(5)
driver.close()



