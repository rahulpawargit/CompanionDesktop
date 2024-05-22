import time

import pytest
from selenium import webdriver
from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_Homepage_Verify:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationpassword()
    logger = LogGen.loggen()

    # def test_verify_elements(self, setup):
    #     self.logger.info("***********Test002_Homepage_Loge******")
    #     self.driver= setup
    #     self.driver.get(self.baseURL)
    #     self.lp= Login(self.driver)
    #     self.lp.setUsername(self.username)
    #     self.lp.click_privacyPolicy()
    #     time.sleep(3)
    #     self.lp.click_Nextnbutton()
    #     time.sleep(3)
    #     self.lp.setPassword(self.password)
    #     time.sleep(1)
    #     self.lp.click_Loginbutton()
    #     time.sleep(3)
    #     self.logger.info("************Login Successfull**********")
    #     self.hp= HomePage(self.driver)
    #     self.hp.click_alert()
    #     # lname = self.hp.verify_locationname()
    #     # assert  True == lname
    #     # lname= self.hp.verify_locationname()
    #     # if lname == "Rishon LeZion":
    #     #     assert True
    #     # else:
    #     #     assert False
    #
    #     # assert self.hp.verify_locationname()
    #     # self.driver.close()
    @pytest.mark.regression
    def test_calendar(self, setup):
        self.logger.info("***********Test002_Homepage_Loge******")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp= Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.click_privacyPolicy()
        time.sleep(3)
        self.lp.click_Nextnbutton()
        time.sleep(3)
        self.lp.setPassword(self.password)
        time.sleep(1)
        self.lp.click_Loginbutton()
        self.logger.info("************Login Successfull**********")
        self.hp= HomePage(self.driver)
        self.hp.click_on_Calendar()
        self.driver.close()

    @pytest.mark.regression
    def test_Floomap(self, setup):
        self.logger.info("***********Test002_Homepage_Loge******")
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
        self.logger.info("************Login Successfull**********")
        self.hp = HomePage(self.driver)
        self.hp.click_on_Floomap()
        self.driver.close()

    @pytest.mark.sanity
    def test_Visitor(self, setup):
        self.logger.info("***********Test002_Homepage_Loge******")
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
        self.logger.info("************Login Successfull**********")
        self.hp = HomePage(self.driver)
        self.hp.click_on_visitor()
        self.driver.close()

    @pytest.mark.sanity
    def test_News(self, setup):
        self.logger.info("***********Test002_Homepage_Loge******")
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
        self.logger.info("************Login Successfull**********")
        self.hp = HomePage(self.driver)
        self.hp.click_on_news()
        self.driver.close()

    def test_workorder(self, setup):
        self.logger.info("***********Test002_Homepage_Loge******")
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
        self.logger.info("************Login Successfull**********")
        self.hp = HomePage(self.driver)
        self.hp.click_on_workorder()
        time.sleep(3)
        act_url= self.hp.driver.current_url
        print(act_url)
        if act_url== "https://obcpneustg-desktopui.obcompanion.cloud/#/workorder":
            self.logger.info("**********Login Test Case Passed**************")
            time.sleep(3)
            self.lp.click_logout()
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            # self.lp.click_logout()
            self.driver.close()
            self.logger.info("**********Login Test Case Failed**************")
            assert False

    def test_Cafeteria(self, setup):
        self.logger.info("***********Test002_Homepage_Loge******")
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
        self.logger.info("************Login Successfull**********")
        self.hp = HomePage(self.driver)
        flag = self.hp.Verify_cafeteria()
        if flag == True:
            self.logger.info("**********Login Test Case Passed**************")
            time.sleep(3)
            self.lp.click_logout()
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            # self.lp.click_logout()
            self.driver.close()
            self.logger.info("**********Login Test Case Failed**************")















