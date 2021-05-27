from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver=driver

    countryInput = (By.ID,'country')
    CheckBox=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
    Purchase=(By.XPATH,"//input[@type='submit']")
    successtext="Success! Thank you! Your order will be delivered in next few weeks :-)."



    def countryInputClick(self,text):
        self.driver.find_element(*ConfirmPage.countryInput).send_keys(text)

    def CheckboxClick(self):
        return self.driver.find_element(*ConfirmPage.CheckBox)

    def Purchaseclick(self):
        self.driver.find_element(*ConfirmPage.Purchase).click()



