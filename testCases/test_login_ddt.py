import time

from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_0012_DataDriver_Login:
    #Hardcoded values
    # baseURL = "https://obcpneustg-desktopui.obcompanion.cloud/"
    # username = "rahul@dbk.com"
    # password = "Jci12!@"

    #Dynamic values, calling from config.ini file
    baseURL= ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    # username = ReadConfig.getApplicationUsername()
    # password = ReadConfig.getApplicationpassword()
    logger =LogGen.loggen()

    @pytest.mark.regression
    def test_loginPagetitle(self, setup):
        # option = webdriver.ChromeOptions()
        # self.option.add_experimental_option("detach", True)
        self.logger.info("************** Test_002_DDT_Login*************")
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

    @pytest.mark.regression
    def test_login(self, setup):
        # option = webdriver.ChromeOptions()
        # self.option.add_experimental_option("detach", True)
        self.logger.info("************** Verify Login*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("No of rows", self.rows)

        lst_status=[]  #Empty list created
        for r in range(2, self.rows +1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUsername(self.user)
        #   self.lp.setUsername(self.username)
            self.lp.click_privacyPolicy()
            time.sleep(3)
            self.lp.click_Nextnbutton()
            time.sleep(3)
            self.lp.setPassword(self.password)
        #   self.lp.setPassword(self.password)
            time.sleep(1)
            self.lp.click_Loginbutton()
            act_title= self.lp.driver.title
            exp_title ="OpenBlue Companion"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("****Test is Passed******")
                    # self.lp.click_logout()
                    lst_status.append("Pass")
                    self.driver.close()
                elif self.exp=="Fail":
                    self.logger.info("****Test is Failed******")
                    # self.lp.click_logout()
                    lst_status.append("Fail")
                    self.driver.close()
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("****Test is Fail******")
                #   self.lp.click_Loginbutton()
                    lst_status.append("Fail")
                    self.driver.close()

                elif self.exp=="Fail":
                    self.logger.info("****Test is Passed******")
                    time.sleep(3)
                    self.lp.click_logout()
                    lst_status.append("Pass")
                    self.driver.close()

            if "Fail" not in lst_status:
                self.logger.info("Login DDT test Passed")
                self.driver.close()
                assert True
            else:
                self.logger.info("Login DDT test Failed")
                self.driver.close()
                assert False

        self.logger.info("########End of Test Cases###########")


