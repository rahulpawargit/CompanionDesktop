import time

from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    #Hardcoded values
    # baseURL = "https://obcpneustg-desktopui.obcompanion.cloud/"
    # username = "rahul@dbk.com"
    # password = "Jci12!@"

    #Dynamic values, calling from config.ini file
    baseURL= ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationpassword()
    logger =LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginPagetitle(self, setup):
        # option = webdriver.ChromeOptions()
        # self.option.add_experimental_option("detach", True)
        self.logger.info("************** Test_001_Login*************")
        self.logger.info("**************Verify Homepage Title *********")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title= self.driver.title
        self.driver.close()
        if act_title=="OpenBlue Companion":
            self.logger.info("**********HomePage Title Test Case Passed**************")
            assert True

        else:
            self.logger.info("**********HomePage Title Test Case Failed**************")
            assert False

    @pytest.mark.sanity
    def test_login(self, setup):
        # option = webdriver.ChromeOptions()
        # self.option.add_experimental_option("detach", True)
        self.logger.info("************** Verify Login*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.click_privacyPolicy()
        time.sleep(3)
        self.lp.click_Nextnbutton()
        time.sleep(3)
        self.lp.setPassword(self.password)
        time.sleep(1)
        self.lp.click_Loginbutton()
        # time.sleep(3)
        act_title= self.lp.driver.title
        if act_title =="OpenBlue Companion":
            self.logger.info("**********Login Test Case Passed**************")
            time.sleep(3)
            self.lp.click_logout()
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            # self.lp.click_logout()
            self.driver.close()
            self.logger.info("**********Login Test Case Failed**************")
            assert False