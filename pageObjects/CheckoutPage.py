from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self,driver):
        self.driver=driver

    cardTitle=(By.CSS_SELECTOR,'.card-title a')
    cardFooter=(By.CSS_SELECTOR,'.card-footer button')
    checkOut=(By.CSS_SELECTOR,"a[class*='btn-primary']") #"a[class*='btn-primary']"
    #checkOut=(By.XPATH,"//a[@class,'btn btn-primary']")
    checkOutlast=(By.CSS_SELECTOR,"button[class*='btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkOutItems(self):
        return self.driver.find_element(*CheckoutPage.checkOut)

    def checkOutItemslast(self):
        self.driver.find_element(*CheckoutPage.checkOutlast).click()
        lastcheckout = ConfirmPage(self.driver)
        return lastcheckout
