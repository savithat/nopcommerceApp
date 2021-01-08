import pytest
import time
from pageObjects.LoginPage import Login
from pageObjects.AddcustomerPage import AddCustomer
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
        time.sleep(5)
        self.addcustomer.clickonAddnewBtn()
        time.sleep(5)
        self.logger.info("**********providing customer info*********")
        self.email = random_generator() + "@gmail.com"
        self.addcustomer.setEmail(self.email)
        self.addcustomer.setPassword("savitha")
        self.addcustomer.setFirstName("savitha")
        self.addcustomer.setLastName("Thippur")
        self.addcustomer.setGender("Female")
        self.addcustomer.setDob("04/05/2009")
        self.addcustomer.setCompanyname("info")
        self.addcustomer.setCustomerrole("Forum Moderators")
        self.addcustomer.setManagerOfVendor("Not a vendor")
        self.addcustomer.setAdminContent("This is addcustomer testing")
        self.logger.info("**********Ended customer info*********")

        self.addcustomer.clickOnSave()
        self.logger.info("**********Save customer info*********")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'The new customer has been added successfully' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.logger.error("********* Add customer validation tested************")



        time.sleep(5)
        self.driver.close()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

