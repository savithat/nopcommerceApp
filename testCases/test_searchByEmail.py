import pytest
import time
from pageObjects.LoginPage import Login
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import searchCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import logGen
import string
import random


class Test_003_Addcustomer:
    Url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserename()
    Password = ReadConfig.getPassword()

    logger = logGen.loggen()


    def test_addcustomer(self, setup):

        self.logger.info("*******Test_003************")
        self.driver = setup
        self.driver.get(self.Url)
        self.driver.maximize_window()

        self.dl = Login(self.driver)
        self.dl.setUserName(self.username)
        self.dl.setPassword(self.Password)
        self.dl.clickLogin()
        self.logger.info("*******Login succesfull************")
        self.logger.info("**********started adding  customer info*********")
        self.addcustomer = AddCustomer(self.driver)
        self.addcustomer.clickonCustomersMenu()
        self.addcustomer.clickonCustomersMenuItem()

        self.searchcust = searchCustomer(self.driver)
        self.searchcust.setEmail("victoria_victoria@nopCommerce.com")
        self.searchcust.clickOnBtnSearch()

        time.sleep(5)
        status = self.searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status

        time.sleep(5)





        self.driver.close()