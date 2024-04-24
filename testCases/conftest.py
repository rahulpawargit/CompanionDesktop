from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'IE':
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=option)
        print("Launching Chrome Browser")
        driver.maximize_window()
        driver.implicitly_wait(30)

    elif browser =='Edge':
        option = webdriver.EdgeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=option)
        print("Launching Edge Browser")
        driver.maximize_window()
        driver.implicitly_wait(30)
    else:
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=option)
        print("Launching Chrome Browser")
        driver.maximize_window()
        driver.implicitly_wait(30)



    return driver


def pytest_addoption(parser):  #This will get the value form CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):    #This will return the browser value to setup
    return request.config.getoption("--browser")