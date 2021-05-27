import pytest
from selenium import webdriver
import time
import selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pageObjects
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from utilities.BaseClass import BaseClass
from pageObjects import ConfirmPage


class Testone(BaseClass):

    def test_e2e(self):
        homepage=HomePage(self.driver)
        checkOutpage= homepage.shopItems()
        cards=checkOutpage.getCardTitle()
        i=-1
        for card in cards:
            i=i+1
            cardtext = card.text
            print(cardtext)
            if cardtext == 'Blackberry':
                checkOutpage.getCardFooter()[i].click()
        checkOutpage.checkOutItems().click()
        lastcheckout=checkOutpage.checkOutItemslast()
        lastcheckout.countryInputClick('ind')
        element =self.verifyLinkPresensce('India')
        element.click()
        lastcheckout.CheckboxClick().click()
        lastcheckout.Purchaseclick()
        assert 'Success' in ConfirmPage.ConfirmPage.successtext
        time.sleep(5)






