import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

from tests import conftest


@pytest.mark.usefixtures('setup')
class BaseClass:

    def verifyLinkPresensce(self,text):

        element=WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.LINK_TEXT, text)))
        return element

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
