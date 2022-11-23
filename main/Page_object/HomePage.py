from selenium.webdriver.common.by import By

from main.utilities.Baseclass import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    profile_name = (By.XPATH, "(//span[@dir='auto'][normalize-space()='Saheli Mondal'])[1]")
    friends = (By.XPATH, "//span[contains(text(),'Friends')]")
    all_friends = (By.XPATH, "(//span[contains(text(),'All Friends')])[1]")
    icon = (By.XPATH, "(//*[name()='svg'][@class='x3ajldb'])[1]")

    def get_icon(self):
        self.driver.find_element(*HomePage.icon).click()

    def get_profile_name(self):
        self.driver.find_element(*HomePage.profile_name).click()

    def get_friends(self):
        self.driver.find_element(*HomePage.friends).click()

    def get_all_friends(self):
        self.driver.find_element(*HomePage.all_friends).click()
