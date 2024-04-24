import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    Location_Name_xpath = "//label[normalize-space()='Rishon LeZion']",
    Logo_xpaht = "//img[@alt='D Campus']",
    SOS_xpath = "//div[@class='parent_sos_div_desktop margin-right-10 ng-star-inserted']//*[name()='svg']",
    Logout_button_xpath = "//a[normalize-space()='Logout']",
    Calendar_link_xpaht = "//div[@class='textwrap'][normalize-space()='Calendar']"
    Alert_button_xpath = "//div[@class='notifications-icon-wrapper']//*[name()='svg']"
    Floor_map_xpath = "//li[@id='Floor Map']//a[@class='disp-inline']"
    Workorder_xpath = "//div[contains(text(),'Work Order')]"
    Visitor_xpath = "//div[contains(text(),'My Visitors')]"
    Newx_xpaht= "//div[@class='textwrap'][normalize-space()='News']"

    def __init__(self, driver):
        self.driver = driver

    # def verify_Logo(self, logo):
    #     # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(By.XPATH, self.Logo_xpaht))
    #     flag = False
    #     flag = self.driver.find_element(By.XPATH, self.Logo_xpaht).is_displayed(locator)
    #     return flag

    def verify_locationname(self):
        flag = False
        locator = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(By.XPATH, self.Location_Name_xpath))
        locationname = locator.text
        if locationname !=" ":
            flag = True
        return flag

    def click_on_Calendar(self):
        self.driver.find_element(By.XPATH, self.Calendar_link_xpaht).click()
    def click_on_Floomap(self):
        self.driver.find_element(By.XPATH, self.Floor_map_xpath).click()
    def click_on_workorder(self):
        self.driver.find_element(By.XPATH, self.Workorder_xpath).click()
    def click_on_visitor(self):
        self.driver.find_element(By.XPATH, self.Visitor_xpath).click()
    def click_on_news(self):
        self.driver.find_element(By.XPATH, self.Newx_xpaht).click()



        # time.sleep(1)
        # return self.driver.current_url


    def click_alert(self):
        self.driver.find_element(By.XPATH, self.Alert_button_xpath).click()
