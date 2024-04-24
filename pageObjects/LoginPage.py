from selenium.webdriver.common.by import By



class Login:
    username_textbox_xpath= "//input[@placeholder='Username']"
    privacy_policy_checkbox_xpath = "//input[@id='terms-of-use']"
    nextbutton_xpath= "//button[normalize-space()='Next']"
    password_textbox_xpath= "//input[@placeholder='Enter password']"
    login_button_xpath = "//button[normalize-space()='Login']"
    logout_button_xpath = "(//li[@id='logout'])[1]"


    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        # self.driver.find_element(By.XPATH, self.username_textbox_xpath).click()
        # self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def click_privacyPolicy(self):
        self.driver.find_element(By.XPATH, self.privacy_policy_checkbox_xpath).click()

    def click_Nextnbutton(self):
        self.driver.find_element(By.XPATH, self.nextbutton_xpath).click()

    def setPassword(self, password):
        # self.driver.find_element(By.XPATH, self.username_textbox_xpath).click()
        # self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def click_Loginbutton(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()