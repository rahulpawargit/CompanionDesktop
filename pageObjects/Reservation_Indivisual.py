import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Reservation_Indivisual:

    schedule_button_xpath = "//u[normalize-space()='Schedule']"
    reservation_button_xpath = "//li[@id='Individual-Reservation']"
    space_typer_xpath = "//div[@id='mat-select-value-7']"
    select_location_xpath = "//span[@class='mat-option-text'][normalize-space()='Rishon LeZion, Building D, Floor 2']"
    start_time_xpath = "//input[@id='mat-input-0']"
