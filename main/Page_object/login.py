from selenium.webdriver.common.by import By

from main.utilities.Baseclass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    mailId_input = (By.CSS_SELECTOR, "input[id='email']")
    pass_input = (By.CSS_SELECTOR, "input[id='pass']")
    login_btn = (By.XPATH, "//body/div/div/div[@role='main']/div/div/div/div/div/div/form["
                           "@data-testid='royal_login_form']/div[2]")

    def get_login_btn(self):
        self.driver.find_element(*LoginPage.login_btn).click()

    def get_mailid_input(self):
        return self.driver.find_element(*LoginPage.mailId_input)

    def get_pass_input(self):
        return self.driver.find_element(*LoginPage.pass_input)
