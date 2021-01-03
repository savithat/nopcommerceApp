import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import logGen




class Test_001:
    Url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserename()
    Password = ReadConfig.getPassword()

    logger = logGen.loggen()


    def test_HomepageTitle(self, setup):

        self.logger.info("*******Test_001************")
        self.logger.info("**********verify HomepageTitle started*********")
        self.driver = setup
        self.driver.get(self.Url)
        self.driver.maximize_window()
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("**********verified HomepageTitle*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomepageTitle.png")
            self.driver.close()
            self.logger.error("********** HomepageTitle failed*********")
            assert False





    def test_login(self, setup):

        self.logger.info("*******Test_001************")
        self.logger.info("**********verify test_login started*********")
        self.driver = setup
        self.driver.get(self.Url)
        self.driver.maximize_window()

        self.dl = Login(self.driver)
        self.dl.setUserName(self.username)
        self.dl.setPassword(self.Password)
        self.dl.clickLogin()
        act_title = self.driver.title


        if act_title == "Dashboard / nopCommerce administration":
            self.dl.clickLogout()
            self.driver.close()
            assert True
            self.logger.info("**********verified loggedin*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.dl.clickLogout()
            self.driver.close()
            self.logger.error("**********failed loggedin*********")
            assert False







