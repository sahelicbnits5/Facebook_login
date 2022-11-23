from selenium.webdriver.common.by import By

from main.utilities.Baseclass import BaseClass


class ProfilePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    my_name = (By.XPATH, By.XPATH,"//h1[normalize-space()='Saheli Mondal']")

    def get_my_name(self):
        self.driver.find_element(*ProfilePage.my_name)

