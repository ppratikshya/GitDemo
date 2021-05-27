import pytest

from testData import TestdataHomePage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_homepage(self, Getdata):
         homepage = HomePage(self.driver)
         homepage.nameInputMethod().send_keys(Getdata['firstname'])
         homepage.emailInputMethod().send_keys(Getdata['email'])
         homepage.genderInputMethod().send_keys(Getdata['gender'])
         homepage.submitButton().click()

    @pytest.fixture(params=TestdataHomePage.TestdataHomePage.testdatainput)
    def Getdata(self, request):
        return request.param







