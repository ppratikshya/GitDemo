
from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop=(By.CSS_SELECTOR,'a[href*="shop"]')
    nameInput=(By.CSS_SELECTOR,'input[name="name"]')
    emailInput=(By.CSS_SELECTOR,'input[name="email"]')
    GenderInput=(By.CSS_SELECTOR,'select[id="exampleFormControlSelect1"]')
    Submit=(By.CSS_SELECTOR,'input[value="Submit"]')


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutpage = CheckoutPage(self.driver)
        return checkOutpage

    def nameInputMethod(self):
        return self.driver.find_element(*HomePage.nameInput)

    def emailInputMethod(self):
        return self.driver.find_element(*HomePage.emailInput)

    def genderInputMethod(self):
        return self.driver.find_element(*HomePage.GenderInput)

    def submitButton(self):
        return self.driver.find_element(*HomePage.Submit)