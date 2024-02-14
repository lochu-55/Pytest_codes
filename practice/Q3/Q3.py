from selenium import webdriver
import pytest

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.select import Select

class webapp:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.automationtesting.in/Register.html")
        self.driver.maximize_window()
        self.logger = logging.getLogger(__name__)
        self.fh = logging.FileHandler("Q3/webapp3.log", mode='w')
        self.frmt = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s")
        self.fh.setFormatter(self.frmt)
        self.logger.addHandler(self.fh)
        self.logger.setLevel(logging.DEBUG)

    def enter_firstname(self):
        self.logger.info("entering first name...")
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("lochani")
        sleep(2)

    def is_firstname_entered(self):
        self.logger.info("checking first name...")
        result = self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        if result.get_attribute("value") != None:
            return True
        else:
            return False

    def enter_lastname(self):
        self.logger.info("entering last name...")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("vilehya")
        sleep(2)

    def is_lastname_entered(self):
        self.logger.info("checking last name...")
        result = self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        if result.get_attribute("value") != None:
            return True
        else:
            return False

    def radio_button(self):
        self.logger.info("selecting gender....")
        self.driver.find_element(By.XPATH, "//input[@value='FeMale']").click()
        sleep(2)

    def check_radiobtn(self):
        self.logger.info("checking the gender radio button...")
        res = self.driver.find_element(By.XPATH, "//input[@value='FeMale']")
        if res.is_selected():
            return True
        else:
            return False

    def check_box(self):
        self.logger.info("obtaining list of checkbox inputs...")
        l = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        for link in l:
            if link.get_attribute("value") == "Movies":
                link.click()

    def check_checkbox(self):
        self.logger.info("checking the hobbies check boxes....")
        res = self.driver.find_element(By.XPATH, "//input[@value='Movies']")
        if res.is_selected():
            return True
        else:
            return False

    def drop_down(self):
        self.logger.info("drop down box is enabled...")
        self.select_web = self.driver.find_element(By.ID, "Skills")
        sel = Select(self.select_web)
        sel.select_by_visible_text("AutoCAD")
        sleep(3)

    def check_dropdown(self):
        self.logger.debug("checking drop down box...")
        opt = self.driver.find_element(By.ID, "Skills")
        # sel = Select(opt)
        if opt.is_displayed() != None:
            return True
        else:
            return False

        ''' list1 = sel.all_selected_options
        for i in list1:
            if i.text == "AutoCAD":
                return True
            else:
                return False'''

    def refresh_button(self):
        self.logger.error("warning:refreshing the page....")
        self.driver.find_element(By.ID, "Button1").click()
        sleep(3)

    def check_refreshbtn(self):
        res = self.driver.find_element(By.ID, "Button1")
        if res.is_enabled():
            return True
        else:
            return False

    def open_newlink(self):
        self.driver.get("https://www.google.co.in/")
        self.driver.back()
        sleep(2)
        self.driver.refresh()
        sleep(2)
        self.driver.forward()
        sleep(3)
