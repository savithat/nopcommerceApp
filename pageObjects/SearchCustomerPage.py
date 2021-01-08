from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class searchCustomer():
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"

    table_xpath = " //*[@id='customers-grid']/tbody"
    tableRows_xpath = "//*[@id='customers-grid']/tbody/tr"
    tableColumns_xpath = "//*[@id='customers-grid']/tbody/tr/td"


    def __init__ (self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstName(self, first):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(first)

    def setLastName(self, last):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(last)

    def clickOnBtnSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def  searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag


    def  searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag





