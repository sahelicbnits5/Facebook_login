import time
from selenium.webdriver.common.by import By
from main.Page_object.HomePage import HomePage
from main.Page_object.login import LoginPage
from main.utilities.Baseclass import BaseClass


class TestMain(BaseClass):
    def test_gmail(self, get_username, get_password):
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        login_page.get_mailid_input().send_keys(get_username)
        login_page.get_pass_input().send_keys(get_password)
        self.driver.implicitly_wait(3)

        self.element_wait_clickable(login_page.login_btn)
        login_page.get_login_btn()
        self.driver.implicitly_wait(3)
        homepage = HomePage(self.driver)
        self.element_wait_clickable(HomePage.friends)
        homepage.get_friends()
        self.driver.implicitly_wait(3)
        # self.element_wait_clickable(HomePage.all_friends)
        # homepage.get_all_friends()

        all_friends = self.driver.find_elements(By.XPATH, "(//span[contains(text(),'All Friends')])[1]")
        for all_friend in all_friends:
            all_friend.click()
            log.info(all_friend.text)

        # self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='x3ajldb'])[1]").click()
        self.element_wait_clickable(HomePage.icon)
        homepage.get_icon()
        self.driver.implicitly_wait(3)
        # homepage = HomePage(self.driver)
        self.element_wait_presence(HomePage.profile_name)
        homepage.get_profile_name()
        self.driver.implicitly_wait(3)
        name = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Saheli Mondal']")

        assert name.text == "Saheli Mondal"
        log.info(name.text)

        self.driver.get('https://scontent-ccu1-1.xx.fbcdn.net/v/t39.30808-1'
                        '/313988805_1101088350607443_911779667711543310_n.jpg?stp=dst-jpg_s320x320&_nc_cat=111&ccb=1'
                        '-7&_nc_sid=7206a8&_nc_ohc=1iLQmGVu4T8AX_Gbs6P&tn=REEti6s7m-1a7Ea2&_nc_ht=scontent-ccu1-1.xx'
                        '&oh=00_AfCCKsvXPQYFB7vVbYCZ8b2pFr85ACPHUn7bWNyzmPii_Q&oe=6382F7EA')
        self.driver.implicitly_wait(3)

        self.driver.get_screenshot_as_file("screenshot.png")


