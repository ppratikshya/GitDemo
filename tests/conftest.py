import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="my option: type1 or type2")

@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name=='chrome':
        driver = webdriver.Chrome(r"C:\Users\PPRATIKS\Downloads\Selenium_Driver_Jars\chromedriver.exe")
    elif browser_name=='firefox':
        driver = webdriver.Firefox(r"C:\Users\PPRATIKS\Downloads\Selenium_Driver_Jars\geckodriver.exe")
    elif browser_name=='ie':
        driver = webdriver.Ie(r"C:\Users\PPRATIKS\Downloads\Selenium_Driver_Jars\IEDriverServer.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()




