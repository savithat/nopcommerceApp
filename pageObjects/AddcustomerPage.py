from selenium.webdriver.support.ui import Select
import time

class AddCustomer():
    #Add customer page
    lnk_Customers_menu_xpath = "//a[@href = '#']/span[contains(text(), 'Customers')]"
    lnk_Customers_menuitem_xpath = "//ul[@class = 'treeview-menu']/li/a[@href = '/Admin/Customer/List']"
    btnAddnew_xpath = "//a[@class ='btn bg-blue']"

    txtEmail_xpath = "//*[@id='Email']"
    txtPassword_xpath = "//*[@id='Password']"
    txtFirstName_xpath = "//*[@id='FirstName']"
    txtLastName_xpath ="//*[@id='LastName']"
    rdMalegender_id = "Gender_Male"
    rdFemalegender_id ="Gender_Female"
    txtDOB_xpath = "//*[@id='DateOfBirth']"
    txtCompanyname_xpath = "//*[@id='Company']"
    chkbobTaxexempt_xpath = "//*[@id='IsTaxExempt']"
    txtlstNewsletter_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div/div[1]/div"
    txtlsFirsttoption = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    txtlsSecondtoption = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"
    txtCustomerrole_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/div"
    txtCustomerroleDel_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"
    txtCustomerroleAdmin_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    txtCustomerroleFoemod_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    txtCustomerroleGuests_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    txtCustomerroleReg_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    txtCustomerroleVendors_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    DrpdnManagervender_xpath = "//*[@id='VendorId']"
    ChkboxActive_xpath = "//input[@id = 'Active']"
    TxtareaAdmincomment_xpath = "//*[@id='AdminComment']"
    btnSave_xpath = "//button[@name = 'save']"


    def __init__(self, driver):
        self.driver = driver

    def clickonCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnk_Customers_menu_xpath).click()

    def clickonCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnk_Customers_menuitem_xpath).click()

    def clickonAddnewBtn(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setGender (self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdMalegender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdFemalegender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMalegender_id).click()

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDOB_xpath ).send_keys(dob)

    def setCompanyname(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyname_xpath).send_keys(comname)

  #  def selectNewsletter(self, name):
   #     sefl.driver.find_element_by_xpath(self.txtlstNewsletter_xpath)

    def setCustomerrole(self, role):
        self.driver.find_element_by_xpath(self.txtCustomerrole_xpath).click()
        time.sleep(2)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.txtCustomerroleReg_xpath )
        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.txtCustomerroleAdmin_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element_by_xpath(self.txtCustomerroleFoemod_xpath)
        elif role == "Guests":
            self.driver.find_element_by_xpath(self.txtCustomerroleDel_xpath).click()
            self.listitem = self.driver.find_element_by_xpath(self.txtCustomerroleGuests_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.txtCustomerroleVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.txtCustomerroleGuests_xpath )
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.DrpdnManagervender_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
         self.driver.find_element_by_xpath(self.TxtareaAdmincomment_xpath).send_keys(content)

    def clickOnSave(self):
       self.driver.find_element_by_xpath(self.btnSave_xpath).click()












